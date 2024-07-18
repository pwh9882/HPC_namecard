import streamlit as st
from dotenv import load_dotenv
import os
import io

from PIL import Image
from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import base64
import json

load_dotenv()

# Azure OpenAI 설정
llm = AzureChatOpenAI(
    api_key=os.getenv("API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)


def encode_image(image):
    # 이미지를 RGB 모드로 변환
    rgb_image = image.convert('RGB')

    # 이미지를 바이트 스트림으로 변환
    buffered = io.BytesIO()
    rgb_image.save(buffered, format="JPEG")

    # 바이트 스트림을 base64로 인코딩
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


def extract_info_from_image(image):
    # 이미지를 base64로 인코딩
    base64_image = encode_image(image)

    # Azure OpenAI에 요청 보내기
    messages = [
        SystemMessage(
            content="You are an AI assistant that can analyze business card images and extract relevant information."),
        HumanMessage(content=[
            {
                "type": "text",
                "text": "Please extract the following information from this business card image and provide it in the following JSON format without any markdown formatting: { \"name\": \"\", \"title\": \"\", \"phone\": \"\", \"email\": \"\", \"address\": \"\", \"company\": \"\" }. If any information is not present, please indicate 'NULL' in the respective field."
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}",
                    "detail": "auto",
                }
            }
        ])
    ]

    response = llm.invoke(messages)

    return response.content


def main():
    st.title("Business Card Recognition App")

    uploaded_file = st.file_uploader(
        "Upload a business card image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Business Card",
                 use_column_width=True)

        if st.button("Extract Information"):
            with st.spinner("Extracting information..."):
                extracted_info = extract_info_from_image(image)
                st.subheader("Extracted Information:")
                # st.write(extracted_info)
                decoded_info = json.loads(extracted_info)
                print(decoded_info)
                name = st.text_input(
                    "Name", decoded_info.get("name", "NULL"))
                title = st.text_input(
                    "Title", decoded_info.get("title", "NULL"))
                phone = st.text_input(
                    "Phone", decoded_info.get("phone", "NULL"))
                email = st.text_input(
                    "Email", decoded_info.get("email", "NULL"))
                address = st.text_input(
                    "Address", decoded_info.get("address", "NULL"))
                company = st.text_input(
                    "Company", decoded_info.get("company", "NULL"))

                if st.button("Save Information"):
                    updated_info = {
                        "name": name,
                        "title": title,
                        "phone": phone,
                        "email": email,
                        "address": address,
                        "company": company
                    }
                    st.write("Updated Information:")
                    st.json(updated_info)


if __name__ == "__main__":
    main()
