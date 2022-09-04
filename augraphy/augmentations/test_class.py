
class test_class123(object):
    """This is a testing class

    :param abc: test 1
    :type abc: int, optional
    :param bbb: test2
    :type bbb: int optional
    """

    def __init__(self, abc=0, bbb=0):
        """Constructor method
        """

        self=abc = abc
        self.bbb=bbb




class Inkbleed2(object):
    """Uses Sobel edge detection to create a mask of all edges, then applies
    random noise to those edges. When followed by a blur, this creates a
    fuzzy edge that emulates an ink bleed effect.

    :param intensity_range: Pair of floats determining the range from which
           noise intensity is sampled.
    :type intensity: tuple, optional
    :param color_range: Pair of ints determining the range from which color
           noise is sampled.
    :type color_range: tuple, optional
    :param kernel_size: Kernel size to determine area of inkbleed effect.
    :type kernel_size: tuple, optional
    :param severity: Severity to determine concentration of inkbleed effect.
    :type severity: tuple, optional
    :param p: The probability this Augmentation will be applied.
    :type p: float, optional
    """

    def __init__(
        self,
        intensity_range=(0.1, 0.2),
        color_range=(0, 224),
        kernel_size=(5, 5),
        severity=(0.4, 0.6),
        p=1,
    ):
        """Constructor method"""
        self.intensity_range = int
        self.color_range=color_range
        self.kernel_size = self.kernel_size
        self.severity = self.severity
        