import streamlit as st

# 웹페이지 제목
st.title("🔢 재미있는 구구단 프로그램")
st.subheader("원하는 단을 선택하면 구구단이 출력됩니다.")

# 사용자로부터 단 입력 받기 (슬라이더 형태)
dan = st.slider("몇 단을 보고 싶으신가요?", min_value=2, max_value=9, value=2)

st.markdown(f"### 🎯 {dan}단 출력 결과")

# 구구단 계산 및 출력
for j in range(1, 10):
    # st.write를 사용하면 웹 화면에 텍스트가 출력됩니다.
    st.write(f"{dan} × {j} = {dan * j}")