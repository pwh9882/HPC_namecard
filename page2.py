import streamlit as st
from PIL import Image
import io
import base64
from db import init_db, save_business_card, get_all_business_cards


def decode_image(base64_image):
    # base64 문자열을 바이트로 디코딩
    image_data = base64.b64decode(base64_image)
    # 바이트 데이터를 이미지로 변환
    image = Image.open(io.BytesIO(image_data))
    return image


def main():
    st.title("Business Card History")

    # Add a section to display all saved business cards
    st.subheader("Saved Business Cards")
    cards = get_all_business_cards()

    for card in cards:
        st.write(f"Name: {card[1]}, Title: {card[2]}, Company: {card[6]}")
        st.write(f"Phone: {card[3]}, Email: {card[4]}")
        st.write(f"Address: {card[5]}")

        # 복구한 이미지 표시
        image = decode_image(card[7])
        st.image(
            image,
            caption=f"{card[1]}'s Business Card",
            use_column_width=True
        )

        st.write("---")


if __name__ == "__main__":
    main()
