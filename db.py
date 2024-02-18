from socket import create_connection
import pandas as pd
from sqlalchemy import create_engine
import datetime as dt 

DB_HOST = "localhost"
DB_USERNAME = "root"
DB_PASS = "MySqlPasswordIsSecure925941@"
DB_DATABASE = "ppx_schedulee_db"
DB_PORT = 3306



class Database_Connection:
    def __init__(self):
        self.connection_string = f"mysql+pymysql://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
        
        
    def get_users(self):

        get_users_query = """
        SELECT user from users_table
        """
        users = list(pd.read_sql(get_users_query,self.connection_string)['users'])
        return users

    def parse_date(self,start_date,end_date):
        try:
            sd = dt.datetime.strptime(start_date, "YY-m-d")
            ed = dt.datetime.strptime(end_date, "YY-m-d")
            if ed>=sd:
                return sd,ed
            return 0,0
        except:
            return 0,0

    def get_activity_for_user(self,username, start_date,end_date):
        sd,ed = self.parse_date(start_date,end_date)
        if sd == 0 or ed == 0:
            return 0

        query_get_user_activity = f"""
        SELECT activity,datetime from activity_user_{username} where datetime > DATE({start_date}) and (datetime < {end_date});
        
        """
        user_data = pd.read_sql(query_get_user_activity,self.connection_string)
        return user_data.to_html()

