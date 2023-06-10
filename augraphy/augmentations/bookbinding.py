import math
import random

import numpy as np
from numba import config
from numba import jit

from augraphy.augmentations.lib import four_point_transform
from augraphy.augmentations.pageborder import PageBorder
from augraphy.base.augmentation import Augmentation
from augraphy.utilities.overlaybuilder import OverlayBuilder


class BookBinding(Augmentation):
    """Creates a book binding effect with shadow and curved lines

    :param radius_range: The range of radius in pixels.
    :type radius_range: tuple, optional
    :param curve_range: Pixels by which the page text should be curved, suggested value is 1/8 of image width.
    :type curve_range: tuple, optional
    :param mirror_range: Tuple of floats to determine percentage of image to be mirrored.
    :type mirror_range: Tuple, optional
    :param curling_direction: The direction of page curling, -1: random, 0: up, 1: down.
    :type curling_direction: int, optional
    :param numba_jit: The flag to enable numba jit to speed up the processing in the augmentation.
    :type numba_jit: int, optional
    :param p: The probability that this Augmentation will be applied.
    :type p: float, optional

    """

    def __init__(
        self,
        radius_range=(1, 100),
        curve_range=(200, 300),
        mirror_range=(1.0, 1.0),
        curling_direction=-1,
        numba_jit=1,
        p=1,
    ):
        super().__init__(p=p, numba_jit=numba_jit)
        self.radius_range = radius_range
        self.curve_range = curve_range
        self.mirror_range = mirror_range
        self.curling_direction = curling_direction
        self.numba_jit = numba_jit
        config.DISABLE_JIT = bool(1 - numba_jit)

    def __repr__(self):
        return f"BookBinding(radius_range={self.radius_range}, curve_range={self.curve_range}, mirror_range={self.mirror_range}, curling_direction={self.curling_direction}, numba_jit={self.numba_jit}, p={self.p})"

    def add_book_shadow(self, img, radius, angle):
        """Add shadow effect in the input image.

        :param img: The image to apply the function.
        :type img: numpy.array (numpy.uint8)
        :param radius: Radius of the shadow effect.
        :type radius: int
        :param angle: Angle value to generate shadow effect.
        :type angle: int
        """

        rows = img.shape[0]
        cols = img.shape[1]

        # compute mask of shadow
        img_dist = np.repeat(np.arange(cols), rows)
        img_dist = np.transpose(img_dist.reshape(cols, rows))
        img_d = img_dist + (radius * (1 - math.cos(angle)))
        img_mask = (img_dist / img_d) ** 2
        
        min_value = np.min(img_mask)
        max_value = np.max(img_mask)
        
        # rescale maskto 0.2 - 1
        min_intensity = 0.2
        max_intensity = 1.0
        img_mask = ((img_mask - min_value) / (max_value - min_value)) * (max_intensity - min_intensity) + min_intensity
        
        
        # rescale 0- 1 to prevent darken of the image
#        img_mask = (img_mask - np.min(img_mask)) / (np.max(img_mask) - np.min(img_mask))

