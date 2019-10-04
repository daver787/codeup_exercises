from env import host, user, password
import pandas as pd
def get_db_url():
    url = f'mysql+pymysql://{user}:{password}@{host}/employees'
    return url

url=get_db_url()
employees=pd.read_sql('''SELECT * FROM employees''',url)
titles=pd.read_sql('''SELECT * FROM titles''',url)