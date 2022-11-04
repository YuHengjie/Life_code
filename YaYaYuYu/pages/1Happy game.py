# %%
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt

# %%
plt.style.use('default')

st.set_page_config(
    page_title = 'Hello',
    page_icon = '💫',
    layout = 'wide'
)

# %%
st.sidebar.success("Select a module above.")

# %%
st.write("# Coming soon ...")