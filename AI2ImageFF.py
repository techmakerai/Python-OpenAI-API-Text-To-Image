# Generate an image from the text by OpenAI's DALL-E Image API and then open it with Firefox
# By TechMakerAI on YouTube 
# 
import webbrowser
import os 

from openai import OpenAI

# I added my API key as a system environment variable. 
client = OpenAI()
# If you rather want to use your API key in this program, then change the above line to, 
# client = OpenAI(api_key="this is your API key")

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

# Display or save the generated image
# print(f"Generated Image URL: {image_url}")

# Specify the path to the Firefox executable
ff_path = os.path.join( "C:\Program Files\Mozilla Firefox", "firefox.exe")  # Adjust this path based on your Firefox installation location

# Use webbrowser.get() to open the URL in Firefox
webbrowser.register("ff", None, webbrowser.BackgroundBrowser(ff_path))

# Open the URL with Firefox web browser
webbrowser.get("ff").open_new_tab(image_url)


 
