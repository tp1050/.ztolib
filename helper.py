# import datetime
# from Kooft import *
import tempfile
import os
import numbers
import pwd
import json
import re
import copy


### Global Static Values
UNIN = '<!NO!>'
INSRTSTMTTEMPLATE = 'INSERT INTO {TABLE}({COLNAMES}) VALUES({VALS})'


###Numerical
###*** CONVERSIONS
def ffloat(f):
    return float(f.replace(',', ''))


def getPriceFromString(s):
    regex = r"(?:[\£\$\€]{1}[,\d]+.?\d*)"
    ret = re.findall(regex, s)
    return [{r[0]:ffloat(r[1:])} for r in ret]

### Text Processing


def sortedList(inList, format=UNIN):
    sorted_list = list(sorted(inList, key=len))
    if isUnin(format):
        return sortedList
    if format == 'dic':
        dic1 = {k: len(k) for k in sorted_list}
        return dic1
    return sorted_list
###***Display Methods


def tprint(*args, **kwargs):
	# """A metghod to diffrentiate programmer prints"""
	prompt = '021CI>>'
	return print(prompt, *args, **kwargs)


def disp(obj, verbose=False):
    if verbose:
        if isinstance(obj, list):
            for o in obj:
                tprint(o)
        elif isinstance(obj, dict):
            tprint(dic2str(obj))
        else:
            tprint(obj)
    return obj


def mySQLTypedFormat(e):
	if isinstance(e, numbers.Number):
		return e
	elif e == '*':
		return '{}'.format('*')
	else:
		return '`{}`'.format(e)


def virgool(inList, quotation='', sym=',', boundBy='', sql=0) -> str:
	inlist2 = []
	if sql == 1:
		for i in inList:
			inlist2.append(mySQLTypedFormat(i))
		inList = inlist2
	boundByL, boundByR = braces(boundBy)
	ret = ''
	for item in inList:
		ret = '{ret}{sym}{quotation}{item}{quotation}'.format(
		    ret=ret, sym=sym, quotation=quotation, item=item)
	ret = '{boundByL}{ret}{boundByR}'.format(
	    boundByL=boundByL, ret=ret[1:], boundByR=boundByR)
	return ret


def berin(n=1, sign='-', indent=0, verbose=1):
	"""   t$ for timestamp"""
	indented = ''
	if indent > 0:
	    indented = berin(n=indent, sign=' ', indent=0, v=0)
	if sign == 't$':
	    sign = datetime.datetime.now()
	ret = ''
	for i in range(n):
	    ret = '{} {}'.format(sign, ret)
	ret = '{}{}'.format(indented, ret)
	if verbose:
	    print(ret)
	return ret

###***Conversion Methods


def dic2str(d, separator=':', lineSeparator=',', b=False) -> str:
	""" convert Dictionary Obj to Str d= input dictionary  separator : Defualt is : but could be set to anything. """
	retTMP = '{}{}{}'
	ret = ''
	tmp = '{} {} {}'
	if b:
		for i, j in d.items():
			ret = retTMP.format(ret, lineSeparator, embrace(
			    tmp.format(str(i), separator, str(j)), '{'))
	else:
		for i, j in d.items():
			ret = retTMP.format(ret, lineSeparator,
			                    tmp.format(str(i), separator, str(j)))
	return ret[1:]


def dic2Lists(dic) -> list:
	"""returns a tuple of two lists ([keys],[values])"""
	return list(dic.keys()), list(dic.values())

###***TextModifiers


def braces(boundBy):
    boundByL = ''
    boundByR = ''
    if not boundBy == '':
        if boundBy == '(' or boundBy == ')':
            boundByL = '('
            boundByR = ')'
        elif boundBy == '{' or boundBy == '}':
            boundByL = '{'
            boundByR = '}'
        elif boundBy == '{' or boundBy == '}':
            boundByL = '{'
            boundByR = '}'
        elif boundBy == '<' or boundBy == '>':
            boundByL = '<'
            boundByR = '>'
        elif boundBy == '[' or boundBy == ']':
            boundByL = '['
            boundByR = ']'
        else:
            boundByL = boundBy
            boundByR = boundBy

    return boundByL, boundByR


def embrace(content, boundBy, boundBy2=UNIN):
    ret = '{boundByL}{content}{boundByR}'
    if boundBy2 == UNIN:
        boundByL, boundByR = braces(boundBy)
    else:
        boundByL, boundByR = boundBy, boundBy2
    ret = ret.format(boundByL=boundByL, boundByR=boundByR, content=content)
    return ret
###Object Serilization


def save(content, name=UNIN, path=UNIN, extension=UNIN):
	"""
Save(content,extension,path,name) the 4th one can be combined into the third
"""
	namePattern = '{path}{name}{extension}'
	if isInitialized(name):
		tprint('initlized')
		name = namePattern.format(path=path, name=name, extension=extension)
		with open(name, "w") as f:
			f.write(content)
			return name
	else:
		inKey = {'delete': False, 'mode': 'w+t'}
		if isInitialized(extension):
		    inKey['suffix'] = extension
		if isInitialized(path):
		 inKey['dir'] = path
		else:
			inKey['dir'] = os.getcwd()
		tf = tempfile.NamedTemporaryFile(**inKey)
		tf.write(content)
		# tprint(content)
		tprint(tf.name)
		name = tf.name
		tf.close
		return name


