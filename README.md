# Product Review Analysis

### This is repo that was made for the test I attended from swym.

| File Name       | Use                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `db.ipynb`      | This is a notebook where store the given JSON files into a SQL database.                                                    |
| `disp.py`       | This is the main driver code. It starts the website and is linked to `sqllocal.py` and `model.py`.                          |
| `model.py`      | This is the main model code. It uses `textblob` for natural language processing. It also saves the results in the database. |
| `queries.ipynb` | This is a notebook where I test SQL queries.                                                                                |
| `sqllocal.py`   | This has the logic for connecting to the database and running queries.                                                      |
| `test.ipynb`    | This is the notebook where I test the model.                                                                                |

### Requirements:

- Usual python install
  
  - textblob
  
  - sqlite3 (Usually included with python)
  
  - streamlit

- Web browser

- The required JSON files. (Not uploaded here as file size is very large)

### How to run:

1. First download the entire git repository and the JSONs.

2. Install everything required.

3. Run `db.ipynb` to save the JSONs in the database. This is currently not a automatic process and needs a little python knowledge.

4. After that run `disp.py` by typing the command `streamlit run disp.py`.

5. Enjoy!

Demo link [https://drive.google.com/file/d/1pc7m9qu1QeuiJn7iWpWXwf-Xlk88asw5/view?usp=sharing](https://drive.google.com/file/d/1pc7m9qu1QeuiJn7iWpWXwf-Xlk88asw5/view?usp=sharing)