#        from matplotlib import pyplot as plt
#        plt.figure()
#        plt.imshow(img_mask)
#        raise ValueError('a')


        # overlay mask of shadow to input image
        ob = OverlayBuilder(
            "darken",
            (img_mask * 255).astype("uint8"),
            img,
            1,
            (1, 1),
            "center",
            0,
            1,
        )
        img_output = ob.build_overlay()

        return img_output.astype("uint8")

    def curve_page(self, img, curve_value):
        """Generate curvy effect in the input image.

        :param img: The image to apply the function.
        :type img: numpy.array (numpy.uint8)
        :param curve_value: Pixel number of the page text should be curved.
        :type curve_value: int

        """

        rows = img.shape[0]
        cols = img.shape[1]

        if curve_value > cols / 2:
            curve_value = int(cols / 2)

        # reassign variable name for clarity
        max_offset_y = curve_value

        if len(img.shape) > 2:
            channels = img.shape[2]
            img_output = np.zeros(
                (rows + max_offset_y, cols, channels),
                dtype=img.dtype,
            )

        else:
            img_output = np.zeros((rows + max_offset_y, cols), dtype=img.dtype)

        img_output = self.curve_page_processing(img, img_output, curve_value, rows, cols)

        return img_output

    @staticmethod
    @jit(nopython=True, cache=True)
    def curve_page_processing(img, img_output, curve_value, rows, cols):
        """Core function for curvy effect processing.

        :param img: The image to apply the function.
        :type img: numpy.array (numpy.uint8)
        :param img_output: The output image from the function.
        :type img_output: numpy.array (numpy.uint8)
        :param curve_value: Pixel number of the page text should be curved.
        :type curve_value: int
        :param rows: Number of rows in input image.
        :type rows: int
        :param cols: Number of columns in input image.
        :type cols: int
        """
        # x coordinate when offset_y starts to become negative
        x_negative = -1
        max_offset_y = curve_value
        for y in range(rows):
            y_new = y + max_offset_y
            for x in range(cols):

                offset_x = 0
                offset_y = int(curve_value * math.sin(2 * 3.14 * x / (3 * rows)))

                # for negative offset_y
                if offset_y < 0:
                    # set value of x when offset_y turns negative
                    if x_negative == -1:
                        x_negative = x

                    offseted_y = y - offset_y
                    offseted_x = x - offset_x
                    check_offset = y - offset_y
                # for positive offset_y
                else:
                    offseted_y = y + offset_y
                    offseted_x = x + offset_x
                    check_offset = y + offset_y

                # assign new y value
                if check_offset < rows:
                    img_output[y_new, x] = img[
                        (offseted_y) % (rows),
                        (offseted_x) % cols,
                    ]
                else:
                    # add top section
                    img_output[(y_new - rows), x] = img[
                        (offseted_y) % (rows),
                        (offseted_x) % cols,
                    ]

        # remove negative offset part
        if x_negative != -1:
            img_output = img_output[:, :x_negative]

        return img_output


    def curve_down_processing(self, image):
        
        
        radius = random.randint(self.radius_range[0], self.radius_range[1])
        angle = 30
        curve_value = random.randint(self.curve_range[0],self.curve_range[1])

        added_border_height = int(image.shape[0] / 20)
        
        # right side of image
        # create borders
        page_border = PageBorder(
                page_border_width_height=(int(added_border_height / 2), -added_border_height),
                page_border_color=(0, 0, 0),
                page_border_background_color=(0, 0, 0),
                page_numbers=random.randint(8, 12),
                page_rotation_angle_range=(3, 5),
                curve_frequency=(1, 3),
                curve_height=(1, 3),
                curve_length_one_side=(10, 10),
                same_page_border=0,
                numba_jit=1,
                p=1,
            )

        image_added_border_right = page_border(np.rot90(image,3))
        image_added_border_right = np.rot90(image_added_border_right[added_border_height:,:])
        
        # flipud to create a better curvy shape
        image_shadow_right = self.add_book_shadow(np.flipud(image_added_border_right), radius, angle)
        image_right = np.flipud(self.curve_page(image_shadow_right, curve_value))
        
        # left side of image
        # create borders
        page_border = PageBorder(
                page_border_width_height=(int(-added_border_height / 2), -added_border_height),
                page_border_color=(0, 0, 0),
                page_border_background_color=(0, 0, 0),
                page_numbers=random.randint(6, 8),
                page_rotation_angle_range=(2, 2),
                curve_frequency=(1, 3),
                curve_height=(1, 3),
                curve_length_one_side=(30, 90),
                same_page_border=0,
                numba_jit=1,
                p=1,
            )

        image_added_border_left = page_border(np.fliplr(image))
        
        from matplotlib import pyplot as plt
        plt.figure()
        plt.imshow(image_added_border_left)
        plt.title("after page broder")
        
        image_shadow_left = np.fliplr(self.add_book_shadow(image_added_border_left, radius, angle))
        
        image_shadow_left = image_shadow_left[:,:-int(added_border_height / 2)]
        
        plt.figure()
        plt.imshow(image_shadow_left)
        plt.title("after shadow")
        
        image_left = self.curve_page(np.fliplr(np.flipud(image_shadow_left)), curve_value * 3)
        
        from matplotlib import pyplot as plt
        plt.figure()
        plt.imshow(image_left)
        plt.title("after curve page")
        
        
        # further bend left image by using perspective transform
        ysize, xsize = image_left.shape[:2]
        curve_xsize = curve_value
        
#        random.randint(int(xsize / 10), int(xsize / 8))

        # bending size
#
#        curve_xsize = curve_value
#
#        # right image x and y size
        cysize, cxsize = image_right.shape[:2]
