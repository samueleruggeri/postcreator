import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Unsplash API configuration
UNSPLASH_API_KEY = 'YOUR_UNSPLASH_API_KEY'
UNSPLASH_API_URL = 'https://api.unsplash.com/photos/random'

# Function to fetch a random image from Unsplash
def fetch_random_image():
    headers = {
        'Authorization': f'Client-ID {UNSPLASH_API_KEY}'
    }
    params = {
        'query': 'nature'  # Change the query to suit your needs
    }
    response = requests.get(UNSPLASH_API_URL, headers=headers, params=params)
    data = response.json()
    image_url = data['urls']['regular']
    image_response = requests.get(image_url)
    return Image.open(BytesIO(image_response.content))

# Function to add a quote to the image
def add_quote_to_image(image, quote):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Arial.ttf', 30)  # Change the font and size as needed
    text_color = (255, 255, 255)  # White color for the text
    text_position = (50, 50)  # Change the position of the text as needed
    draw.text(text_position, quote, font=font, fill=text_color)
    return image

# Main function
def create_social_media_content():
    # Fetch a random image from Unsplash
    image = fetch_random_image()

    # Generate a quote (replace this with your own logic to generate quotes)
    quote = "This is a sample quote."

    # Add the quote to the image
    image_with_quote = add_quote_to_image(image, quote)

    # Save the final image
    image_with_quote.save('social_media_content.jpg')
    print("Social media content created successfully.")

# Run the main function
create_social_media_content()