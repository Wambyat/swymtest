# basic strealit page that runs a sqlquery when i push a button
# and displays the results in a table

import streamlit as st
import pandas as pd

# import SQLQuery from qu.py
from qu import SQLquery

# create a button
if st.button('Run SQL Query'):
    df = SQLquery("SELECT * FROM posi_bl WHERE reviewerID = (SELECT reviewerID FROM posi_bl GROUP BY reviewerID ORDER BY COUNT(reviewerID) DESC LIMIT 1)")
    st.write(df)
    st.success("QUERY RAN SUCCESSFULLY")
    st.success("Name is "+str(df[4][0]))