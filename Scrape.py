import requests
from bs4 import BeautifulSoup
import os

# Set the URL of the website you want to scrape
url = "https://www.pexels.com/search/car/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all image tags on the page
img_tags = soup.find_all('img')

# Create a directory to save the images
if not os.path.exists('car_images'):
    os.makedirs('car_images')

# Download each image and save it to the directory
for img in img_tags:
    try:
        img_url = img['src']
        if 'http' not in img_url:
            # If the image URL is relative, add the base URL of the website
            img_url = f"{url}/{img_url}"
        response = requests.get(img_url)
        img_file = open(f"car_images/{img_url.split('/')[-1]}", 'wb')
        img_file.write(response.content)
        img_file.close()
    except:
        pass
