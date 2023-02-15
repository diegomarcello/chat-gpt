from InstagramAPI import InstagramAPI

# Initialize InstagramAPI with your Instagram credentials
username = 'your_username'
password = 'your_password'
api = InstagramAPI(username, password)
api.login()

# Upload an image to Instagram and get the media ID
image_path = 'path/to/image.jpg'
caption = 'This is my caption'
api.uploadPhoto(image_path, caption=caption)
media_id = api.LastJson['media']['id']

# Add a comment to the post
comment = 'This is my comment'
api.comment(media_id, comment)
