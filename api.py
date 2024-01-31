import streamlit as st
import requests


google_api_key="GOOGLE_API_KEY"

# API 요청 보내기
headers = {
    "Authorization": f"Bearer {google_api_key}"
}
response = requests.get( headers=headers)

# API 응답 처리
if response.status_code == 200:
    data = response.json()
    # 응답 데이터를 처리하는 코드 작성
else:
    st.error("API 요청 중 오류가 발생했습니다.")
    
def convert_to_casual_language(recipe_text):
    # 여기에 텍스트를 casual한 언어로 변환하는 코드를 작성합니다.
    casual_text = recipe_text.replace("양념장을 만듭니다.", "양념을 만들어 뿌려요!")
    casual_text = casual_text.replace("오븐에 30분 동안 굽니다.", "오븐에 30분 정도 구워주세요!")
    return casual_text