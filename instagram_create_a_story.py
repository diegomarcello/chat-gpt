from instabot import Bot

# Initialize the bot with your Instagram credentials
bot = Bot()
bot.login(username='your_username', password='your_password')

# Load the image you want to post as a story
image_path = 'path/to/image.jpg'
bot.upload_story_photo(image_path)

# Load the video you want to post as a story
video_path = 'path/to/video.mp4'
bot.upload_story_video(video_path)
