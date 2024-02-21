# Generating an Image from Text with OpenAI's DALL-E API
This Python program will generate an image based on the text input with OpenAI's Dall-E Image API. Then, in the first example, it will open the image with the default web browser. In the second code, it will open the file with the Firefox web browser. Finally, in the last example, it will save the image to a file on the hard drive. 

Please follow the YouTube video to learn more about this code:
https://youtu.be/XYtFgmF39uc

Before you can run this code on your computer, you will need to install the following packages: 

```console
pip install openai   
```
If you have Python 3.12 or newer, also install the "setuptools" package,    

```console
pip install setuptools
```
Then, you must set the API key from OpenAI as a system environment variable. If you rather want to use your API key in the Python program, then add it to the definition of the variable "client" as, 
```python
client = OpenAI(api_key="this is your API key")
```

