

# """UNIN in capitals will equal to uninitliazed if BaseObject is imported"""
# from helper import UNIN, isInitialized, dic2str
# from DoolQL import DoolQL
# class BaseObject:
#         def __init__(self):
#             self._name = self.__class__.__name__
#
#         @property
#         def name(self):
#             """ Returns the Class name"""
#             return self._name
#
#         @name.setter
#         def name(self, value=UNIN):
#             if not isInitialized(value):
#                 self._name = self.__class__.__name__
#             self._name = value
#
#         def __repr__(self):
#             """Return string version of dictionary representing the inner varrs all"""
#             return dic2str(self.getDic())
#
#         def save(self):
#             import json
#             path = '{}.dool'.format(self.name())
#             with open(path, 'w') as file:
#                 file.write(json.dumps(self.getDic()))
#                 return path
#
#         def getDic(self):
#             """Returns a Dictionary of all non-psudo-private attributes and vars"""
#             dic = vars(self)
#             dDic = {}
#             for k, v in dic.items():
#                 if not k.startswith('_'):
#                     dDic[k] = v
#             return dDic
#
# #        def getVarNames(self):
#  #           """ Returns the variable names of none hidden local variables in list form ordered as is"""
#   #          list((self.getDic()).keys())
# #
#  #       def getData(self):
#   #              """ Returns the values of none hidden local variables in list form ordered as is"""
#    #             list((self.getDic()).values())
