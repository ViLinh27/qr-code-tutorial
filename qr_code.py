import qrcode
# pillow implicity imported
print('Enter a website link to make into a qr code: ')

#eggdropsandwich_link = 'https://www.youtube.com/watch?v=ZsMkK98iZHg'
userlink = input()


qr = qrcode.QRCode(version=1, box_size=5, border=5)
# version: parameter controls size of QR code
# box_size: controls how man pizels each box of QR code is
# border: congtrols how many boxes thick border should be

qr.add_data(userlink)
qr.make()

qr.make_image()

print('Enter a fill color for the main qr code: ')
userfill = input()
print('Enter a background color forthe qr code (make sure the color constrasts with fill color): ')
userback = input()

img = qr.make_image(fill_color=userfill, back_color=userback)


print('Enter a name for your qr code file: ')
userfilename = input()

img.save(f'{userfilename}.png')
print('Your qr code has been made')

# tutorial https://www.codedex.io/projects/generate-a-qr-code-with-python
