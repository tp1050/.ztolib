from BaseObject import BaseObject
from helper import UNIN, isInitialized, dic2Lists, virgool, berin, INSRTSTMTTEMPLATE,isUnin
from TTable import TTable
from DoolQL import DoolQL


class UseFullObject(BaseObject):
    def __init__(self, content=UNIN, dbConn=UNIN):
        super().__init__()
        self._insertStmt = UNIN
        self._dbConn = dbConn
        self.content = content


    @property
    def insertStmt(self):
        """Insert statement is required in order to push the instance state to DB"""
        colnames, vals = dic2Lists(self.getDic())
        valPlaceHolders = ''
        if isinstance(colnames, list):
            colnames = virgool(colnames)
            valPlaceHolders = berin(len(vals), ',%s', verbose=False)[1:]
        else:
            valPlaceHolders = '%s'
        stmt = INSRTSTMTTEMPLATE.format(
            TABLE=self.name, COLNAMES=colnames, VALS=valPlaceHolders)
        self._insertStmt = DoolQL(stmt, tuple(vals))
        return self._insertStmt

    @insertStmt.setter
    def insertStmt(self, value):
        raise Exception(
            "Khiar:>> updateing the insert statment is currently not possible")

    def push(self):
        if isUnin(self._dbConn):
            raise Exception('Khiar : Connection Object is not isInitialized')
        self._dbConn.insert(self.insertStmt.stmt, self.insertStmt.params)


    def tabulate(self):
        d = self.getDic()
        return TTable(list(d.keys()), list(d.values()))
        #return TTable(self.getVarNames(),self.getData())
    def html(self):
        return self.tabulate().html()
