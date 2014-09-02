Project 0: Setup and Image Manipulation
========

## Due: 4 Sept 2014, 11:59pm

You will work on the first project individually.

## Step 1: Install Python/Numpy/OpenCV

Follow the instructions [here](https://github.com/ut-cs378-vision-2014fall/course-info/blob/master/installing_open_cv.md).

## Step 2: Set up your git repo

Follow the instructions [here](https://github.com/ut-cs378-vision-2014fall/course-info/blob/master/github_setup.md)

## Step 3: Implement your solutions

Your goal is to implement everything necessary for the unit tests in `image_manipulation_test.py` to pass. Put your implementation in `image_manipulation.py`. You can test your current implementation at any time with the `run_tests.sh` script. When everything is complete, you should get output like the following:

```bash
$ ./run_tests.sh 
No style errors found. You're so hip!

test_flip_image (image_manipulation_test.TestImageManipulation)
Tests the flip_image function. ... ok
test_negate_image (image_manipulation_test.TestImageManipulation)
Tests the invert_image function. ... ok
test_swap_red_and_green (image_manipulation_test.TestImageManipulation)
Tests the swap_red_and_green function. ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.437s

OK
All unit tests passing. Congrats!
```

## Step 4: Submit your solution

As described in the [GitHub setup guide](https://github.com/ut-cs378-vision-2014fall/course-info/blob/master/github_setup.md), your local repository should be configured to push your changes to your private GitHub repo. To submit your implementation at any time, just run `git push` from within your repository.

You can `git push` as often as you like before the submission deadline. At the deadline, we'll take a snapshot of your GitHub repository and use that for grading. If you submit your solution late, be sure to notify the TA by email as described in [the syllabus](https://github.com/ut-cs378-vision-2014fall/course-info).

For this first assignment, if all the unit tests pass, and you have no style errors, you'll receive full credit! Points will be deducted from a maximum of 100 for each failing test and for style violations:
* -20 points per failing test, up to -60 total
* -1 point per pep8 style violation, up to -20 total 
