import openai
import os
import json
import streamlit as st


openai.organization = "org-LHvw1N9BZvsiUKmaQdsj5S4M"
openai.api_key = "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"
openai.Model.list()


st.set_page_config(layout="wide")

st.markdown("""
<style>
.bigger-font {
    font-size:18px !important;
}
.biggest-font {
    font-size:20px !important;
}

</style>
""", unsafe_allow_html=True)

st.write('# Da Vinci Story generator')
st.write('### By @Edgecaser')

st.markdown('<p class="bigger-font">This uses the DaVinci model by OpenAI to generate a short story.</p>', unsafe_allow_html=True)
st.markdown('<p class="bigger-font">It requires a sample story from you. You will need an OpenAI account</p>', unsafe_allow_html=True)

orgnid = st.text_input('What is your Organization ID?',help='Found in settings page')

apikey = st.text_input('What is your API key',help='Found in the API Keys page')

openai.Model.retrieve("text-davinci-002")

storytopic = st.text_input('Okay. We need a sample of writing to get your style. What is your story about?',help='One or two words to describe the overall topic of your story',max_chars=200)

story = st.text_input('Okay. We need a sample of writing to get your style. What is your story about?',help='Wax Poetic... up to 1500 characters',max_chars=1600)

newtopic = st.text_input('Nice! What should your short story be about?',help='One or two words to describe the overall topic of your story',max_chars=200)


if st.button('START'):
  promptstring = 'Topic:' + storytopic + '\nShort Story: ' + story + '\nTopic:' + newtopic + '\n Short Story:'
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=promptstring,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0
  )
  #response.choices[0].text
  st.write(response.choices[0].text)
