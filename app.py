import streamlit as st
import json

# Carregar dados do arquivo JSON
with open('5fdf88c3.json', 'r', encoding='utf-8') as f:
    teams = json.load(f)

st.title("Busca Interativa por Times de Futebol Brasileiros")

# Caixa de seleção para escolher o time
team_names = [team['name'] for team in teams]
selected_team = st.selectbox("Escolha um time:", team_names)

if selected_team:
    team = next(t for t in teams if t['name'] == selected_team)
    st.header(f"{team['name']} ({team['founded_date']})")
    st.markdown(f"- **Cidade / Estado:** {team['city']} / {team['state']}")
    st.markdown(f"- **Cores:** {team['colors']}")
    st.markdown(f"- **Campeonato Brasileiro:** {team.get('brazilian_championship', 'N/A')}")
    st.markdown(f"- **Libertadores da América:** {team.get('libertadores', 'N/A')}")
    st.markdown(f"- **Copa do Brasil:** {team.get('copa_do_brasil', 'N/A')}")
    # Informações estaduais com fallback para diferentes estados
    st.markdown(f"- **Títulos Estaduais:** {team.get('paulista', team.get('carioca', team.get('gaucho', team.get('mineiro', 'N/A'))))}")
    st.markdown(f"- **Total de títulos importantes:** {team.get('total_titles', 'N/A')}")
    st.subheader("História resumida:")
    st.write(team['history'])