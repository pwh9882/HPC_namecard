import streamlit as st
from PIL import Image
import io
import base64
from db import init_db, save_business_card, get_all_business_cards, update_business_card, delete_business_card


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

    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False
    if 'edit_card_id' not in st.session_state:
        st.session_state.edit_card_id = None

    for card in cards:
        col1, col2 = st.columns([1, 2])

        with col1:
            # 복구한 이미지 표시
            image = decode_image(card[7])
            st.image(image, caption=f"{
                     card[1]}'s Business Card", use_column_width=True)

        with col2:
            if st.session_state.edit_mode and st.session_state.edit_card_id == card[0]:
                st.subheader("Edit Business Card")

                name = st.text_input("Name", card[1], key=f"name_{card[0]}")
                title = st.text_input("Title", card[2], key=f"title_{card[0]}")
                phone = st.text_input("Phone", card[3], key=f"phone_{card[0]}")
                email = st.text_input("Email", card[4], key=f"email_{card[0]}")
                address = st.text_input(
                    "Address", card[5], key=f"address_{card[0]}")
                company = st.text_input(
                    "Company", card[6], key=f"company_{card[0]}")

                col3, col4 = st.columns([1, 1])
                with col3:
                    if st.button("Save Changes", key=f"save_{card[0]}"):
                        info = {
                            "name": name,
                            "title": title,
                            "phone": phone,
                            "email": email,
                            "address": address,
                            "company": company,
                            "image": card[7]  # 기존 이미지 사용
                        }
                        update_business_card(card[0], info)
                        st.session_state.edit_mode = False
                        st.session_state.edit_card_id = None
                        st.rerun()
                with col4:
                    if st.button("Cancel", key=f"cancel_{card[0]}"):
                        st.session_state.edit_mode = False
                        st.session_state.edit_card_id = None
                        st.rerun()
            else:
                st.write(f"**Name:** {card[1]}")
                st.write(f"**Title:** {card[2]}")
                st.write(f"**Phone:** {card[3]}")
                st.write(f"**Email:** {card[4]}")
                st.write(f"**Address:** {card[5]}")
                st.write(f"**Company:** {card[6]}")

                col3, col4 = st.columns([1, 1])
                with col3:
                    if st.button("Edit", key=f"edit_{card[0]}"):
                        st.session_state.edit_card = card
                        st.session_state.edit_mode = True
                        st.session_state.edit_card_id = card[0]
                        st.rerun()
                with col4:
                    if st.button("Delete", key=f"delete_{card[0]}"):
                        delete_business_card(card[0])
                        st.rerun()

        st.write("---")


if __name__ == "__main__":
    main()
