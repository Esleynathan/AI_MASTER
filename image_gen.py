from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

client = OpenAI(
    api_key=SECRET_KEY,
)

response = client.images.generate(
    model='dall-e-3',
    prompt='',
    size='1024x1024',
    quality='standard',
    n=1,
)

image_url = response.data[0].url
print(image_url)