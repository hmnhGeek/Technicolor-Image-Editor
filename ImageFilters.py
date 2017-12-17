import cv2
import argparse as ap

class ImageFilters(object):

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def recolor_to_RC(self, scaling_factor):

        """RC (red, cyan): Note that red and cyan can mix to make grays. This color
            space resembles Technicolor Process 2 and CGA Palette 3."""

        src = cv2.imread(self.source)
        dest = src.copy()

        # Take the pixel values
        b, g, r = cv2.split(src)

        # Apply Technicolor 1
        cv2.addWeighted(b, scaling_factor, g, scaling_factor, 0, b)

        # Merge at the destination image.
        cv2.merge((b, b, r), dest)

        cv2.imwrite(self.destination, dest)

    def recolor_to_RGV(self):

        """Simulate conversion from BGR to RGV (red, green, value).
            The source and destination images must both be in BGR format.
            Blues are desaturated."""

        src = cv2.imread(self.source)
        dest = src.copy()

        # Take the pixel values
        b, g, r = cv2.split(src)

        # Apply RGV
        cv2.min(b, g, b)
        cv2.min(b, r, b)

        # Merge at the destination image.
        cv2.merge((b, g, r), dest)

        cv2.imwrite(self.destination, dest)

    def recolor_to_CMV(self):

        """Simulate conversion from BGR to CMV (cyan, magenta, value).
            The source and destination images must both be in BGR format.
            Yellows are desaturated."""

        src = cv2.imread(self.source)
        dest = src.copy()

        # Take the pixel values
        b, g, r = cv2.split(src)

        # Apply CMV
        cv2.max(b, g, b)
        cv2.max(b, r, b)

        # Merge at the destination image.
        cv2.merge((b, g, r), dest)

        cv2.imwrite(self.destination, dest)
