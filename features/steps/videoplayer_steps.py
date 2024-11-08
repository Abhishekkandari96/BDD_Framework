import time
from behave import then , Given
from pages.video_player import VideoPlayer


@Given(u"I am in videoplayer")
def initialise_videoplayer(context):
    # initialise videoplayer screen
    context.video_player = VideoPlayer(context.driver)

@then(u"Pause video")
def pause_the_video(context):
    # Pause thr video
    context.video_player.pause_video()

@then(u"I replay the video using the Continue Watching button")
def step_replay_video(context):
    # Replay the Video using the 'Continue Watching' button:
    context.video_player.continue_watching()

@then(u"I adjust the volume to 50 percent")
def step_adjust_volume(context):
    # Adjust Volume:
    context.video_player.set_volume(5)

@then(u"I change the video resolution to 480p and back to 720p")
def step_change_resolution(context):
    # Change Video Resolution:
    context.video_player.change_resolution("480p")
    # to handle speed
    time.sleep(2)
    context.video_player.change_resolution("720p")

@then(u"exit the videoplayer")
def step_exit_project(context):
    # existing from video player
    context.video_player.exit_video()

