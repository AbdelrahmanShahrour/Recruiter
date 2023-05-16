# import the streamlit library
import streamlit as st


# give a title to our app
st.title('AutoRecruiterEngine - 0.1')
 # Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Engine", "Results"])
tab1.write("this is Engine")
tab2.write("this is results")

with tab1:
    st.write("## Is Must")
    col1, col2, col3 = st.columns(3)
    with col1:
        must1 = st.text_input('Skill 1')
    with col2:
        must2 = st.text_input('Skill 2')
    with col3:
        must3 = st.text_input('Skill 3')

    st.write("## Is Plus")
    col4,col5, col6 = st.columns(3)
    with col4:
        plus1 = st.text_input('Skill 4')
    with col5:
        plus2 = st.text_input('Skill 5')
    with col6:
        plus3 = st.text_input('Skill 6')

    btn = st.button('Click me')
with tab2:
    if btn:
        st.write(f"""is must : {must1}, {must2}, {must3}
                    is plus : {plus1}, {plus2}, {plus3}
        """)
    else:
        st.warning('Not found results yet')

