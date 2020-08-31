
from memegenerator.lib import the_called_function

import streamlit as st

res = the_called_function()

st.write(f'mon package dit: {res}')
