import webbrowser
import os 
from openai import OpenAI
client = OpenAI()

# Define the text description
text = "artificial intelligence"
  
response = client.images.generate(
  model="dall-e-2",
  prompt=text,
  size="1024x1024",
  quality="standard",
  n=1,
)
 
image_url = response.data[0].url

webbrowser.open(image_url) 

# Display or save the generated image
# print(f"Generated Image URL: {image_url}")
