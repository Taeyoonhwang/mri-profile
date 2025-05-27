# MRI v1 - Profile Viewer (Streamlit)
# 내부 데이터 기반 - Google Sheets 미사용

import streamlit as st
import pandas as pd

# ----------------------------
# 초기 데이터 - 생두 프로파일 예시
# ----------------------------
def load_initial_data():
    data = [
        {"품목명": "Kenya AA TOP", "1st 타겟": "08:00", "DT 타겟": "09:30", "Drop 타겟": "11:00"},
        {"품목명": "Ethiopia G1", "1st 타겟": "07:30", "DT 타겟": "09:00", "Drop 타겟": "10:40"},
        {"품목명": "Colombia Supremo", "1st 타겟": "08:10", "DT 타겟": "09:40", "Drop 타겟": "11:10"},
        {"품목명": "Guatemala Antigua", "1st 타겟": "08:05", "DT 타겟": "09:35", "Drop 타겟": "11:05"},
        {"품목명": "Brazil Santos", "1st 타겟": "08:00", "DT 타겟": "09:20", "Drop 타겟": "10:50"},
    ]
    return pd.DataFrame(data)

# ----------------------------
# 앱 시작
# ----------------------------
st.set_page_config(page_title="MRI - Profile Viewer", page_icon="🌱", layout="wide")
st.title("🌱 Museo Roasting Intelligence - Profile")

# 세션 상태에 데이터프레임 저장
if "profile_df" not in st.session_state:
    st.session_state.profile_df = load_initial_data()

df = st.session_state.profile_df

# ----------------------------
# 데이터 테이블 출력
# ----------------------------
st.subheader("📋 기준 프로파일 목록")
st.dataframe(df, use_container_width=True)

# ----------------------------
# 새로운 프로파일 추가 폼
# ----------------------------
with st.expander("➕ 새 프로파일 추가"):
    with st.form("add_profile_form"):
        item = st.text_input("품목명")
        first = st.text_input("1st 타겟", placeholder="예: 08:00")
        dt = st.text_input("DT 타겟", placeholder="예: 09:30")
        drop = st.text_input("Drop 타겟", placeholder="예: 11:00")
        submitted = st.form_submit_button("추가하기")

        if submitted and item:
            new_row = {"품목명": item, "1st 타겟": first, "DT 타겟": dt, "Drop 타겟": drop}
            st.session_state.profile_df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            st.success(f"'{item}' 프로파일이 추가되었습니다!")
            st.experimental_rerun()
