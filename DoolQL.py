
class DoolQL:
    def __init__(self, stmt, params):
            super().__init__()
            self.stmt = stmt
            self.params = params
    def __repr__(self):
        return f'<DoolQL Stmt: stmt = {self.stmt}    params = {self.params}>'
    def get(self):
        return {'stmt':self.stmt,'params':self.params}
