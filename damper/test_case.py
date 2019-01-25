import numpy as np

class TestCase:
    '''
	a test case consisting of a set of values for c and a_c
	'''
	def __init__(self, sys, c_vals, a_vals):
		self.sys = sys
		self.c_vals = c_vals
		self.a_vals = a_vals
	def results(self):
		'''
		output results of test case as a matrix.
		rows represents values of a, columns values of c.
		'''
		def force_values():
			# map force ratio over values of c
			accum = []
			for c in self.c_vals:
				self.sys.damper.coef = c
				accum.append(self.sys.force_ratio())
			return accum
		# apply force_values for every values of a, concatenate to accumulator matrix.
		results = np.array([])
		for a in self.a_vals:
			self.sys.accel = a
			forces = np.array(force_values)
			results = np.concatenate(results, forces, axis = 0)
		return results
