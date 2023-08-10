import pandas as pd
import json
import sqlite3
from textblob import TextBlob
from sqllocal import SQLquery

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def modelRun():
    df = pd.read_json("AMAZON_FASHION.json", lines=True)
    df.drop(["style", "unixReviewTime", "reviewTime", "image"], axis=1, inplace=True)
    columns_with_nan = df.columns[df.isna().any()]
    df[columns_with_nan] = df[columns_with_nan].fillna("")
    print("1")
    df["reviewText_sentiment"] = df["reviewText"].apply(get_sentiment)
    print("now doing summery")
    df["summary_sentiment"] = df["summary"].apply(get_sentiment)

    positive_reviews_df = df[
        (df["reviewText_sentiment"] > 0) & (df["summary_sentiment"] > 0)
    ]

    db_name = "test.db"
    conn = sqlite3.connect(db_name)
    table_name_df = "posi_bl1"
    positive_reviews_df.to_sql(table_name_df, conn, if_exists="replace", index=False)
    conn.close()

    # select from table posi_bl where reviewerID is most repeated reviewerID
    qu = "SELECT * FROM posi_bl1 WHERE reviewerID = (SELECT reviewerID FROM posi_bl1 GROUP BY reviewerID ORDER BY COUNT(reviewerID) DESC LIMIT 1)"
    df = SQLquery(qu)
    print(df)

if __name__ == "__main__":
    modelRun()