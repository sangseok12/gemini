import streamlit as st
import random
import google.generativeai as genai
import pandas as pd
from tools import find_recipe_with_ingredients

with open('style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 

st.title(" 🍽️뭐 먹지? ")
st.caption("요리를 추천해 드립니다!!🥦")

# Google API key
if "api_key" not in st.session_state:
  try:
    st.session_state.api_key = st.secrets["GOOGLE_API_KEY"]
  except:
    st.session_state.api_key = ""
    st.write("Your Google API Key is not provided in `.streamlit/secrets.toml`, but you can input one in the sidebar for temporary use.")

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Sidebar for parameters
with st.sidebar:
  # Google API Key
  if not st.session_state.api_key:
    st.header("Google API Key")
    st.session_state.api_key = st.text_input("Google API Key", type="password")
  else:
    genai.configure(api_key=st.session_state.api_key)
  

  
    # ChatCompletion parameters
  model_name='gemini-pro'

  generation_config = {
  "temperature": 0.5,
  "max_output_tokens": 2048,
  "top_k": 10,
  "top_p": 0.35,
   }
  

  # 이미지 추가
  st.image('/workspaces/gemini/.imagie/.imagie/야채사진.png', caption='')

  # 사이드바 꾸미기
  st.markdown("# 🥕우선 냉장고를 여세요!🥕")
  st.write("사용할만한 식재료를 입력하세요.") 
  st.write("재료 2~4가지 입력을 권장합니다.") 
  st.write("ai 챗봇이 메뉴를 추천해드립니다.")

# Display messages in history
for msg in st.session_state.messages:
  if parts := msg.parts:
    with st.chat_message('human' if msg.role == 'user' else 'ai'):
      for p in parts:
        st.write(p.text)

# Chat input
################
# if prompt := st.chat_input("재료를 알려주세요!(예:양파, 피망, 감자, ...)"):
#     with st.chat_message('human', avatar='🙂'):
#         st.write(prompt)

#     # 요리 유형 또는 특징을 바탕으로 요리 추천을 위한 새로운 프롬프트 생성
#     recipe_request = f"이런 조건에 맞는 요리 추천해주세요: {prompt}."

#     # Google AI 모델 설정 및 초기화
#     model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)

#     # Google AI 모델을 사용하여 응답 생성
#     response = model.generate_content(recipe_request, stream=True)

#     # AI 모델의 응답을 표시 (채팅 스타일로)
#     with st.chat_message("ai", avatar='🧑‍🍳'):
#         for chunk in response:
#             st.write(chunk.text)
##################
# if prompt := st.chat_input("재료를 알려주세요!"):
#     with st.chat_message('human', avatar='🙂'):
#         st.write(prompt)

#     user_ingredients = prompt.split(", ")  # 사용자 입력을 쉼표로 분리
#     recommended_recipe = find_recipe_with_ingredients(user_ingredients)
    
#     # 추천된 요리의 재료 목록을 출력
#     with st.chat_message("ai", avatar='🧑‍🍳'):
#         st.write(recommended_recipe)
###################################
# if prompt := st.chat_input("재료를 알려주세요!(예:양파, 피망, 감자, ...)"):
#     with st.chat_message('human', avatar='🙂'):
#         st.write(prompt)

#     # 입력된 재료를 분리하고 처리
#     user_ingredients = prompt.split(", ")

#     recommended_recipe = find_recipe_with_ingredients(user_ingredients)

#     # 요리 추천을 위한 새로운 프롬프트 생성
#     recipe_request = f"음식 이름과 재료는 그대로 표출해줘!:{recommended_recipe}"

#     # AI 모델 설정 및 초기화 (예: Google AI 모델)
#     model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)

#     # AI 모델을 사용하여 요리 추천 응답 생성
#     response = model.generate_content(recipe_request, stream=True)

#     # AI 모델의 응답을 채팅 스타일로 표시
#     with st.chat_message("ai", avatar='🧑‍🍳'):
#         for chunk in response:
#             st.write(chunk.text)
###################################
if prompt := st.chat_input("재료를 알려주세요!(예:양파, 피망, 감자, ...)"):
    with st.chat_message('human', avatar='🙂'):
        st.write(prompt)

    # 입력된 재료를 분리하고 처리
    user_ingredients = prompt.split(", ")

    recommended_recipe = find_recipe_with_ingredients(user_ingredients)

    # 요리 추천을 위한 새로운 프롬프트 생성
    recipe_request = f"음식 이름과 재료를 표출해 주고 음식 레시피를 추천해주고 음식 재료를 표출 할 때에는 요리 재료들을 줄바꿈 없이 한줄에 표현해주고 모든 텍스트는 일정한 크기로 해주고 친절하게 말하는 듯이 해줘.:{recommended_recipe}"

    # AI 모델 설정 및 초기화 (예: Google AI 모델)
    model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)

    # AI 모델을 사용하여 요리 추천 응답 생성
    response = model.generate_content(recipe_request, stream=True)

    # AI 모델의 응답을 채팅 스타일로 표시
    with st.chat_message("ai", avatar='🧑‍🍳'):
        for chunk in response:
            st.write(chunk.text)
###################################
    #Google AI 모델을 사용하여 채팅 응답 생성
# model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)
# chat = model.start_chat(history=st.session_state.messages)
# response = chat.send_message(prompt, stream=True)

#     #AI 모델의 스트림 응답을 표시
# with st.chat_message("ai", avatar='🧑‍🍳'):
#        placeholder = st.empty()
#        text = ''
# for chunk in response:
#            text += chunk.text
#            placeholder.write(text + "▌")
# placeholder.write(text)

    # 채팅 히스토리 삭제
st.session_state.messages = []   