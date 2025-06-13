import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px # Usaremos Plotly para gráficos interativos e mais estéticos

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
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Sexo', 'Idade'])

# --- Formulário de Registro ---
with st.form(key='registration_form', clear_on_submit=True):
    st.subheader("Novo Registro")
    col1, col2 = st.columns(2)
    with col1:
        sexo = st.selectbox(
            "Selecione o Sexo:",
            options=["Masculino", "Feminino", "Outro", "Prefiro não informar"],
            key="sexo_input",
            help="Escolha o sexo da pessoa."
        )
    with col2:
        idade = st.number_input(
            "Digite a Idade:",
            min_value=0,
            max_value=120,
            step=1,
            key="idade_input",
            help="Insira a idade da pessoa."
        )

    st.markdown("---")
    submit_button = st.form_submit_button(
        label="Registrar",
        type="primary",
        help="Clique para registrar os dados."
    )

    if submit_button:
        new_data = pd.DataFrame([{'Sexo': sexo, 'Idade': idade}])
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.success("Dados registrados com sucesso!")

# --- Exibição dos Dados em Tabela ---
st.markdown("## Dados Registrados")
if not st.session_state.data.empty:
    st.dataframe(st.session_state.data, use_container_width=True, hide_index=True)
else:
    st.info("Nenhum dado registrado ainda. Preencha o formulário acima.")

# --- Estatísticas e Gráficos ---
st.markdown("---")
st.markdown("## Estatísticas dos Registros")

if not st.session_state.data.empty:
    # Gráfico 1: Distribuição por Sexo (Gráfico de Barras - Plotly)
    st.subheader("Distribuição por Sexo")
    sexo_counts = st.session_state.data['Sexo'].value_counts().reset_index()
    sexo_counts.columns = ['Sexo', 'Contagem']
    fig_sexo = px.bar(
        sexo_counts,
        x='Sexo',
        y='Contagem',
        color='Sexo',
        title='Contagem de Registros por Sexo',
        labels={'Contagem': 'Número de Pessoas', 'Sexo': 'Gênero'},
        template="streamlit", # Tema para Streamlit
        text='Contagem' # Exibir os valores nas barras
    )
    fig_sexo.update_traces(textposition='outside')
    st.plotly_chart(fig_sexo, use_container_width=True)

    # Gráfico 2: Distribuição de Idades (Histograma - Matplotlib)
    st.subheader("Distribuição de Idades")
    fig_idade, ax_idade = plt.subplots(figsize=(10, 5))
    ax_idade.hist(st.session_state.data['Idade'], bins=range(0, 101, 5), edgecolor='black', color='#636EFA')
    ax_idade.set_title('Distribuição das Idades', fontsize=16)
    ax_idade.set_xlabel('Idade', fontsize=12)
    ax_idade.set_ylabel('Frequência', fontsize=12)
    ax_idade.grid(axis='y', alpha=0.75)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig_idade)

else:
    st.info("Registre alguns dados para visualizar as estatísticas.")

# --- Rodapé ---
st.markdown("---")
st.markdown("Desenvolvido com ❤️ por Seu Amor.")
