import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Sistema de Carteirinhas", layout="centered")

st.title("🏫 Cadastro de Carteirinha Escolar")
st.write("Pais, preencham os dados abaixo para gerar a identificação do aluno.")

# Formulário de entrada
with st.form("form_aluno"):
    turma = st.selectbox("Selecione a Turma", ["Pre4 ma", "pre4 mb", "", "4º Ano", "5º Ano"])
    nome = st.text_input("Nome Completo do Aluno")
    ra = st.text_input("Número do RA (Registro Acadêmico)")
    foto = st.file_uploader("Tire ou envie uma foto do aluno", type=["jpg", "png", "jpeg"])
   

    enviar = st.form_submit_button("Gerar Carteirinha")

# Lógica após clicar no botão
if enviar:
    if nome and ra and foto:
        st.success("Carteirinha gerada com sucesso!")
        
        # Design da Carteirinha
        st.markdown("---")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            img = Image.open(foto)
            st.image(img, use_container_width=True)
            
        with col2:
            st.subheader(f"👤 {nome}")
            st.write(f"**RA:** {ra}")
            st.write(f"**TURMA:** {turma}")
            st.write(f"**VALIDADE:** 12/2026")
            st.caption("Documento Digital Escolar")
            
        st.info("💡 Você pode tirar um print desta tela para salvar a carteirinha no celular.")
    else:
        st.error("Por favor, preencha todos os campos e envie uma foto.")