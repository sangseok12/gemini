import pandas as pd
import random
import google.generativeai as genai

file_path = '/workspaces/gemini/Cooking.csv'
cooking_data = pd.read_csv(file_path)
cooking_data.head()



# 데이터 불러오기 및 전처리
def load_data():
    file_path = '/workspaces/gemini/Cooking.csv'
    try:
        CK = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        CK = pd.read_csv(file_path, encoding='euc-kr')

    # 열의 합을 이용해 새로운 열 생성
    CK['NEW_COL'] = CK[['INQ_CNT', 'RCMM_CNT', 'SRAP_CNT']].sum(axis=1) / 3

    # 필요한 열만 선택
    selected_CK = CK.iloc[:, [2, 13]]

    # 결측값이 있는 행 제거
    CK_cl = selected_CK.dropna()

    # 'CKG_NM' 열을 기준으로 중복 제거
    final_data = CK_cl.drop_duplicates(subset='CKG_NM')

    return final_data

# 최종 데이터 로드
final_data = load_data()

# ################################################
#2
# def to_markdown(text):
#     # to_markdown 함수 구현이 없으므로 간단한 출력 대체
#     print(text)
# model = gemini.GenerativeModel('gemini-pro')
# def 추출_및_생성(음식_목록):
#     prompt = """문장에서 식재료만 추출해줘.
# Input: 냉장고에 어묵이 있고, 당근도 있고, 토마토도 있고, 사과도 있고, 오이도 있어.
# Output: 어묵, 당근, 토마토, 사과, 오이
# Input: {}
# Output:
# """
#     # 모델에 입력할 프롬프트 생성
#     prompt_input = prompt.format(음식_목록)
#     # 모델에 프롬프트 전송
#     response = model.generate_content(prompt_input)
#     # 결과를 Markdown으로 변환 및 반환
#     return response.text
# ingredients = 추출_및_생성('음식_목록')
# def find_recipe_with_ingredients(ingredients):
#     def cook(selected_ingredients):
#         recipes = []
#         for _, row in final_data.iterrows():
#             recipe_ingredients = row['CKG_MTRL_CN'].lower().split(', ')
#             if all(all(ingredient in item for item in recipe_ingredients) for ingredient in selected_ingredients):
#                 recipes.append(row['CKG_NM'])
#         return recipes
#     selected_ingredients = [ingredient.lower().strip() for ingredient in ingredients]
#     possible_dishes = cook(selected_ingredients)
#     if not possible_dishes:
#         return "적합한 요리를 찾을 수 없습니다."
#     selected_dish = random.choice(possible_dishes)
#     selected_row = final_data[final_data['CKG_NM'] == selected_dish]
#     dish_ingredients = selected_row['CKG_MTRL_CN'].values[0]
#     return f"{selected_dish}: {dish_ingredients}"
################################################
#요리 추천 함수1
# def find_recipe_with_ingredients(ingredients):
#    def cook(selected_ingredients):
#        recipes = []
#        for _, row in final_data.iterrows():
#            recipe_ingredients = row['CKG_MTRL_CN'].lower().split(', ')
#            if all(all(ingredient in item for item in recipe_ingredients) for ingredient in selected_ingredients):
#                recipes.append(row['CKG_NM'])
#        return recipes

#    selected_ingredients = [ingredient.lower().strip() for ingredient in ingredients]
#    possible_dishes = cook(selected_ingredients)
#    if not possible_dishes:
#        return "적합한 요리를 찾을 수 없습니다."
    
#    selected_dish = random.choice(possible_dishes)
#    selected_row = final_data[final_data['CKG_NM'] == selected_dish]
#    dish_ingredients = selected_row['CKG_MTRL_CN'].values[0]

#    return f" '{selected_dish}' : {dish_ingredients}"
#######################################################
222222222222222222222222222222222222222222222222222222222222222222
def to_markdown(text):
    # to_markdown 함수 구현이 없으므로 간단한 출력 대체
    print(text)
model = genai.GenerativeModel('gemini-pro')
def 추출_및_생성(음식_목록):
    prompt = """문장에서 식재료만 추출해줘.
Input: 냉장고에 어묵이 있고, 당근도 있고, 토마토도 있고, 사과도 있고, 오이도 있어.
Output: 어묵, 당근, 토마토, 사과, 오이
Input: {}
Output:
"""
    # 모델에 입력할 프롬프트 생성
    prompt_input = prompt.format(음식_목록)
    # 모델에 프롬프트 전송
    response = model.generate_content(prompt_input)
    # 결과를 Markdown으로 변환 및 반환
    return response.text
ingredients = 추출_및_생성('음식_목록')
def find_recipe_with_ingredients(ingredients):
    def cook(selected_ingredients):
        recipes = []
        for _, row in final_data.iterrows():
            recipe_ingredients = row['CKG_MTRL_CN'].lower().split(', ')
            if all(all(ingredient in item for item in recipe_ingredients) for ingredient in selected_ingredients):
                recipes.append(row['CKG_NM'])
        return recipes
    selected_ingredients = [ingredient.lower().strip() for ingredient in ingredients]
    possible_dishes = cook(selected_ingredients)
    if not possible_dishes:
        return "적합한 요리를 찾을 수 없습니다."
    selected_dish = random.choice(possible_dishes)
    selected_row = final_data[final_data['CKG_NM'] == selected_dish]
    dish_ingredients = selected_row['CKG_MTRL_CN'].values[0]
    return f"{selected_dish}: {dish_ingredients}"