#
#        # source and target points of the bending process
        source_points = np.float32([[0, 0], [xsize, 0], [xsize, ysize], [0, ysize]])
        target_points = np.float32([[curve_xsize, 0], [xsize, 0], [xsize, ysize], [curve_xsize, ysize]])


        image_left = np.fliplr(np.flipud(image_left.astype("float"))) / 255

        plt.figure()
        plt.imshow(image_left)
        plt.title("left1")

#        image_left = np.fliplr(np.flipud(image_left))
        # get bended image
        image_left = (four_point_transform(image_left, source_points, target_points, cxsize, cysize) * 255).astype(
            "uint8",
        )
        
        plt.figure()
        plt.imshow(image_left)
        plt.title("left2")
        
        
        
        # remove the empty section after the transform
#        image_left = image_left[:, curve_xsize:]
        # generate range of mirror and crop image based on mirror size
        mirror_range = np.random.uniform(self.mirror_range[0], self.mirror_range[1])
        image_left = image_left[:cysize, image_left.shape[1] - int(image_left.shape[1] * mirror_range) :]
        # get new y and x size of left image
        ysize, xsize = image_left.shape[:2]

        plt.figure()
        plt.imshow(image_left)
        plt.title("left 3")


        # get their y difference
        y_diff = cysize - ysize

        # create new image with original size + mirror size
        image_output = np.zeros((ysize + y_diff, xsize + cxsize, image_right.shape[2])).astype(
            "uint8",
        )


        # merged left image and right image
        image_output[:, :xsize] = image_left

