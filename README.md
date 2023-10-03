# augraphy-doc

<p align="center">
    <img src="https://github.com/sparkfish/augraphy/blob/dev/images/logo/augraphy.png?raw=true" width="600" title="Augraphy Logo">
</p>


# List of Augmentations
## Pixel Level Augmentations
Pixel level augmentations apply augmentation to the input image only, that including alpha layer of the image. Additional inputs such as mask, keypoints or bounding boxes will not be affected.

|    Augmentation    |      Image      |   Alpha Layer   |
|--------------------|----------------:|----------------:|
|BadPhotoCopy        |        ✓        |        -        |
|BindingsAndFasteners|        ✓        |        -        |
|BleedThrough        |        ✓        |        -        |
|Brightness          |        ✓        |        -        |
|BrightnessTexturize |        ✓        |        -        |
|ColorPaper          |        ✓        |        -        |
|ColorShift          |        ✓        |        -        |
|DelaunayTessellation|        ✓        |        -        |
|DirtyDrum           |        ✓        |        -        |
|DirtyRollers        |        ✓        |        -        |
|Dithering           |        ✓        |        -        |
|DotMatrix           |        ✓        |        -        |
|Faxify              |        ✓        |        -        |
|Gamma               |        ✓        |        -        |
|Hollow              |        ✓        |        -        |
|InkBleed            |        ✓        |        -        |
|InkColorSwap        |        ✓        |        -        |
|InkMottling         |        ✓        |        -        |
|Jpeg                |        ✓        |        -        |
|Letterpress         |        ✓        |        -        |
|LightingGradient    |        ✓        |        -        |
|LinesDegradation    |        ✓        |        -        |
|LowInkPeriodicLines |        ✓        |        -        |
|LowInkRandomLines   |        ✓        |        -        |
|LowLightNoise       |        ✓        |        -        |
|Markup              |        ✓        |        -        |
|NoiseTexturize      |        ✓        |        -        |
|NoisyLines          |        ✓        |        -        |
|PatternGenerator    |        ✓        |        -        |
|ReflectedLight      |        ✓        |        -        |
|Scribbles           |        ✓        |        -        |
|ShadowCast          |        ✓        |        -        |
|SubtleNoise         |        ✓        |        -        |
|VoronoiTessellation |        ✓        |        -        |
|WaterMark           |        ✓        |        -        |

## Spatial level Augmentations
Spatial level augmentations apply augmentation to all inputs such as image (including alpha layer), mask, keypoints and bounding boxes.


|    Augmentation    |      Image      |   Alpha Layer   |       Mask      |    Keypoints    | Bounding Boxes  |
|--------------------|----------------:|----------------:|----------------:|----------------:|----------------:|
|BookBinding         |        ✓        |        ✓        |        ✓        |        ✓        |        ✓*       |
|Folding             |        ✓        |        ✓        |        ✓        |        ✓        |        ✓*       |
|Geometric           |        ✓        |        ✓        |        ✓        |        ✓        |        ✓*       |
|GlitchEffect        |        ✓        |        ✓        |        ✓        |        ✓        |        ✓*       |
|InkShifter          |        ✓        |        ✓        |        ✓        |        ✕        |        ✕        |
|PageBorder          |        ✓        |        ✓        |        ✓        |        ✓        |        ✓*       |
|SectionShift        |        ✓        |        ✓        |        ✓        |        ✓        |        ✓*       |
|Squish              |        ✓        |        ✓        |        ✓        |        ✓        |        ✓*       |

Remarks: <br />
[-] : augmentation doesn't affect this input. <br />
[✓] : augmentation is supported on this input. <br />
[✕] : augmentation is not supported on this input. <br />
[✓*] : augmentation is supported on this input under certain criteria. <br />