*******
Folding
*******

.. autoclass:: augraphy.augmentations.folding.Folding
    :members:
    :undoc-members:
    :show-inheritance:

--------
Overview
--------
The Folding augmentation emulates folded paper being scanned, with a visible warp effect around the fold line.

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
In this example, a Folding augmentation instance is initialized and the folding count is set to 4 (4).
Noise at folding area is set to low value (0.1).
Each folding gradient width is set to low value (0.1, 0.2) and folding gradient height is to very low value (0.01, 0.02).

Code example:

::

    folding = Folding(fold_count=4,
                      fold_noise=0.1,
                      gradient_width=(0.1, 0.2),
                      gradient_height=(0.01, 0.1)
                      )

    img_folded= folding(image)
    cv2.imshow("folding", img_folded)

Augmented image:

.. figure:: augmentations/folding/folding.png