#        if y_diff != 0:
#            image_output[:-y_diff, xsize:] = image_right
#        else:
#            
            
        image_output[:, xsize:] = image_right


        
        
        return image_output

    def __call__(self, image, layer=None, force=False):
        image = image.copy()

        # get bending direction
        if self.curling_direction == -1:
            curve_down = random.choice([0, 1])
        else:
            curve_down = self.curling_direction


        if curve_down:
            image_output = self.curve_down_processing(image)
            
            return image_output

        '''


        radius = random.randint(self.radius_range[0], self.radius_range[1])
        angle = 30
        curve_value = max(
            int(image.shape[1] / 10),
            random.randint(
                self.curve_range[0],
                self.curve_range[1],
            ),
        )

        added_border_height = int(image.shape[0] / 10)

        # right page - add page border, add shadow and then bend page
        if curve_down:

            page_border = PageBorder(
                page_border_width_height=(int(added_border_height / 2), -added_border_height),
                page_border_color=(0, 0, 0),
                page_border_background_color=(0, 0, 0),
                page_numbers=random.randint(8, 12),
                page_rotation_angle_range=(3, 5),
                curve_frequency=(1, 3),
                curve_height=(1, 3),
                curve_length_one_side=(10, 10),
                same_page_border=0,
                numba_jit=1,
                p=1,
            )

            image_added_border_right = page_border(np.rot90(image,3))
            image_added_border_right = np.rot90(image_added_border_right[added_border_height:,:])
            
            # flipud to create a better curvy shape
            image_shadow_right = self.add_book_shadow(np.flipud(image_added_border_right), radius, angle)
            image_right = np.flipud(self.curve_page(image_shadow_right, curve_value))
            
        else:
            page_border = PageBorder(
                page_border_width_height=(int(added_border_height / 2), added_border_height),
                page_border_color=(0, 0, 0),
                page_border_background_color=(0, 0, 0),
                page_numbers=random.randint(6, 8),
                page_rotation_angle_range=(-3, 3),
                curve_frequency=(1, 3),
                curve_height=(1, 3),
                curve_length_one_side=(10, 10),
                same_page_border=0,
                numba_jit=1,
                p=1,
            )

            image_added_border_right = page_border(image)
            image_shadow_right = self.add_book_shadow(image_added_border_right, radius, angle)
            image_right = self.curve_page(image_shadow_right, curve_value)
            
            
        # left page - add page border, add shadow and then bend page
        if curve_down:
            page_border = PageBorder(
                page_border_width_height=(int(-added_border_height / 2), -added_border_height),
                page_border_color=(0, 0, 0),
                page_border_background_color=(0, 0, 0),
                page_numbers=random.randint(6, 8),
                page_rotation_angle_range=(3, 5),
                curve_frequency=(1, 3),
                curve_height=(1, 3),
                curve_length_one_side=(30, 90),
                same_page_border=0,
                numba_jit=1,
                p=1,
            )

            image_added_border_left = page_border(np.fliplr(image))
            
            from matplotlib import pyplot as plt
            plt.figure()
            plt.imshow(image_added_border_left)
            plt.title("after page broder")
            
            image_shadow_left = np.fliplr(self.add_book_shadow(image_added_border_left, radius, angle))
            
            image_shadow_left = image_shadow_left[:,:-int(added_border_height / 2)]
            
            plt.figure()
            plt.imshow(image_shadow_left)
            plt.title("after shadow")
            
            image_left = self.curve_page(np.fliplr(np.flipud(image_shadow_left)), curve_value * 3)
            
            from matplotlib import pyplot as plt
            plt.figure()
            plt.imshow(image_left)
            plt.title("after curve page")
            
#            raise ValueError('a')
            
        else:
            page_border = PageBorder(
                page_border_width_height=(int(-added_border_height / 2), -added_border_height),
                page_border_color=(0, 0, 0),
                page_border_background_color=(0, 0, 0),
                page_numbers=random.randint(6, 8),
                page_rotation_angle_range=(-3, 3),
                curve_frequency=(1, 3),
                curve_height=(1, 3),
                curve_length_one_side=(30, 90),
                same_page_border=0,
                numba_jit=1,
                p=1,
            )

            image_added_border_left = page_border(np.fliplr(np.flipud(image)))
            
            
            
            image_shadow_left = np.fliplr(self.add_book_shadow(image_added_border_left, radius, angle))
            if image.shape[1] > image.shape[0]:
                left_curve_value = curve_value
            else:
                left_curve_value = curve_value * 3
            image_left = self.curve_page(np.flipud(image_shadow_left), left_curve_value)




        # further bend left image by using perspective transform
        ysize, xsize = image_left.shape[:2]
#        curve_xsize = curve_value*2
        
#        random.randint(int(xsize / 10), int(xsize / 8))

        # bending size

        curve_xsize = curve_value*2

        # right image x and y size
        cysize, cxsize = image_right.shape[:2]

        # source and target points of the bending process
        source_points = np.float32([[0, 0], [cxsize, 0], [cxsize, cysize], [0, cysize]])
        target_points = np.float32([[curve_xsize, 0], [cxsize, 0], [cxsize, cysize], [curve_xsize, cysize]])

        if curve_down:
            img_left = np.fliplr(np.flipud(image_left.astype("float"))) / 255
        else:
            img_left = image_left.astype("float") / 255

        # get bended image
        image_left = (four_point_transform(img_left, source_points, target_points, cxsize, cysize) * 255).astype(
            "uint8",
        )
        
        plt.figure()
        plt.imshow(image_left)
        plt.title("left")
        
        
        
        # remove the empty section after the transform
        image_left = image_left[:, curve_xsize:]
        # generate range of mirror and crop image based on mirror size
        mirror_range = np.random.uniform(self.mirror_range[0], self.mirror_range[1])
        image_left = image_left[:, image_left.shape[1] - int(image_left.shape[1] * mirror_range) :]
        # get new y and x size of left image
        ysize, xsize = image_left.shape[:2]

        # get their y difference
        y_diff = cysize - ysize

        if not curve_down:
            image_left = np.fliplr(self.add_book_shadow(np.fliplr(image_left), radius, angle))

        # create new image with original size + mirror size
        if len(image_right.shape) > 2:
            new_image = np.zeros((ysize + y_diff, xsize + cxsize, image_right.shape[2])).astype(
                "uint8",
            )
        else:
            new_image = np.zeros((ysize + y_diff, xsize + cxsize)).astype("uint8")

        # merged left image and right image
        if curve_down:
            new_image[:, :xsize] = image_left
        else:
            if image.shape[0] < image.shape[1]:
                start_y = 0
                new_image[start_y : image_left.shape[0], :xsize] = image_left
            else:
                start_y = curve_value
                random_offset = random.randint(int(ysize / 30), int(ysize / 25))
                random_offset = 0
                new_image[start_y - random_offset :, :xsize] = image_left[: -start_y + random_offset, :]
        if y_diff != 0:
            new_image[:-y_diff, xsize:] = image_right
        else:
            new_image[:, xsize:] = image_right

        image_out = new_image

        return image_out
        '''