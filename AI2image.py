# Generate image from text by OpenAI's DALL-E Image API and then open it in a web browser
# By TechMakerAI on YouTube 
# 
import webbrowser
import os 

from openai import OpenAI
client = OpenAI()

# A text description of the desired image(s). 
# The maximum length is 1000 characters for dall-e-2 
# and 4000 characters for dall-e-3.
text = "artificial intelligence "
  
response = client.images.generate(
  model = "dall-e-2",
  prompt = text,
  
  # Must be one of 256x256, 512x512, or 1024x1024 for dall-e-2. 
  # Must be one of 1024x1024, 1792x1024, or 1024x1792 for dall-e-3 models.
  size = "1024x1024", 
  quality = "standard", 
  
  # number of images. Must be between 1 and 10. 
  # For dall-e-3, only n=1 is supported. 
  n=1  
)
 
image_url = response.data[0].url

# Open the URL in the default web browser
webbrowser.open(image_url) 
