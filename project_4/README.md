Final Project
========

<img height="350" src="https://raw.githubusercontent.com/ut-cs378-vision-2014fall/course-info/master/images/sfm_header.png"/>

For your final project, you'll tackle a problem related to 3D reconstruction and computer vision. This will include:

* A detailed proposal of the problem you plan to solve.
* Two progress reports on your implementation.
* A final report detailing your approach and results.
* A ten-minute in-class presentation of your results.

### Project proposal (20 points), Due 28 Oct, 11:59pm

It is up to each group to select a project topic. You'll present your idea in a project proposal, which I'll evaluate to make sure that it has appropriate scope, difficulty, and to help get you started researching how to accomplish your implementation.

As we covered various topics related to 3D reconstruction and computer vision this semester, I've tried to highlight particular problems and applications that seemed like good candidates for final projects. Look over the course meeting notes to remind yourself of what we've covered so far and to motivate your selection of a topic. That said, you need not limit yourself to things we've explicitly covered in class meetings.

The first step of your project will be to submit a project proposal including:

* Members of your group and group name
* Project topic
* Objectives with associated measurable results
* Planned schedule for meeting objectives

#### Groups

You are free to self-organize into any group you like as long as it has at least three and no more than five members. List your group members and any filename-safe team name you like (used for managing code and submissions) in your proposal. I expect larger groups to take on more ambitious projects.

#### Topic requirements

Although you have a lot of latitude in the topic of your project, it must meet at least the following requirements:

* It has some component where 3D information is deduced from 2D images.
* It demands substantial implementation effort on your part (i.e., original code creation).
* It has a reasonable probability of success given the time and resources available to you.

Aim high! It is better to be too ambitious and fail to meet some of your goals than to select too simple of a project. I will take into account the difficulty of the project when evaluating it.

#### Objectives and associated results

Given the topic you plan to approach, determine at least three high-level objectives that you are aiming for. For each objective, identify at least one measureable result that confirms whether and to what extent you have met the objective. Here are some example objectives and associated results:

* Objective: Reconstruct a room with my cell phone camera
  * Result: A phone app that tracks 100 or more 3D points accurately in real-time.
  * Result: A 3D point cloud which measures major dimensions of the room with in 10% of true dimensions.

* Objective: Insert an image on the football field of a UT home game.
  * Result: A still image of the field with 99% of foreground pixels removed.
  * Result: A 5-second gameplay clip including a pan where the playing field bounds are estimated to within 10% accuracy.

* Objective: Control a mouse cursor by tracking a hand in a cell phone video.
  * Result: Succesfully segment a hand from 90% of video frames with a clean background.
  * Result: Send an email entirely using the system.

#### Planned schedule for meeting objectives

For each result you listed, estimate the effort required to complete it, and the date on which you expect to have achieved that result. The more detailed you make your results, the easier this estimation will be, and the better chance you'll have of finishing your project on schedule.

If you like, you can assign particular objectives and/or results to specific group members--whatever works best for you.

#### How to turn in

By the due date, place a file `proposal.pdf` in the `project_4` repository of your group members.

### Progress Report 1 (10 points), Due 13 Nov, 11:59pm
Progress Report 1 is an updated and expanded version of your initial proposal. It should include:
* Updated Project topic
* Updated objectives with associated measurable results
* Updated schedule for meeting objectives

Each group should have recieved an evaluation of their initial proposal by 4 November. Using this evaluation, update your topic, objectives, and schedule as necessary, and include it in your progress report.

Further, for any results or objectives that you planned to achieve by the Progress Report 1 due date, demonstrate that you have achieved them by providing images, video, or starter code. If you missed your planned completion date, explain what challenges you faced that prevented you from achieving them.

Include an updated schedule in your progress report that reflects what you believe you can achieve and when for the duration of the final project schedule.

#### How to turn in.
By the due date, place a file `progress_report_1.pdf` in the `project_4` repository of your group members.

### Progress Report 2 (10 points), Due 20 Nov, 11:59pm
Requirements are the same as for progress report 1, except you should address the goals for the time period between progress report 1 and 2.

#### How to turn in.
By the due date, place a file `progress_report_2.pdf` in the `project_4' repository of your group members.

### Final report and implementation (50 points), Due 2 Dec, 11:59pm
Each team will submit a report along with their implementation.

#### Report requirements (35 points)
Your report, in PDF format, should serve as a standalone showcase of your project's achievements as well as a document of your implementation process. Include as many pictures, diagrams, graphs, and quantitative measures as you can to demonstrate your results. Your report should be at least 5 pages, and include at least:

* Overview: enumerate the final objectives of your project and key results that you achieved.
* Background: Give a brief description of the state-of-the-art in the are of your project. If you referred to or used directly previous work (academic papers, open source code, data sets, etc), cite it fully and describe its relevance to your project.
* Methods: Describe the software and other components you created to achieve your objectives. What languages, libraries, hardware, and so forth did you employ? How did you structure your system? What algorithms did you apply or create?
* Results: Demonstrate concretely the objectives you completed with **quantitative** results. For example, if you planned to track faces with 90% accuracy, demonstrate your success rate by measuring it and listing your actual success rate. Include screenshots, graphs, and videos (also checked in with your report) to prove what you achieved.

You'll be evaluated not just on the contents of the report but to the degree to which it demonstrates that you successfully achieved the objectives of your project.

#### Implementation requirements (15 points)
Quality of implementation is very important for successfully software projects. The quality of your implementation will contribute to your final project grade. I expect the following:

* A README.md at your top-level implementation directory describing the structure and organization of your code and support files, and instructions for building and running the code. I understand that some code my require specialized hardware (cell phone, etc) to run.
* All code should be well-documented with comments, readable code, and well-factored structure. I'll evaluate code quality using similar criteria as those applied in code review on other projects.
* All major logic/algorithms must include unit tests verifying their correctness. It's best to write unit tests as you go rather than trying to add them all at the end--you'll find that making your code easy to test will often have a big impact (for the better) on its organization.

#### How to turn in.
By the due date, place the PDF-format report in the file `final_report.pdf` in the `project_4` repository of your group members. Place all code, support files, and documentation in a `code` subdirectory of the `project_4` folder. 

### In-class presentation (10 points), 25 Nov, 2 Dec, or 4 Dec
Each team will give a 10-minute presentation to the entire class summarizing the goals and results of their final project. As many or as few group members may participate in the presentation as you want, but everyone will share the same grade for the presentation.

Presentation time slots are recorded on [`presentations.md`](presentations.md).

Requirements:
* 10 minutes of presentation material (up to 5 minutes of questions and discussion will follow).
* Include a summary of the original and updated final objectives of your project.
* Include a summary of results from objectives you did complete (think **live demos**, pictures, videos). You can spend the bulk of your time on this section.
* Include a summary of key challenges you faced and how you adapted your objectives to meet or work around them.

You are responsible for showing up with presentation materials that will work with the A/V setup in WEL 2.256, which has a projector with VGA video and 3.5mm audio connections, as well as an opaque projector. **I recommend you test out your laptop or other presentation material in WEL 2.256 before your presentation day**. No special keys or access are needed to connect; come any time to test it out.

## Logistics

You will work on this project in self-selected groups of three to five students.

If the group chooses to turn in a project N days late, each individual in the group will lose N of their remaining late days for the semester. If one or more students have no more late days left, they'll lose credit without affecting the other group members' grades.


