from pathlib import Path
from PIL import Image
import streamlit as st

from sub_app import generator, reader


img_paths = Path('sub_app').joinpath('imgs').glob('*.*g')

if img_paths:
    for img_path in img_paths:
        img_path.unlink()

favicon_img_path = Path('favicon.png')

st.set_page_config(
    page_title="QRcode App",
    page_icon=Image.open(favicon_img_path),
    layout="centered",
    menu_items={
         'About': """
         # QRコード生成/読み込みアプリ
         このアプリはQRコードを生成/読み込みするアプリです。
         """
    }
)

# サイドバーで選択するアプリページの設定
PAGES = {
    "GeneratorApp": generator,
    "ReaderApp": reader,
}

selection = st.sidebar.radio(
    "select app",
    tuple(PAGES.keys()),
)

page = PAGES[selection]

# sub_appディレクトリ内の各pythonファイルのapp関数を実行
page.app()
