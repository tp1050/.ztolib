# import sys
# sys.path.append('/home/c/PycharmProjects/lib')
from helper import getArrayDim, save as savefile
class TTable:
	tableStyle = '\n<style>\n\t table, th, td {   border:1px solid black; }\n </style>\n'
	patternTable = '\n<table style="width:100%">\n\t{}\n</table>\n'
	patternTR = '\n<tr> \n {}\n </tr>\n'
	patternTH = '\t<th> {} </th>\n'
	patternTD = '\t<td> {} </td>\n'

	def __init__(self, headers, sections):
		# helper.tprint(headers,sections)
		self.headers = headers
		self.sections = []
		self.addRows(sections)

	def addRow(self, row):
		if isinstance(row, tuple):
			row = list(row)
		if len(row) == len(self.headers):
			self.sections.append(row)
		else:
			raise Exception('Khiar> Table Column Count miss-match')

	def addRows(self, rows):
		dims = getArrayDim(rows)
		if dims == 2:
			for row in rows:
				self.addRow(row)
		elif dims == 1:
			self.addRow(rows)
		else:
			raise Exception('Khiar> Table Column Count miss-match dim big')

	def absorb(self, ttbl):
		if ttbl.headers == self.headers:
			for rows in ttbl.sections:
				self.addRows(rows)
		else:
			raise Exception('Khiar: Headers dont match')

	def html(self):
		p = []
		for h in self.headers:
			p.append(self.patternTH.format(h))
		heads = self.patternTR.format('\n'.join(p))
		vals = []
		p = []
		for rows in self.sections:
			for s in rows:
				p.append(self.patternTD.format(s))
			vals.append(self.patternTR.format('\n'.join(p)))
			p = []
		table = self.tableStyle + \
			self.patternTable.format('{}\n &nbsp; {}'.format(heads, ' '.join(vals)))
		return table

	def __repr_(self):
		return self.html()

	def __str__(self):
		return self.html()

	def save(self):
		"""         Save(content,extension,path,name) the 4th one can be combined into the third     """
		savefile(contnet=self.html())

class TTableI(TTable):
	def __init__(self, headers, sections):
		s = '<input type="text" id="fname" name="fname" value="{}">'
		self.patternTD = self.patternTD.format(s)
		print(self.patternTD)
		super().__init__(headers, sections)
		print(self.patternTD)

	def ihtml(self):
		h = self.html()
		hh = '<form action="/" method="POST" name="form"> \n {} <input id="submit" name="submit" type="submit" value="submit"> </form>'
		return hh.format(h)


class TTable2(TTable):
		from helper import UNIN,isUnin
		def __init__(self, headers, sections):
			self.inputPattern = '<input type="text" id={} name="{}" value="{}">'
			self.formPattern='<form action="/echo" method="POST" name="form"> \n {} <input id="submit" name="submit" type="submit" value="submit"> \n</form>'
			super().__init__(headers, sections)


		def html(self,editable=False,whichColEd=[],whichColEx=[]):
				from helper import UNIN,isUnin



				from helper import catalouge
				cat=catalouge(self.headers)
				p = []
				for h in self.headers:
					p.append(self.patternTH.format(h))
				heads = self.patternTR.format('\n'.join(p))
				vals = []
				p = []
				for rows in self.sections:
					colCounter=0
					for col in rows:
						if editable:
							item=cat[colCounter]
							print(item,((item in whichColEd) or ( item not in whichColEx)),whichColEx,col)
							if (item in whichColEd) or ( item not in whichColEx):
								newCol=self.inputPattern.format(item,item,col)

								col=newCol
							colCounter=colCounter+1
						p.append(self.patternTD.format(col))
					vals.append(self.patternTR.format('\n'.join(p)))
					p=[]
				table = self.tableStyle + self.patternTable.format('{}\n &nbsp; {}'.format(heads, ' '.join(vals)))
				if editable:
					table=self.formPattern.format(table)
				return table
