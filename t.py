
import pandas as pd
from sqlalchemy import create_engine
import datetime as dt 


DB_HOST = "localhost"
DB_USERNAME = "root"
DB_PASS = "MySqlPasswordIsSecure925941@"
DB_DATABASE = "ppx_schedulee_db"
DB_PORT = 3306


connection_string = f"mysql+pymysql://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}"
eng = create_engine(connection_string)
table = str()
with eng.connect() as con:
    table = con.execute("SELECT * FROM users_table").all()
print(table)