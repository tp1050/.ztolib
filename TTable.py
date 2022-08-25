import sys
sys.path.append('/home/c/PycharmProjects/lib')
from helper import tprint,getArrayDim,save
class TTable:
	tableStyle='\n<style>\n\t table, th, td {   border:1px solid black; }\n </style>\n'
	patternTable='\n<table style="width:100%">\n\t{}\n</table>\n'
	patternTR='\n<tr> \n {}\n </tr>\n'
	patternTH='\t<th> {} </th>\n'
	patternTD='\t<td> {} </td>\n'


	def __init__(self,headers,sections):
		# helper.tprint(headers,sections)
		self.headers=headers
		self.sections=[]
		self.addRows(sections)

	def addRow(self,row):
		if len(row)==len(self.headers):
			self.sections.append(row)
		else: raise Exception('Khiar> Table Column Count miss-match')
	def addRows(self,rows):
		dims=getArrayDim(rows)
		if dims==2:
			for row in rows:
				self.addRow(row)
		elif dims==1:
			self.addRow(rows)
		else: raise Exception('Khiar> Table Column Count miss-match')
	def absorb(self,ttbl):
		if ttbl.headers==self.headers:
			for rows in ttbl.sections:
				self.addRows(rows)
		else:raise Exception('Khiar: Headers dont match')
	def html(self):
		p=[]
		for h in self.headers:
			p.append(self.patternTH.format(h))
		heads=self.patternTR.format('\n'.join(p))
		vals=[]
		p=[]
		for rows in self.sections:
			for s in rows:
				p.append(self.patternTD.format(s))
			vals.append(self.patternTR.format('\n'.join(p)))
			p=[]
		table=self.tableStyle+self.patternTable.format('{}\n &nbsp; {}'.format(heads,' '.join(vals)))
		return table
	def __repr_(self):
		return self.html()
	def __str__(self):
		return self.html()
	def save(self):
		"""         Save(content,extension,path,name) the 4th one can be combined into the third     """
		save(contnet=self.html())
