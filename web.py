import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
for todo in todos :
    checkbox = st.checkbox(todo,key = todo)
    if checkbox :
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "" , placeholder= " Enter Todo ..." ,
              on_change= add_todo , key = "new_todo") 
