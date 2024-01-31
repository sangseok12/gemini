import pandas as pd

# 파일 경로
file_path = 'Cooking.csv'

# 다른 인코딩 옵션을 사용하여 파일을 불러오기
try:
    CK = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    CK = pd.read_csv(file_path, encoding='euc-kr')

# 각 행의 'INQ_CNT', 'RCMM_CNT', 'SRAP_CNT' 값을 더한 후, 평균을 계산하여 'NEW_COL' 열로 추가
CK['NEW_COL'] = CK[['INQ_CNT', 'RCMM_CNT', 'SRAP_CNT']].sum(axis=1) / 3

#선택
selected_CK = CK.iloc[:, [2, 13]]

# 결측치가 있는 행 제거
CK_cl = selected_CK.dropna()

# 터미널에서 실행해야함!!!!!! pip install -q -U google-generativeai

import google.generativeai as genai

import textwrap
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  
model = genai.GenerativeModel('gemini-pro')

prompt = """문장에서 식재료만 추출해줘.

Input: 냉장고에 어묵이 있고, 당근도 있고, 토마토도 있고, 사과도 있고, 오이도 있어.
Output: 어묵, 당근, 토마토, 사과, 오이

Input: 냉장고에 마우스랑 노트북이랑 연필이랑 감자가 있어.
Output: 재료가 많아서 요리를 찾을 수 없거나 부족해서 제안할 만한 음식이 없어요.

Input: 머스타드랑 후추랑 계란이랑 마늘이 집에 있어.
Output: 머스타드, 후추, 계란, 마늘

Input: {}
Output:
"""

response = model.generate_content(prompt.format({"지금 바나나, 고구마, 감자, 김치, 식용유, 후추, 김, 생수, 커피, 초콜릿, 마우스, 가지, 양파, 사과가 냉장고에 있어."}))
to_markdown(response.text)

def cook(ingredients):
    """
    주어진 재료를 포함하는 요리를 찾아 반환합니다.
    :param ingredients: 요리에 사용될 재료 목록
    :return: 해당 재료를 포함하는 요리 목록
    """
    # 해당 재료를 하나라도 포함하는 요리를 찾습니다.
    recipes = []
    for index, row in CK_cl.iterrows():
        recipe_ingredients = row['CKG_MTRL_CN'].lower()
        if any(ingredient in recipe_ingredients for ingredient in ingredients):
            recipes.append(row['CKG_NM'])
    return recipes
print(response.text.split(', '))