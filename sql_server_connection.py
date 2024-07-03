import pyodbc
import os
import dotenv
from sql_models.produto_model.produto import MetodosProduto
from sql_models.sales_model.sales_type import MethodsTypesSales
from sql_models.sales_model.sales import MethodsSales

dotenv.load_dotenv()

class ConnectionDatabase():
    def __init__(self) -> None:
        STRING_CONNECTION_DB_NEW = os.getenv('STRING_CONNECTION_DB_NEW')
        self.connection_db = None
        self.cursor_connection = None
        try:
            self.connection_db = pyodbc.connect(STRING_CONNECTION_DB_NEW)
            self.cursor_connection = self.connection_db.cursor()
            print("Conection with DB - Success!")
        except Exception as error_except:
            print(f"Conection with DB - Failed!\nError:{error_except}")
    
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
        
    def get_type_sales(self):
        if self.connection_db != None:
            query_return = self.cursor_connection.execute("SELECT * FROM [SICNET_139726].[dbo].[TABEST7]").fetchall() #query
            if len(query_return) != 0:
                lista_de_tipos_de_recebimentos = []
                for tipo in query_return:
                    tipo_model = MethodsTypesSales.convert_to_sales_types(tipo)
                    lista_de_tipos_de_recebimentos.append(tipo_model)
                return {"status_db": "success", "query_return": lista_de_tipos_de_recebimentos}
            else:
                return {"status_db": "types_not_found"}    
        else:
            return {"status_db": "failed"}

    def get_sales_not_note(self, sale_search):
        if self.connection_db != None:
            query_return = self.cursor_connection.execute(f"SELECT TOP (1000) [data], [nota], [pedido], [lkreceb] FROM [SICNET_139726].[dbo].[TABEST3A] WHERE [lkreceb] = {sale_search.type_sale} AND [lkcliente] = 0 AND [nota] IS NULL AND [data] >= '{sale_search.start_date}' AND [data] <= '{sale_search.end_date}';").fetchall() #query
            if len(query_return) != 0:
                lista_de_vendas = []
                for venda in query_return:
                    venda_model = MethodsSales.convert_to_sales(venda)
                    lista_de_vendas.append(venda_model)
                return {"status_db": "success", "query_return": lista_de_vendas}
            else:
                return {"status_db": "types_not_found"}    
        else:
            return {"status_db": "failed"}
        