"""Unit tests for the tracking module.

Implement your tracking module so that all tests pass.
An example of how to run these tests is given in run_tests.sh.

The tests below will be used to test the correctness of your
implementation.

You should add additional detailed tests as you add more
of your own functions to your implementation!
"""

import cv2
import tracking
import numpy
import unittest


class TestTracking(unittest.TestCase):
    """Tests the functionality of the tracking module."""

    def setUp(self):
        """Initializes shared state for unit tests."""
        # Read the ground-truth ball bounds.
        with open('test_data/ball_bounds.txt', 'r') as f:
            self.ball_bounds = [map(int, line.split())
                                for line in f.readlines()]

        # Read the ground-truth face bounds.
        with open('test_data/face_bounds.txt', 'r') as f:
            self.face_bounds = [map(int, line.split())
                                for line in f.readlines()]

        # 10 pixels of error per frame for ball tracking.
        self.max_ball_diff = len(self.ball_bounds) * 10

        # 100 pixels of error per frame for face tracking.
        self.max_face_diff = len(self.face_bounds) * 100

    def _tracking_bounds_diff(self, expected_bounds, actual_bounds):
        """Computes the difference, in pixels, between tracked bounds."""
        self.assertEqual(len(actual_bounds), len(expected_bounds))
        tracking_diff = 0
        for expected, actual in zip(expected_bounds, actual_bounds):
            tracking_diff += sum(numpy.abs(
                numpy.array(expected) - numpy.array(actual)))
        print "Total of %d pixels of bounds difference across %d frames" % (
            tracking_diff, len(expected_bounds))
        return tracking_diff

    def track_ball_with_function_(self, video_filename, tracking_function):
        """Tracks the ball in 'video_filename' with 'tracking_function'."""
        video = cv2.VideoCapture(video_filename)
        bounds = tracking_function(video)
        bounds_diff = self._tracking_bounds_diff(self.ball_bounds, bounds)
        self.assertLessEqual(bounds_diff, self.max_ball_diff)

    def test_track_ball_1(self):
        """Tests that the ball in ball_1.mov is correctly tracked."""
        self.track_ball_with_function_(
            "test_data/ball_1_frames/frame_%03d.png", tracking.track_ball_1)

    def test_track_ball_2(self):
        """Tests that the ball in ball_2.mov is correctly tracked."""
        self.track_ball_with_function_(
            "test_data/ball_2_frames/frame_%03d.png", tracking.track_ball_2)

    def test_track_ball_3(self):
        """Tests that the ball in ball_3.mov is correctly tracked."""
        self.track_ball_with_function_(
            "test_data/ball_3_frames/frame_%03d.png", tracking.track_ball_3)

    def test_track_ball_4(self):
        """Tests that the ball in ball_4.mov is correctly tracked."""
        self.track_ball_with_function_(
            "test_data/ball_4_frames/frame_%03d.png", tracking.track_ball_4)

    def test_track_face(self):
        """Tests that the face in face.mov is correctly tracked."""
        video = cv2.VideoCapture('test_data/face_frames/frame_%03d.png')
        bounds = tracking.track_face(video)
        bounds_diff = self._tracking_bounds_diff(self.face_bounds, bounds)
        self.assertLessEqual(bounds_diff, self.max_face_diff)


if __name__ == '__main__':
    unittest.main()
