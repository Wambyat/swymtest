import pandas as pd
import json
import sqlite3
from textblob import TextBlob
from sqllocal import SQLquery
import streamlit as st
import pandas as pd

# import SQLQuery from qu.py
from sqllocal import SQLquery
from model import modelRun


# This displays the results from the sql db
def query(table_name):
    df = SQLquery(
        f"SELECT * FROM {table_name} WHERE reviewerID = (SELECT reviewerID FROM posi_bl GROUP BY reviewerID ORDER BY COUNT(reviewerID) DESC LIMIT 1)"
    )
    st.write(df)
    st.success("QUERY RAN SUCCESSFULLY")
    st.success("Name is " + str(df[4][0]))
    df = SQLquery(
        f"SELECT * FROM {table_name} WHERE asin = (SELECT asin FROM posi_bl GROUP BY asin ORDER BY COUNT(asin) DESC LIMIT 1)"
    )
    st.write(df)
    # st.success("QUERY RAN SUCCESSFULLY")
    # st.success("Product is "+str(df[3][0]))

    df = SQLquery("SELECT * FROM main_meta WHERE asin = '" + str(df[3][0]) + "'")
    st.write(df)
    st.success("QUERY RAN SUCCESSFULLY")
    st.success("Product is " + str(df[0][0]))
    st.success("Rank is " + str(df[4][0]))
    st.write("Price is: " + "\\" + str(df[8][0]))
    st.title("Description below")
    st.write(str(df[7][0]).strip("[]").strip('"'))


# This is to run without running model
if st.button("Run SQL Query (Model wont be rerun)"):
    query("posi_bl")


if st.button("Run model again (This takes approximatly 8-10 mins)"):
    # put this in a loading circle
    with st.spinner("Model called and running...."):
        modelRun()
    st.success("MODEL RAN SUCCESSFULLY")
    query("posi_bl1")
