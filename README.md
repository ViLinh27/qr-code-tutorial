# qr-code-tutorial
 codedex mini project tutorial on how to make qr code in python

## Credits

### Andrew from hackernoon: https://hackernoon.com/how-to-instantly-create-a-front-end-for-your-python-program

Introduces the streamlit library as a useful front-end to add to python projects

### Turtle Code on Youtube @turtlecode here: https://www.youtube.com/@turtlecode

Had a useful tutorial to compare to Jerry Zhu's basic arcade maker tutorial

### Jerry Zhu's codedex.io tutorial here: https://www.codedex.io/projects/generate-a-qr-code-with-python

Where I first found out about the qrcode library of python and how it was useful for this kind of mini project

## Issues

Most of my issues have been typos. It came with learning the streamlit library and the syntax. Plus some reviewing of python and my usual weakness with typos.

### Image upload issue
A new issue that came up was when I was trying to incorporate a customization feature that would allow users to upload images to add to their QR code (if they chose to). I'm using Rod Trent's code as reference. But the try catch block always fails and throws an exception.

Some problems I've had include the fact that I'm trying to use Image.open() without the import, so I'm missing that. Another thing is I didn't spell LANCZOS right when referencing Trent's code. I put in a 0 where an O should have been. The LANCZOS is an algorithm  that the library uses for image resizing to my understanding. There was also a transparency conflict with my converting to Rgb (the image uploaded) . I thought that would have ben fine but the transparency masking needs RGBA to work.

When using mask = logo when pasting with the transparency mask, python looks at the alpha channel of the logo. So if that alpha is 0, then it'll blend well with the QR code. RGB makes the image lose it's transparency and I didn't want a solid box around the logo image.
