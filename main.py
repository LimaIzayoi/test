import streamlit as st
import pandas as pd

# --- Configurações da Página ---
st.set_page_config(
    page_title="Formulário de Registro - Pessoas",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Título e Descrição ---
st.title("📝 Registro de Pessoas")
st.markdown("Preencha os campos abaixo para registrar informações de sexo e idade.")

# --- Inicialização da Sessão de Dados ---
# Usamos st.session_state para manter os dados mesmo após interações do usuário
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Sexo', 'Idade'])

# --- Formulário de Registro ---
# st.form agrupa os elementos do formulário e permite limpar os campos após o envio
with st.form(key='registration_form', clear_on_submit=True):
    st.subheader("Novo Registro")
    
    # Organiza os campos em duas colunas para melhor aproveitamento do espaço (UX)
    col1, col2 = st.columns(2)
    
    with col1:
        sexo = st.selectbox(
            "Selecione o Sexo:",
            options=["Masculino", "Feminino", "Outro", "Prefiro não informar"],
            key="sexo_input",
            help="Escolha o sexo da pessoa." # Dica útil ao usuário
        )
    with col2:
        idade = st.number_input(
            "Digite a Idade:",
            min_value=0,
            max_value=120,
            step=1,
            key="idade_input",
            help="Insira a idade da pessoa (de 0 a 120 anos)."
        )

    st.markdown("---") # Linha divisória para separar visualmente
    
    # Botão de submissão do formulário
    submit_button = st.form_submit_button(
        label="Registrar",
        type="primary", # Destaca o botão principal
        help="Clique para registrar os dados na tabela abaixo."
    )

    # Lógica para adicionar os dados quando o botão é clicado
    if submit_button:
        new_data = pd.DataFrame([{'Sexo': sexo, 'Idade': idade}])
        # Concatena o novo registro com os dados existentes
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.success("Dados registrados com sucesso!") # Feedback visual para o usuário

---

# Exibição dos Dados em Tabela

st.markdown("## Dados Registrados")

# Verifica se há dados para exibir
if not st.session_state.data.empty:
    # Exibe o DataFrame como uma tabela interativa
    st.dataframe(st.session_state.data, use_container_width=True, hide_index=True)
else:
    st.info("Nenhum dado registrado ainda. Preencha o formulário acima para começar.")

---

# Rodapé

st.markdown("Desenvolvido com ❤️ por Seu Amor.")
