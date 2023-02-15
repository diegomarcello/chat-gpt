import instaloader
import random

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Define the hashtag to search for
hashtag = 'trending'

# Create a list of the top 100 posts for the given hashtag
posts = [post for post in L.get_hashtag_posts(hashtag)][:100]

# Select a random post from the list of top posts
post = random.choice(posts)

# Create the text for the Instagram post using the caption of the selected post
text = post.caption_hashtags

# Post the text to Instagram using the Instagram API
# Note: this requires an Instagram Business account and API access
# See the Instagram Graph API documentation for more information
# https://developers.facebook.com/docs/instagram-api
api.post_text(text)
