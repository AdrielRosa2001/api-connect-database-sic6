import pyodbc
import os
import dotenv

dotenv.load_dotenv()

class ConnectionDatabase():
    def __init__(self) -> None:
        STRING_CONNECTION_DB = os.getenv('STRING_CONNECTION_DB')
        self.connection_db = None
        self.cursor_connection = None
        try:
            self.connection_db = pyodbc.connect(STRING_CONNECTION_DB)
            self.cursor_connection = self.connection_db.cursor()
            print("Conection with DB - Success!")
        except:
            print("Conection with DB - Failed!")
    
    def get_product_by_code(self, code):
        if self.connection_db != None:
            query_return = self.cursor_connection.execute(f"SELECT * FROM [SICNET_139726].[dbo].[TABEST1] WHERE [codigo] = '{code}';").fetchone() #query
            return {"status_db": "success", "query_return": query_return}
        else:
            return {"status_db": "failed"}
        
connection_db = ConnectionDatabase()
return_data = connection_db.get_product_by_code('7896741313348')
if return_data['status_db'] == "success":
    print(return_data['query_return'])
else:
    print("Banco de dados indisponível no momento!")


#7896741313348