import streamlit as st
import pandas as pd

# --- Configuração da Página ---
st.set_page_config(
    page_title="Formulário de Registro - IHC",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Título e Descrição ---
st.title("📝 Formulário de Registro Simples")
st.markdown(
    """
    Olá! Este formulário interativo permite que você **registre dados de sexo e idade**,
    exibindo-os em uma tabela logo abaixo e com a **opção de download em CSV**.
    """
)
st.markdown("---")

# --- Inicialização da Sessão (para armazenar os dados) ---
if 'dados_registrados' not in st.session_state:
    st.session_state.dados_registrados = pd.DataFrame(columns=["Sexo", "Idade"])

# --- Função para limpar os campos do formulário ---
def clear_form_fields():
    st.session_state.sexo_input_form = "Masculino"
    st.session_state.idade_input_form = 25 # LINHA CORRIGIDA AQUI

# --- Formulário de Registro ---
st.header("✨ Registrar Novo Usuário")

# Definimos valores padrão para garantir que os campos sempre tenham um valor.
if 'sexo_input_form' not in st.session_state:
    st.session_state.sexo_input_form = "Masculino"
if 'idade_input_form' not in st.session_state:
    st.session_state.idade_input_form = 25 # LINHA CORRIGIDA AQUI

with st.form("registro_form"):
    col1, col2 = st.columns(2)
    with col1:
        sexo = st.selectbox(
            "Selecione o Sexo:",
            ["Masculino", "Feminino", "Outro"],
            key="sexo_input_form",
            index=["Masculino", "Feminino", "Outro"].index(st.session_state.sexo_input_form)
        )
    with col2:
        idade = st.number_input(
            "Digite a Idade:",
            min_value=0,
            max_value=120,
            key="idade_input_form",
            value=st.session_state.idade_input_form
        )

    st.markdown("---")
    registrar_button = st.form_submit_button("✅ Registrar Dados", on_click=clear_form_fields)

    if registrar_button:
        if sexo and idade is not None:
            novo_registro = pd.DataFrame([{"Sexo": sexo, "Idade": idade}])
            st.session_state.dados_registrados = pd.concat(
                [st.session_state.dados_registrados, novo_registro], ignore_index=True
            )
            st.success("Dados registrados com sucesso!")
        else:
            st.warning("Por favor, preencha todos os campos antes de registrar.")

# --- Exibição da Tabela de Dados ---
st.header("📋 Dados Registrados")

if not st.session_state.dados_registrados.empty:
    st.dataframe(st.session_state.dados_registrados, use_container_width=True)

    # --- Botão de Download CSV ---
    # Converte o DataFrame para CSV
    csv_data = st.session_state.dados_registrados.to_csv(index=False)

    st.download_button(
        label="📥 Baixar Tabela em CSV",
        data=csv_data,
        file_name="dados_registrados.csv",
        mime="text/csv",
        help="Clique para baixar os dados da tabela em formato CSV."
    )
else:
    st.info("Nenhum dado registrado ainda. Use o formulário acima para começar!")

st.info("Desenvolvido com ❤️ por seu especialista em Python e Streamlit.")
