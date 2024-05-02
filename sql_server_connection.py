import pyodbc
import os
import dotenv
from sql_models.produto_model.produto import MetodosProduto

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
            if query_return != None:
                produto_model = MetodosProduto.convert_to_product_type(query_return)
                return {"status_db": "success", "query_return": produto_model}
            else:
                return {"status_db": "product_not_found"}    
        else:
            return {"status_db": "failed"}
        
    def get_product_by_description(self, description):
        if self.connection_db != None:
            query_return = self.cursor_connection.execute(f"SELECT * FROM [SICNET_139726].[dbo].[TABEST1] WHERE [produto] LIKE '%{description}%';").fetchall() #query
            if len(query_return) != 0:
                lista_de_produtos = []
                for produto in query_return:
                    produto_model = MetodosProduto.convert_to_product_type(produto)
                    lista_de_produtos.append(produto_model)
                return {"status_db": "success", "query_return": lista_de_produtos}
            else:
                return {"status_db": "product_not_found"}    
        else:
            return {"status_db": "failed"}