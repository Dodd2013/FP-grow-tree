__author__ = 'Dodd'
import fptree
import tree

class FP_Grow_tree:
	def __init__(self,datas,a,support):
		self.f=fptree.fptree(datas,support)
		self.f.fp_tree()
		self.f.tree=tree.tree(self.f.getRootTree(),self.f.headtable,support,a)
		#print(a)
		self.f.tree.FP_growth(self.f.headnode,self.f.headtable)
		pass