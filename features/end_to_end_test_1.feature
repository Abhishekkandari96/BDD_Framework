

Feature: Automate tasks on the Indee platform

  Scenario: End to End Test Case In BDD Framework Given For Assignment
    Given I am on the Indee login page
    When I log in using the provided PIN
    Given Iam at homepage
    Given I navigate to the Test Automation Project
    Then I switch to the Details tab
    Then I return to the Videos tab
    Then I play the video
    Given I am in videoplayer
    Then  Pause video
    Then I replay the video using the Continue Watching button
    Then I adjust the volume to 50 percent
    Then I change the video resolution to 480p and back to 720p
    Then exit the videoplayer
    Given Iam at homepage
    Then I log out of the platform
