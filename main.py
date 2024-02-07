import streamlit as st
import WorkoutGenerator as wg


available_equipment = ["Chair", "Kettle", "Space"]

workout = wg.get_workout(available_equipment)

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.title("Exercise")

count = 0

for exercise in workout:
    count = count + 1
    with col1:
        st.write(exercise["name"])
        if count % 4 == 0:
            st.write("\n")