def saveDic(dic, path=UNIN):
    if not isInitialized(path):
        path = 'cfg.dool'
    with open(path, 'w') as file:
        file.write(json.dumps(dic))


def loadDic(path=UNIN):
    if not isInitialized(path):
        path = 'cfg.dool'
    with open(path, 'r') as f:
        return json.loads(f.read())
###***Text input


def read(address, returnArray=False):
	try:
		with open(address, 'r', encoding='utf-8') as f:
			ret = f.read()
			if returnArray:
				return ret.split('\n')
			return ret
	except Exception as e:
		return str(e)

###Typing and Qualifiers


def getArrayDim(testlist, dim=0):
   """tests if testlist is a list and how many dimensions it has
   returns -1 if it is no list at all, 0 if list is empty
   and otherwise the dimensions of it"""
   if isinstance(testlist, list):
      if testlist == []:
          return dim
      dim = dim + 1
      dim = getArrayDim(testlist[0], dim)
      return dim
   else:
      if dim == 0:
          return -1
      else:
          return dim


def isUnin(obj):
    case = type(obj).__name__
    if case == 'str':
        return obj == UNIN
    elif case == 'list':
        UNIN in obj
    elif case == 'dict':
        return UNIN in list(obj.values())
    return False


def isInitialized(obj):
    return not isUnin(obj)


def getUserName():
    ret = pwd.getpwuid(os.geteuid()).pw_name
    #b=pwd.getpwuid( os.getuid() )[ 0 ]
    return ret


#######
####
#
# def nameSpace(
#     self, scope='instance', filter='public', deep=True, format="dict"
# ):
#     tempDic = {}
#     """ Scope section"""
#     if scope == 'instance':
#         scope = self
#     elif scope == 'class':
#         scope = type(self)
#
#     """Copy method matters if caller needs to update the source"""
#     if deep:
#         tempDic = copy.deepcopy(vars(scope))
#     else:
#         tempDic = copy.copy(vars(self))
#
#     """filter"""
#     retDic = {}
#     if filter == 'public':
#         f = filter(lambda e: not e[0].startswith('_'), tempDic.items())
#         retDic.update(dict(f))
#     elif filter == 'all':
#         retDic.update(tempDic)
#     """format"""
#     if format == 'keys':
#         retDic = retDic.keys()
#     elif format == 'values':
#         retDic = retDic.values()
#         return retDic
#     elif format == 'dict':
#         pass
#     return retDic
#
#     #     def getDic(self, all="easy", format='dict', copy="deep"):
#     #         """Returns attributes/property/etc
#     #         all=     easy:simple variables
#     #                 |instance: only instance level
#     #                 |all : everything
#     #                 |methods todo--> Return methods
#     #         format=  dict   : name-space-mapping
#     #                 |keys  : Variable names
#     #                 |items : list of key,value tuple
#     #                 |values
#     # """
#     #         dDic = {}
#     #         if copy == "deep":
#     #             dic = copy.deepcopy(vars(self))
#     #         else:
#     #             dic = vars(self)
#     #         if all == 'instance':
#     #             return self.__dict__
#     #         elif all == "easy":
#     #             for k, v in dic.items():
#     #               if not k.startswith('_'):
#     #                   dDic[k] = v
#     #               elif all == '__':
#     #                   for k, v in dic.items():
#     #               if k.startswith('__'):
#     #                   dDic[k] = v
#     #                   elif all == '_':
#     #               for k, v in dic.items():
#     #                   if not k.startswith('__') and k.startswith('_'):
#     #                       dDic[k] = v
#     #                   elif all == 'all':
#     #                       pass
#     #                   if format == 'dict':
#     #                   return dDic
#     #                   elif format == 'keys':
#     #                   return list(dDic.keys())
#     #                   elif format == 'items':
#     #                   return dDic.items()
#     #                   elif format == 'values':
#     #                   return list(dDic.values())
#
#     #
#     # import dis
#     # import inspect
#     # from dill.source import getsource
#     #
#     # def rossva(func):
#     #     def inner(*args, **kwargs):
#     #         print("")
#     #         print(func.__name__)
#     #         print(inspect.getsource(func))
#     #         print(inspect.getsourcelines(func))
#     #         print(dis.dis(func))
#     #         print( getsource(func))
#     #         return func(*args, **kwargs)
#     #     return inner
#     #
#     # def show(func):
#     #     def inner(*args,**kwargs):
#     #         print('This is the two separate args as inja hast',*args,*kwargs,'zortom')
#     #         print('This is kwargs',', '.join('%s=%s' % kv for kv in kwargs.items()))
#     #         return func(*args,**kwargs)
#     #     return inner
#     #
#     #
#     #
#     #
#     # # def digests(params):
#     # # 	""" takes the raw input sent from browser and turns into a dictionary fixing the shorthands
#     # # 	 fromat     {key}={value}"""
#     # # 	try:
#     # # 		pairs=params.split(',')
#     # # 		ret={}
#     # # 		for joft in pairs:
#     # # 			key,value=joft.split('=')
#     # # 			ret[key]=value
#     # # 	except Exception as e:
#     # # 		return str(e)
#     #
#     #
#     # #
#     # # def bechoogh(inP):
#     # # 	""" Convert input from dic to x=ZY,j=iu,...."""
#     # # 	res='{}={}'
#     # # 	ret=''
#     # # 	for key in inP:
#     # # 		ret='{},{}'.format(ret,res.format(key,inP[key]))
#     # # 	return ret[1:]
