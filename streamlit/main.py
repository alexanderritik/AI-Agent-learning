import streamlit as st

from streamlit_ace import st_ace

st.write("hello Ritik") #It automatically write anything on the browser
st.write({"key": "value"})

3+4 # if you write anything in main line of stream code
"hello" if False else "bye"

#If any button pressed or you interactive with any widget the whole app will and this how streamlit work
pressed = st.button("Press me")
print(pressed)


st.title("Super title")
st.subheader('Small header')
st.markdown("This is markdown")


code_example = """
def greet(name):
    print("hello", name)
"""
st.code(code_example, language="python")

code_example_json = """
{
    "hello": 21,
    "king": "myname"
}
"""
st.code(code_example_json, language="json")


# #running editor
content = st_ace()

content