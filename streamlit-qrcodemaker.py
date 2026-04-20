import qrcode

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

import PIL.ImageColor as ImageColor
from PIL import Image
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="My QR Code Maker", page_icon=":)" , layout="centered")

#page title
st.title(":) My QR Code Maker")

#user input
st.write(" Create your own QR Code here. Enter a text, link or data below.")
userlink  = st.text_input("Enter the content for your qr code here: ")

#customization options
st.subheader('Customizations');
col1,col2 = st.columns(2)

with col1:
    fill_color = st.color_picker("Qr Color", "#000000")
with col2:
    back_color = st.color_picker("Background Color", "#FFFFFF")

rgb_fill = ImageColor.getcolor(fill_color, "RGB")
rgb_back = ImageColor.getcolor(back_color, "RGB")

#size of qr code
box_size = st.slider("Size", min_value = 5, max_value = 20, value = 10, key="my_slider")

#rounded corners
round_enabled = st.toggle("Do you want rounded corners? Toggle On, if yes")

#image added to qr code?
uploaded_img= st.file_uploader(
    "Upload logo( PNG/JPG, square recommended, transparent PNG ideal)",
    type=["png","jpg","jpeg"]
    )

#file name
myfilename  = st.text_input("Enter a name for your qr code file if you want to download it later: ")

#button to make qrcode
if st.button("Generate QR Code"):
    if userlink.strip() =="":
        st.warning(" Please enter some content :(")
    else:#if there is valid data to turn into qr code
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = box_size,
            border = 4,
            )
        qr.add_data(userlink)
        qr.make(fit=True)

        if round_enabled:#rounded corners turned on
            img = qr.make_image(
                image_factory = StyledPilImage,
                module_drawer = RoundedModuleDrawer(),
                color_mask = SolidFillColorMask(
                    front_color=rgb_fill,
                    back_color = rgb_back
                )
            )
        else:
            img = qr.make_image(fill_color = fill_color, back_color = back_color)

        img = img.convert("RGB")

        #logo handling
        if uploaded_img is not None:
            try:
                logo=Image.open(uploaded_img).convert("RGBA")
                qrw, qrh= img.size

                #logo size
                logo_size = int(qrw * 0.25)
                logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

                #center the logo
                pos = ((qrw- logo_size) // 2, (qrh- logo_size) //2)

                #paste img with transprency mask
                img.paste(logo,pos, mask=logo)
                
            except Exception as e:
                st.warning(f"Logo processing failed :( ({e}) - showing QR without logo.")

        st.image(img,caption="Your QR Code is here", use_container_width = True)

        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label=" Download qr code here",
            data = byte_im,
            file_name= myfilename,
            mime="image/png"
            )

#footer
st.markdown("---")
st.markdown("Made by Linh Nguyen, with care using [Streamlit](https://streamlit.io/)")
st.markdown("---")
st.markdown("Credits:")
st.markdown("Andrew from hackernoon: https://hackernoon.com/how-to-instantly-create-a-front-end-for-your-python-program")
st.markdown("Turtle Code on Youtube @turtlecode here: https://www.youtube.com/@turtlecode")
st.markdown("Jerry Zhu's codedex.io tutorial here: https://www.codedex.io/projects/generate-a-qr-code-with-python")

# streamlit qrcode tutorial https://youtu.be/ccbzvKcoaps?si=7uIdfRjsnZz6F6LC

#stylings
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&display=swap');
        *{
            font-family:"Pixelify Sans", sans-serif;
            font-optical-sizing: auto;
            font-weight: <weight>;
            font-style: normal;
            color: #544775;
        }
        .stApp{
            color: #544775;
            background-color:#dbc3e1;
        }
        
        .stButton button,
        .stDownloadButton button,
        {
            color: #544775;
            background-color:#dbc3e1;
        }
        .stButton button:hover,
        .stTextInput input:hover{
            background-color:#e092ac;
        }
        
        .stTextInput input
        {
            color: #544775;
            background-color:#c7a6cf;
        }
        div[data-testid="stSlider"][key="my_slider"]
        {
            color:#ab47bc;
            /*background:#ab47bc;*/
            /*background-color:#ab47bc;*/
        }
        div[data-testid="stSlider] > div > div > div > div {
            background: #ab47bc
        }
    </style>

""",unsafe_allow_html=True)
