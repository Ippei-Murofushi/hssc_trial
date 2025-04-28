import streamlit as st
import pandas as pd

df = pd.read_csv('./sample.csv')
edited_df = st.data_editor(df)

#favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
#st.markdown(f"Your favorite command is **{favorite_command}** 🎈")