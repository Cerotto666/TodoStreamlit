from utils import functions as f
import  streamlit as st

def home_page():
    st.title("Home")
    st.write("Benvenuto! Scegli cosa fare:")
    st.button("Vai a Visualizza", on_click=lambda: f.navigate_to('Visualizza'))
    st.button("Vai a Modifica", on_click=lambda: f.navigate_to('Modifica'))


def visualizza_page():
    st.title("Visualizza")
    st.write("Qui puoi visualizzare i dati.")
    data = ["Compito 1", "Compito 2", "Compito 3"]
    st.write("Elenco dei dati:")
    st.write(data)
    st.button("Torna alla Home", on_click=lambda: f.navigate_to('Home'))




def add_task():
    new_task = st.session_state.new_task
    st.session_state["tasks"].append(new_task)
    st.session_state["new_task"] = ""


def modifica_page():

    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []

    st.title("Modifica")
    st.write("Qui puoi modificare i dati.")
    st.text_input("Aggiungi un nuovo compito", key="new_task")
    st.button("Aggiungi", on_click=add_task)
    if st.session_state["tasks"]:
        st.write("Compiti aggiunti:")
        for task in st.session_state["tasks"]:
            st.write(f"- {task}")
    st.button("Torna alla Home", on_click=lambda: f.navigate_to('Home'))
