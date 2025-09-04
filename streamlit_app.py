import streamlit as st
import pandas as pd
from datetime import date 

st.title("급식 인기 메뉴 랭킹 앱 🍔🍜")
st.write("우리 학교 급식 통계를 확인하고 급식 메뉴를 평가해주세요🎉")

#2. 웹에 게시된 csv파일 불러오기
url = "https://github.com/teacher188-netizen/blank-app/blob/main/meals_data.csv"+"?raw=true"
df = pd.read_csv(url, encoding = 'cp949')
st.dataframe(df)

#3. 데이터 대시보드 만들기
st.write("오늘의 메뉴를 표 형태로 확인할 수 있어요.")
#오늘 날짜 불러오기
dt = str(date.today())
today_row = df.loc[df['급식일자']== dt]
st.write(today_row)

#metric 활용하기
st.write("metric으로 통계 정보를 전광판 형태로 시각화할 수 있어요.")
st.title(today_row['요리명'].item())
st.metric("오늘의 메뉴", today_row['요리명'].item(),border=True)

#metric 열 만들기
a, b = st.columns(2)
a.metric("칼로리", today_row['칼로리정보(Kcal)'].item(), 1600-today_row['칼로리정보(Kcal)'].item(), border=True)
b.metric("단백질", today_row['단백질(g)'].item(), 40-today_row['단백질(g)'].item(), border=True)

#4. 차트로 데이터 시각화하기

#4-1. 지도 만들기
map_data = pd.DataFrame({
    'lat': [37.5665, 37.5700, 37.5796],
    'lon': [126.9780, 126.9920, 126.9770],
    'place': ['시청', '동대문', '경복궁']
})

st.map(map_data)


#4-2. 선 그래프 만들기
st.line_chart(df, x='급식일자', y = ['칼로리정보(Kcal)'])

#4-3. 막대 그래프 만들기
st.bar_chart(df, x ='요일', y = '칼로리정보(Kcal)', color = '급식일자' , horizontal = True)



#다양한 입력 기능
st.date_input("날짜를 선택할 수 있는 입력폼") 
st.selectbox("항목 중 하나를 선택할 수 있는 입력폼", ["월", "화", "수", "목", "금"])
st.text_input("주관식 입력폼", placeholder="placehoder에 들어가는 값이 힌트가 됩니다.")
st.slider("슬라이더를 조정해서 값을 선택하는 입력폼", 1, 5)
st.radio("객관식 버튼 입력폼", ["1", "2", "3", "4", "5"])

#입력 기능을 하나로 묶기
#with: 각종 요소를 함께 묶어서 입력한 내용을 제출버튼으로 한 번에 제출 가능
with st.form("폼 이름 설정"):
    #각종 입력 기능을 넣어서 폼 안에 들어갈 질문을 작성합니다.
    # 변수 = 입력 기능 명령어 형식으로 작성하세요.
    d = st.date_input("급식 날짜를 선택해주세요.") 

    #제출 버튼이 있어야 전송이 가능합니다.(필수)
    submitted = st.form_submit_button("제출")

#제출 내용 확인
if submitted:
    #제출내용을 웹에 바로 보여줍니다.
    st.write(f"""
            with st.form 안에 들어있는 변수를 중괄호 안에 넣으면 변수와 문자를 함께 출력할 수 있어요.\n
            날짜: {d}
            """)
