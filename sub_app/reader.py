import pyzbar.pyzbar
from PIL import Image
import streamlit as st


def app():
    st.title('QRコード読み込みアプリ')

    uploaded_file = st.file_uploader(
        'QRコードのイメージファイルを選択してください',
        type=['png', 'jpg']
    )

    if uploaded_file is not None:
        qrcode = pyzbar.pyzbar.decode(Image.open(uploaded_file))
        if qrcode:
            read_text = qrcode[0].data.decode('utf-8')
            md = f'''
            ##### {read_text}
            '''
            left_col, center_col, right_col = st.columns(3)
            left_col.write('read_data:')
            center_col.markdown(md)
            right_col.write('')
        else:
            st.write(
                '<font color="Red">※読み込みエラー！QRコード画像を確認してください</font>',
                unsafe_allow_html=True
            )
