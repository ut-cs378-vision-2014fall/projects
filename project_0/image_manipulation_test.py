"""Unit tests for the image_manipulation module.

Implement your image_manipulation module so that all tests pass.
An example of how to run these tests is given in run_tests.sh.

Don't edit this file! An unchanged version will test your code.
"""

import cv2
import image_manipulation
import numpy
import unittest


def _sparse_pixels(image, stride=50):
    """Returns pixels sparsely sampled by 'stride' in 'image.'"""
    rows, cols, _ = image.shape
    for row in range(0, rows, stride):
        for col in range(0, cols, stride):
            yield row, col


class TestImageManipulation(unittest.TestCase):
    """Tests the functionality of the image_manipulation module."""

    def setUp(self):
        """Initializes shared state for unit tests."""
        self.nyc_image = cv2.imread("test_data/nyc.jpg")

    def _assert_pixels_equal(self, row, col, expected_pixel, actual_pixel):
        """Asserts deep equality between expected_pixel and actual_pixel."""
        self.assertTrue(
            numpy.array_equal(expected_pixel, actual_pixel),
            "Expected pixel (%d, %d) = %s, actual %s" % (
                col, row, expected_pixel, actual_pixel))

    def test_flip_image(self):
        """Tests the flip_image function."""

        # Test each combination of horizontal and vertical flipping.
        for horizontal in (False, True):
            for vertical in (False, True):
                nyc_flipped = image_manipulation.flip_image(
                    numpy.copy(self.nyc_image), horizontal, vertical)

                rows, cols, _ = self.nyc_image.shape
                for row, col in _sparse_pixels(numpy.copy(self.nyc_image)):
                    row_flipped = rows - row - 1 if vertical else row
                    col_flipped = cols - col - 1 if horizontal else col
                    expected_pixel = self.nyc_image[row_flipped, col_flipped]
                    self._assert_pixels_equal(
                        row, col, expected_pixel, nyc_flipped[row, col])

    def test_negate_image(self):
        """Tests the negate_image function."""

        nyc_negated = image_manipulation.negate_image(self.nyc_image)

        for row, col in _sparse_pixels(self.nyc_image):
            expected_pixel = [255, 255, 255] - self.nyc_image[row, col]
            self._assert_pixels_equal(
                row, col, expected_pixel, nyc_negated[row, col])

    def test_swap_blue_and_green(self):
        """Tests the swap_blue_and_green function."""
        nyc_swapped = image_manipulation.swap_blue_and_green(
            numpy.copy(self.nyc_image))

        for row, col in _sparse_pixels(self.nyc_image):
            expected_pixel = []
            expected_pixel.append(self.nyc_image[row, col, 1])  # First green.
            expected_pixel.append(self.nyc_image[row, col, 0])  # Then blue.
            expected_pixel.append(self.nyc_image[row, col, 2])  # Then red.
            self._assert_pixels_equal(
                row, col, expected_pixel, nyc_swapped[row, col])

if __name__ == '__main__':
    unittest.main()
