import qrcode
# pillow implicity imported
eggdropsandwich_link = 'https://www.youtube.com/watch?v=ZsMkK98iZHg'

qr = qrcode.QRCode(version=1, box_size=5, border=5)
# version: parameter controls size of QR code
# box_size: controls how man pizels each box of QR code is
# border: congtrols how many boxes thick border should be

qr.add_data(eggdropsandwich_link)
qr.make()

qr.make_image()

img = qr.make_image(fill_color='green', back_color='yellow')

img.save('youtube_qr.png')

# tutorial https://www.codedex.io/projects/generate-a-qr-code-with-python
