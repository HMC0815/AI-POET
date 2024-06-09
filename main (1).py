#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
#from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#load_dotenv()

chat_model = ChatOpenAI(openai_api_key=api_key)

#subject = 'AI'
#result = chat_model.invoke(subject + '에 대한 시를 써줘')
#print(result.content)
#!pip install streamlit

import streamlit as st
st.title('인공지능 시인')
subject = st.text_input('시의 주제를 입력해주세요')
st.write('시의 주제:'+ subject)

if st.button('시 작성'):
    with st.spinner('시 작성중...'):
        result = chat_model.invoke(subject+'에 대한 시를 써줘')
    st.write(result.content)

