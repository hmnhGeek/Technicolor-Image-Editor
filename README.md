# Channel Mixing (Technicolor and Other Filters)

__Channel mixing__ is a simple technique for remapping colors. The color at a
destination pixel is a function of the color at the corresponding source pixel (only).
More specifically, each channel's value at the destination pixel is a function of any or
all channels' values at the source pixel.

## Technicolor
Technicolor is a series of color motion picture processes, the first version dating from 1916, and followed by improved versions over several decades.

## Technicolor Process 2
Convinced that there was no future in additive color processes, Comstock, Wescott, and Kalmus focused their attention on subtractive color processes. This culminated in what would eventually be known as Process 2 (1922) (in the later 1900s commonly called by the misnomer, "two-strip Technicolor"). As before, the special Technicolor camera used a beam-splitter that simultaneously exposed two consecutive frames of a single strip of black-and-white film, one behind a green filter and one behind a red filter.
A sample image of popular character donald duck is shown below. On left, donald duck is in Technicolor process 2 and on right is the original image.

![Donald Duck in Technicolor Process 2]()

## Technicolor Process 1
Technicolor originally existed in a two-color (red and green) system. In Process 1 (1916), a prism beam-splitter behind the camera lens exposed two consecutive frames of a single strip of black-and-white negative film simultaneously, one behind a red filter, the other behind a green filter. Because two frames were being exposed at the same time, the film had to be photographed and projected at twice the normal speed. Exhibition required a special projector with two apertures (one with a red filter and the other with a green filter), two lenses, and an adjustable prism that aligned the two images on the screen.
A sample image of popular character donald duck is shown below. On left, donald duck is in Technicolor process 1 and on right is the original image.

![Donald Duck in Technicolor Process 1]()

## CGA Palette 1
Simulating CMV color space is quite similar to simulating RGV, except that the
desaturated part of the spectrum is yellow instead of blue. To desaturate yellows,
we should increase B values to the per-pixel maximum of B, G, and R.
A sample image of popular character donald duck is shown below. On left, donald duck is in CGA Palette 1 and on right is the original image.

![CMV Palette 1 Donald Duck]()

## Using GUI
Clone this repository and then in that directory run gui.py.
