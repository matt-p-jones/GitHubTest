import streamlit as st
import pandas as pd
import altair as alt
st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_karts = pd.read_csv('data/kart_stats.csv')
# st.dataframe(df_karts)
df_karts = df_karts[['Body','Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Handling']]

st.dataframe(df_karts.style
             .highlight_max(color='lightgreen',axis=0,subset=['Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Handling'])
             .highlight_min(color='red',axis=0,subset=['Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Handling'])
)

st.line_chart(df_karts, x='Weight',y='Acceleration')

alt_chart = (
    alt.Chart(df_karts)
    .mark_circle()
    .encode(x="Weight", y="Ground Handling", color="Body", tooltip= ["Body","Weight","Ground Handling"])
)
st.altair_chart(alt_chart,use_container_width=True)

chosen_kart = st.selectbox('Pick a Kart', df_karts['Body'])
df_single_kart = df_karts.loc[df_karts['Body']==chosen_kart]
df_single_kart= df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart, x='category', y='strength')
