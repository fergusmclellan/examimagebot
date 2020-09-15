import os
from webexteamsbot import TeamsBot
from PIL import Image, ImageDraw, ImageFont

# Retrieve required details from environment variables
bot_email = os.getenv("TEAMS_BOT_EMAIL")
teams_token = os.getenv("TEAMS_BOT_TOKEN")
bot_url = os.getenv("TEAMS_BOT_URL")
bot_app_name = os.getenv("TEAMS_BOT_APP_NAME")

# Create a Bot Object
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
)


# A simple command that returns a basic string that will be sent as a reply
def create_image(incoming_msg):
    """
    Function to create an image based on .
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    image_filename = 'output.png'
    drawing = ImageDraw.Draw(img)
    drawing.rectangle([(0,0), (200, 200)], fill=None, outline='black',width=2)
    img.save(image_filename)
    return "image saved as" + image_filename


# Add new commands to the box.
bot.add_command("/createimage", "help for create image", create_image)


if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
