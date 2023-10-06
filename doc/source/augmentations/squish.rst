******
Squish
******

.. autoclass:: augraphy.augmentations.squish.Squish
    :members:
    :undoc-members:
    :show-inheritance:

--------
Overview
--------
The Squish augmentation creates a squish effect by removing a fixed horizontal or vertical section of the image. For additional input such as mask and keypoints, they are fully supported. For bounding boxes, they will be affected only if the starting point or ending point of the box is in the squishing area.

Initially, a clean image with single line of text is created.

Code example:

::

    # import libraries
    import cv2
    import numpy as np
    from augraphy import *


    # create a clean image with single line of text
    image = np.full((500, 1500,3), 250, dtype="uint8")
    cv2.putText(
        image,
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        (80, 250),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        0,
        3,
    )

    cv2.imshow("Input image", image)

Clean image:

.. figure:: augmentations/input.png

---------
Example 1
---------
In this example, a Squish augmentation instance is initialized and the squish direction is set to vertical (1).
The location of squish effect is set to random location ("random").
The number of squish effect is set to random value in between 5 and 10 (5,10).
The squished distance in each squish effect is set to random value in between 5 and 7 (5, 7).
Squish line will be drawn randomly in each squish effect ("random").
The thickness of each squish line is set to 1 (1,1).

Code example:

::

    squish = Squish(squish_direction = 1,
                    squish_location = "random",
                    squish_number_range = (5,10),
                    squish_distance_range = (5,7),
                    squish_line = "random",
                    squish_line_thickness_range = (1,1)
                    )

    img_squish = squish(image)

    cv2.imshow("squish", img_squish)

Augmented image:

.. figure:: augmentations/squish/squish.png

---------
Example 2
---------
In this example, a Squish augmentation will be applied to additional inputs such as mask, keypoints and bounding boxes.
The Squish augmentation will be using the default parameters value and hence no additional parameters value will be specified.

Code example:

::

    squish = Squish()

    img_squish, mask, keypoints, bounding_boxes = squish(image=image, mask=mask, keypoints=keypoints, bounding_boxes=bounding_boxes)

    cv2.imshow("squish", img_squish)


Input mask:

.. figure:: augmentations/input_mask.png

Input keypoints:

.. figure:: augmentations/input_keypoints.png

Input bounding boxes:

.. figure:: augmentations/input_bounding_boxes.png

Augmented image:

.. figure:: augmentations/squish/squish2.png

Augmented mask:

.. figure:: augmentations/squish/squish2_mask.png

Augmented keypoints:

.. figure:: augmentations/squish/squish2_keypoints.png

Augmented bounding boxes:

.. figure:: augmentations/squish/squish2_bounding_boxes.png
