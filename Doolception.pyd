
class Doolception(Exception):
      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class TDBOffline(Doolception):
    def __init__(self,message,*args):
        super().__init__(*args)
        self._message=message

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TDBOffline:
            print(f"{func.__name__} TDB is offline")
            return inner_function
