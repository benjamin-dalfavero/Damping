import numpy as np

class SysPlot:
	'''
	plot of a test case
	'''
	def __init__(self, test_case, name, labels):
		self.case = test_case
		self.name = name
		self.labels = labels
	def plot(self):
		'''
		plot test case
		'''
		# plot each row of results along with c values
		results = self.case.results()
		r, c = np.shape(results)
