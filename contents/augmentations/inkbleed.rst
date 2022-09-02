********
Inkbleed
********

The Ink Bleed augmentation relies on Sobel edge detection to create a mask of all edges, then applies random noise to those edges. When followed by a blur, this creates a fuzzy edge that emulates an ink bleed effect.


| Parameter         | Description                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `intensity_range` | Range of intensities to select from. Intensity must be a value between 0 to 1 and specifies the intensity of the noise added to the edges. |
| `color_range`     | The value range of the colors used for noise.                                                                                              |
| `kernel_size`     | Kernel size to determine area of inkbleed effect.                                                                                          |
| `severity`        | Severity to determine concentration of inkbleed effect.                                                                                    |
| `p`               | The probability that this augmentation will be applied.                                                                                    |






