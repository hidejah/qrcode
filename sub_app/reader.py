from pyzbar.pyzbar import decode
from PIL import Image
import streamlit as st


def app():
    st.title('QRコード読み込みアプリ')

    uploaded_file = st.file_uploader(
        'QRコードのイメージファイルを選択してください',
        type=['png', 'jpg']
    )

    if uploaded_file is not None:
        qrcode = decode(Image.open(uploaded_file))
        if qrcode:
            read_text = qrcode[0].data.decode('utf-8')
            read_text = qrcode[0].data.decode('utf-8')
            st.code('< read_data >{}{}'.format('\n', read_text))
        else:
            st.write(
                '<font color="Red">※読み込みエラー！QRコード画像を確認してください</font>',
                unsafe_allow_html=True
            )
