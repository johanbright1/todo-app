import streamlit as st
import functions


todos = functions.get_todos()

st.title("Todo App")
st.subheader("Welcome to my todo app")
st.write("Built to increase productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "", placeholder = "Add new todo...")
