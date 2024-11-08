Utilizing the Page Object Model (POM) and BDD framework and organized as follows:
Python Selenium Script:
The code is structured with POM and BDD frameworks for a modular and maintainable approach. The main automation script is located in the features/end_to_end_test_1.feature file. This file contains the end-to-end flow as specified in the assignment.
The project includes a well-organized directory structure:
•	features/steps: Contains step definitions for different parts of the application (e.g., login_steps.py, videoplayer_steps.py).
•	pages: Contains Page Object classes (e.g., home_page.py, login_page.py, video_player.py), each encapsulating UI elements and actions for its respective page, following the POM structure.
•	data/data.json: Holds test data, such as credentials and URLs, to keep configuration separate from code.
I have used Allure as the reporting tool.



