from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("Inter_24pt-Bold.ttf", 50)
font2 = ImageFont.truetype("Inter_18pt-SemiBold.ttf", 40)


def generate_image(users, end, wins, title):
    image = Image.open("image.jpg")
    drawer = ImageDraw.Draw(image)
    drawer.text(
        (450, 200),
        title,
        font=font2,
        fill='black',
        anchor='mm'
    )
    drawer.text(
        (200, 345),
        str(users),
        font=font,
        fill='black',
        anchor='mm'
    )
    drawer.text(
        (450, 345),
        str(wins),
        font=font,
        fill='black',
        anchor='mm'
    )
    drawer.text(
        (700, 345),
        str(end),
        font=font,
        fill='black',
        anchor='mm'
    )
    drawer.text(
        (700, 345),
        str(end),
        font=font,
        fill='black',
        anchor='mm'
    )
    return image

