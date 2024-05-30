import streamlit as st
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

def main():
        st.title('Início')
        st.divider()
        number = st.number_input("Escolha um número para a Tabuada: ", step=1, placeholder="Escreva o número aqui")
        st.divider()
        for i in range(1,11):
            st.text(f'{number} x {i} = {number * i}')
        st.divider()
    
main()
