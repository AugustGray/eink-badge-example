# E-Ink Digital Badge

A minimalist, always-on digital badge powered by a Raspberry Pi Zero W and a Waveshare 2.13" V4 e-ink diplay.

This python project badge can display contact info like your name, e-mail, phone, and/or show a QR code for quick sharing of links.

---

## Features
- Display any custom text
- Generate and display **QR codes** (Link, contact card, etc.)
- Display images or logos (png, svg) - *Planned*
- Low power, always-on e-ink display
- Support rotation for flexible mounting
- fully customizable (fonts, layouts, etc.)

---

## Requirements
### Hardware Requirements
- **Raspberry Pi Zero W** (Tested) - other Pi models may work
- **Waveshare 2.13" V4** e-ink display (Tested) - other models may work
- MicroSD card (8GB+ recommended)
- USB power source
- *(Optional)* 3D-printed and or laser-cut enclosure


### Sofware Requirements
- **Python 3.9+**
- [Pillow](https://pillow.readthedocs.io/en/stable/)- Image processing
- [Qrcode](https://pypi.org/project/qrcode/)- QR code generation
- Waveshare e-ink display Python driver ([repo link](https://github.com/waveshare/e-Paper))
- RPi.GPIO or compatible GPIO library
- Raspberry Pi OS Lite (recommended for performance & low power)

---

## Installation
1. **Enable SPI on Raspberry Pi**
``` bash
sudo raspi-config
# Interface Options --> SPI --> Enable
```

2. Clone this repository
``` bash
git clone https://github.com/AugustGray/eink-badge-example.git
```

3. Install dependencies
	- Python3-Pip
	- Python3-Pil
	- Python3-numpy
	- Pip qrcode

Install Pip, Pil and Numpy
``` bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-pil python3-numpy
```

Install qrcode
```bash
pip3 install qrcode
```