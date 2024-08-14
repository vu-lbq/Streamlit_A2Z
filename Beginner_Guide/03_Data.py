# Import Necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
# Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))