from pathlib import Path
# from PIL import Image
import qrcode
import streamlit as st


FILE_NAME = 'qrcode.png'
qrcode_img_path = Path('imgs').joinpath(FILE_NAME)

error_correction_dict = {
    "レベルL（約7%）": qrcode.constants.ERROR_CORRECT_L,
    "レベルM（約15%, デフォルト）": qrcode.constants.ERROR_CORRECT_M,
    "レベルQ（約25%）": qrcode.constants.ERROR_CORRECT_Q,
    "レベルH（約30%）": qrcode.constants.ERROR_CORRECT_Q
}

st.title('QRコード生成アプリ')

text_data = st.text_input('QRコードを生成したいURLなどの文字列')

setting = st.radio(
    "オプション",
    key="setting",
    index=0,
    options=[
        "簡易設定",
        "詳細設定"
    ]
)

if setting == "詳細設定":
    version = st.selectbox(
        "生成されるQRコードのバージョン",
        (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "40",
        )
    )

    error_correction = st.radio(
            "誤り訂正レベル",
            key="error_correction",
            index=1,
            options=[
                "レベルL（約7%）",
                "レベルM（約15%, デフォルト）",
                "レベルQ（約25%）",
                "レベルH（約30%）"
            ],
    )

    box_size = st.text_input('セルのサイズ（最小セルサイズ:10, デフォルト）', value="10")

    border = st.text_input('余白の幅（最小幅:4, デフォルト）', value="4")

    fill_color = st.color_picker(label='fill_color:')
    st.write('selected: ', fill_color)

    back_color = st.color_picker(label='back_color:', value="#ffffff")
    st.write('selected: ', back_color)

if st.button('QRコード生成'):
    img = qrcode.make()
    if setting == "詳細設定":
        qr = qrcode.QRCode(
            version=int(version),
            error_correction=error_correction_dict.get(error_correction),
            box_size=int(box_size),
            border=int(border)
        )
        qr.add_data(text_data)
        qr.make()
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
    else:
        img = qrcode.make(text_data)
    img.save(qrcode_img_path)
    st.image(img.get_image())

    with open(qrcode_img_path, 'rb') as file:
        btn = st.download_button(
                label='Download image',
                data=file,
                file_name=FILE_NAME,
                mime='image/png'
              )
