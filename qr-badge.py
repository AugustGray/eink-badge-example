from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont
import qrcode
import time

# Init display
epd = epd2in13_V4.EPD()
epd.init()
epd.Clear(0xFF)

# Create blank image: 122x250
image = Image.new('1', (epd.height, epd.width), 255)
draw = ImageDraw.Draw(image)

# ==== QR Code (Left half) ====
qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=4,
	border=1,
)
qr.add_data("https://github.com/AugustGray/eink-badge-example")
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# Resize and paste
qr_img = qr_img.resize((100, 100))
image.paste(qr_img, (10, 10)) # x = 0 to 60

# ==== Separator ====
line_x = 124
draw.line([(line_x, 0), (line_x, epd.width)], fill=0, width=2)

# ==== Text (Right half) ====
font_h1 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
font_h2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
font_text = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 10)

# Position text right half (x = 65-122)
text_x = line_x + 12
draw.text((text_x, 20), "Name", font=font_h1, fill=0)
draw.text((text_x, 40), "Lastname", font=font_h1, fill=0)
draw.text((text_x, 60), "@Github", font=font_h2, fill=0)
draw.text((text_x, 78), "contact-info", font=font_text, fill=0)

# ====  Rotate display ====
image = image.rotate(180)

# ==== Display ====
epd.display(epd.getbuffer(image))
epd.sleep()
