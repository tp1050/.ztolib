import sys
sys.path.append('/home/c/PycharmProjects/lib')
from DoolQL import DoolQL
from helper import UNIN,isInitialized,loadDic,saveDic,isUnin,tprint
from BaseObject import BaseObject
import mysql.connector
from Doolception import TDBOffline
from sqlalchemy import create_engine as CreateEngine

# from mysql.connector import Error
# from mysql.connector import pooling
# # class DBEngine(BaseObject):
# #     def __init__(self,address,engineProvider='mySQL',confDict={}):
# #         self.address=address
# #         self.engineProvider=engineProvider
# #
# #     def mySql(self,confDict={}):
# #         self.address.update(confDict)
# #         self.engine=mysql.connector.connect(**self.address)
# #     def sqlLite(self):
# #         self.engine=createEngine(f'mysql://{self.address.user}:{self.address.password}@{self.address.host}:{self.address.port}')
# #
# #     def mySQLConfUpdate(self,confDict):
# #         self.confDict.update(confDict)
# #     def mySQLConf(self):
# #         return self.mySQLConf
# class DBEngine(BaseObject):
#     def __init__(self,address,engineProvider='mySQL',confDict={}):
#         if engineProvider=='mySQL':
#             self.address.update(confDict)
#             self.engine=createEngine(f'mysql://{self.address.user}:{self.address.password}@{self.address.host}:{self.address.port}')
#         elif engineProvider=='SQLLITE':
#             self.engine=createEngine(f'sqllite://{self.address.user}:{self.address.password}@{self.address.host}:{self.address.port}')
#         elif engineProvider=='MYSQLPool':
#             try:
#                 from mysql.connector.pooling import MySQLConnectionPool as PMS
#                 confDict={'pool_name':"pynative_pool",'pool_size':5,'pool_reset_session':True,'auth_plugin' : 'mysql_native_password'}
#                 self.address.update(confDict)
#                 connectionPool=PMS(**address)
#                 connIns=connectionPool.get_connection()
#                 if connIns.is_connected():
#                     return connectionPool,connIns
#                     # db_Info = c.get_server_info()
#     def engine(self):
#         return self.engine



class TDB(BaseObject):
    def __init__(self, host=UNIN, port=UNIN, user=UNIN, password=UNIN, database=UNIN):
        arg = locals()
        del arg['self']
        if isInitialized(arg):
            self.address =arg
        else:
            self.loadAddress()
        self._conn = UNIN
        self.initialize()

    def saveAddress(self,path=UNIN):
        if isUnin(path):
            path='cfg.dool'
        saveDic(self.address,path)
    def loadAddress(self,path=UNIN):
        if isUnin(path):
            path='cfg.dool'
        self.address = loadDic(path)



    def getConn(self):
        if self.isConnected():
            return self._conn
        else:
            raise TDBOffline('KHAIR>> TDB object instace is offline')

    def initialize(self):
        self.address['auth_plugin'] = 'mysql_native_password'
        self._conn = mysql.connector.connect(**self.address)
        # self._conn.ping(reconnect=True, attempts=10, delay=1)
        return self.getConn()

    def isConnected(self):
        try:
            return self._conn.is_connected()
        except Exception as e:
            print (e)
            return False


    def insert(self, stmt, params):
        if not self.isConnected():
            self.initialize()
        mc = self._conn.cursor(buffered=True)
        mc.execute(stmt, params)
        self._conn.commit()
        mc.close
        return 'Khoob'

    def select(self, stmt, params):
        if not self.isConnected():
            self.initialize()
        mc = self._conn.cursor(prepared=True)
        print(stmt, params)
        mc.execute(stmt, params)
        ret = mc.fetchall()
        mc.close()
        return ret
