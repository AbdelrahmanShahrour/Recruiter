# import the streamlit library
import streamlit as st
import pandas as pd
from serpapi import GoogleSearch


# give a title to our app
st.title('AutoRecruiterEngine - 0.2')
 # Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Engine", "Final Results"])
tab1.write("this is Engine")
tab2.write("this is results")

def scrap(q):
    search = GoogleSearch({
        "q": q, 
        "api_key": "1835fadd674bcb5f97ec8bbf2c66cd388599e307ab40ab27f3d49b0f8345e107",
        "num": "40"
    })
    result = search.get_dict()
    result.get("organic_results")
    link, name, PosComp, snippet_highlighted_words, snippet = [], [], [], [], []
    for item in result.get("organic_results"):
        link.append(item.get("link"))
        x = item.get("title").split('-')
        name.append(x[0])
        PosComp.append(x[1:])
        snippet_highlighted_words.append(item.get("snippet_highlighted_words"))
        snippet.append(item.get("snippet"))
        print('===========================\n')
        
    data = pd.DataFrame({"name":name, "link":link, "Pos and Comp":PosComp, "snippet_highlighted_words":snippet_highlighted_words, "snippet":snippet})
    return data

with tab1:
    st.write("## Is Must")
    must1 = st.text_input('KeyWords')
    btn = st.button('Click me')

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')




with tab2:
    if btn:
        q1 = f""" site:jo.linkedin.com/in {must1}"""
        print(q1)
        data = scrap(q1)
        st.write(data)
        csv = convert_df(data)
        st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Rec.csv',
        mime='text/csv',
        )
    else:
        st.warning('Not found results yet')
    
    