Project 3: Tracking
========

## Due: 4 Nov 2014, 11:59pm
## Code reviews due: 7 Nov 2014, 11:59pm
## Final code revisions due: 11 Nov 2014, 11:59pm

In this project, you'll track objects in video sequences. There are many effective methods to do this for the problems provided, so unlike previous projects, you will have to choose which particular approach works best for you for each problem case. I suggest a thorough consideration of OpenCV's libraries when designing solutions.

Think back over the different methods for tracking and motion detection discussed in class, including background subtraction, optical flow, sparse feature tracking, and Kalman filtering. You can use any combination of these techniques (and others!) to accomplish your tracking tasks.

### Tracking the bounds of a solid-colored ball (50 points)

<img height="350" src="https://raw.githubusercontent.com/ut-cs378-vision-2014fall/course-info/master/images/ball_frame.png"/>

For this part of the project, you'll track a ball as it moves across different background fields. There are four input videos, `ball_{1,2,3,4}.mov`. You'll need to track the ball's motion in each video.

Implement four functions, `track_ball_{1,2,3,4}()`, which track the bounds of the ball in each of the four input videos. It's likely that the implementation of these four functions will share some helper functions, or may just call a single shared implementation, perhaps with different parameters.

Your function will return, for each frame of the video, the `(min_x, min_y, max_x, max_y)` tuple describing the rectangular bounding box around the ball. The bounds will be compared against the ground truth bounds in `test_data/ball_bounds.txt`.

Your implementation may not make use of any "ground truth" information about the videos that it does not determine on its own, including the ball's color, initial location, dimensions, or motion.

### Tracking the location of a face (30 points)

<img height="350" src="https://raw.githubusercontent.com/ut-cs378-vision-2014fall/course-info/master/images/face_track_frame.png"/>

For this part of the project, you will track a face as it moves in a real video. You will implement a `track_face()` function that returns output of the same format as your ball tracking functions: a per-frame `(min_x, min_y, max_x, max_y)` bounding box of the face. You will likely need more sophisticated detection to find a face compared with a ball.

Your implementation may not make sue of any "ground truth" information about the video that it does not determine on its own, including the face's initial location or motion.

### Code quality and review (20 points)

Above and beyond just passing the pep8 style checker, you should strive to write readable, modular, well-factored code. As in project 1, each group will review three other groups code, and then receive ratings on the quality of their review. You'll receive up to 5 points for the quality of your groups review. After you revise your code in response to review, we'll go over your final code and rate it's quality for up to another 15 points. Hint: the style and comments of OpenCV tutorials is not a model you should emulate :)

### Extra credit (maximum of 50 points)

Tracking is a broad research topic, and we're only scratching the surface with the above tasks. If you like, you can do additional implementation work for extra credit.

Be sure to include code for the extra credit as part of your check-in. Also, please add a PDF write-up describing which extra credit you implemented including your results called `extra_credit.pdf` in the project_3 directory so we can see your results.

#### Track multiple pedestrians in a street video (20 points)

Download the ETH annotated pedestrian video dataset from [here](http://www.vision.ee.ethz.ch/datasets_extra/ewap_dataset_full.tgz). Implement multi-object tracking for pedestrians in the video, and compare your results to the labeled ground truth.

#### Composite a 3D object onto a planar surface in a video (30 points)

Similar to effects in [this video](https://www.youtube.com/watch?v=Y9HMn6bd-v8), use parallax effects in tracked features in a video to establish a planar surface in the scene, and then composite a 3D model onto the planar surface. Produce a video of the result.

## Logistics

You will work on this project in randomly assigned groups of three. All group members should have identical submissions in each of their private repositories by the project due date. We will select one group member's repository, clone it, and use it to compute the grade for all group members.

If the group chooses to turn in a project N days late, each individual in the group will lose N of their remaining late days for the semester. If one or more students have no more late days left, they'll lose credit without affecting the other group members' grades.


