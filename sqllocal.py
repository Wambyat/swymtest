import sqlite3
import pandas as pd


def SQLquery(query):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute(query)
    df = c.fetchall()
    return pd.DataFrame(df)


# Finds most common reviewerID
if __name__ == "__main__":
    qu = "SELECT * FROM posi_bl WHERE reviewerID = (SELECT reviewerID FROM posi_bl GROUP BY reviewerID ORDER BY COUNT(reviewerID) DESC LIMIT 1)"
    df = SQLquery(qu)
    print(df)
