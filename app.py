import requests
from bs4 import BeautifulSoup
import os
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Set the URL of the website you want to scrape
    url = "https://www.pexels.com/search/car/"
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Parse the HTML content of the website using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all image tags on the page
    img_tags = soup.find_all('img')
    
    # Create a list of image URLs
    image_urls = []
    for img in img_tags:
        try:
            img_url = img['src']
            if 'http' not in img_url:
                # If the image URL is relative, add the base URL of the website
                img_url = f"{url}/{img_url}"
            image_urls.append(img_url)
        except:
            pass
    
    # Select a random image URL from the list
    random_image_url = random.choice(image_urls)
    
    # Render the HTML template and pass in the random image URL
    return render_template('index.html', image_url=random_image_url)

if __name__ == '__main__':
    app.run()
