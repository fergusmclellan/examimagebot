import os
from webexteamsbot import TeamsBot
from PIL import Image, ImageDraw, ImageFont

FONT_HEIGHT_SIZE_PX = 15
FONT_WIDTH_SIZE_PX = 9
LINE_SPACING_PX = 2
BORDER_PADDING_PX = 6
MAX_WIDTH_PX = 950
MAX_HEIGHT_PX = 600
IMAGE_FONT = ImageFont.truetype('cour.ttf', FONT_HEIGHT_SIZE_PX)

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
    img = Image.new('RGB', (220, 220), color = ('white'))
    drawing = ImageDraw.Draw(img)
    drawing.text((BORDER_PADDING_PX, 10), incoming_msg.text, font=IMAGE_FONT, fill=('black'))
    drawing.rectangle([(0,0), (200, 200)], fill=None, outline='black',width=2)
    img.save('/app/' + image_filename)
    return "image saved as: " + image_filename


# Add new commands to the box.
bot.add_command("/createimage", "help for create image", create_image)


if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
