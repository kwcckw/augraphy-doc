# augraphy-doc

<p align="center">
    <img src="https://github.com/sparkfish/augraphy/blob/dev/images/logo/augraphy.png?raw=true" width="600" title="Augraphy Logo">
</p>


# Additional Target Support
Some augmentations support additional inputs such as mask, keypoints and bounding boxes. 

|    Augmentation    |      Image      |       Mask      |    Keypoints    | Bounding Boxes  |
|--------------------|----------------:|----------------:|----------------:|----------------:|
|BadPhotoCopy        |        ✓        |        -        |        -        |        -        |
|BindingsAndFasteners|        ✓        |        -        |        -        |        -        |
|BleedThrough        |        ✓        |        -        |        -        |        -        |
|BookBinding         |        ✓        |        -        |        -        |        -        |
|Brightness          |        ✓        |        -        |        -        |        -        |
|BrightnessTexturize |        ✓        |        -        |        -        |        -        |
|ColorPaper          |        ✓        |        -        |        -        |        -        |
|ColorShift          |        ✓        |        -        |        -        |        -        |
|DelaunayTessellation|        ✓        |        -        |        -        |        -        |
|DirtyDrum           |        ✓        |        -        |        -        |        -        |
|DirtyRollers        |        ✓        |        -        |        -        |        -        |
|Dithering           |        ✓        |        -        |        -        |        -        |
|DotMatrix           |        ✓        |        -        |        -        |        -        |
|Faxify              |        ✓        |        -        |        -        |        -        |
|Folding             |        ✓        |        -        |        -        |        -        |
|Gamma               |        ✓        |        -        |        -        |        -        |
|Geometric           |        ✓        |        -        |        -        |        -        |
|GlitchEffect        |        ✓        |        -        |        -        |        -        |
|Hollow              |        ✓        |        -        |        -        |        -        |
|InkBleed            |        ✓        |        -        |        -        |        -        |
|InkColorSwap        |        ✓        |        -        |        -        |        -        |
|InkMottling         |        ✓        |        -        |        -        |        -        |
|InkShifter          |        ✓        |        -        |        -        |        -        |
|Jpeg                |        ✓        |        -        |        -        |        -        |
|Letterpress         |        ✓        |        -        |        -        |        -        |
|LightingGradient    |        ✓        |        -        |        -        |        -        |
|LinesDegradation    |        ✓        |        -        |        -        |        -        |
|LowInkPeriodicLines |        ✓        |        -        |        -        |        -        |
|LowInkRandomLines   |        ✓        |        -        |        -        |        -        |
|LowLightNoise       |        ✓        |        -        |        -        |        -        |
|Markup              |        ✓        |        -        |        -        |        -        |
|NoiseTexturize      |        ✓        |        -        |        -        |        -        |
|NoisyLines          |        ✓        |        -        |        -        |        -        |
|PageBorder          |        ✓        |        -        |        -        |        -        |
|PatternGenerator    |        ✓        |        -        |        -        |        -        |
|ReflectedLight      |        ✓        |        -        |        -        |        -        |
|Scribbles           |        ✓        |        -        |        -        |        -        |
|SectionShift        |        ✓        |        -        |        -        |        -        |
|ShadowCast          |        ✓        |        -        |        -        |        -        |
|Squish              |        ✓        |        -        |        -        |        -        |
|SubtleNoise         |        ✓        |        -        |        -        |        -        |
|VoronoiTessellation |        ✓        |        -        |        -        |        -        |
|WaterMark           |        ✓        |        ✕        |        ✕        |        -        |

Remarks: <br />
[-] : augmentation doesn't affect this input. <br />
[✓] : augmentation is supported on this input. <br />
[✕] : augmentation is not supported on this input. <br />