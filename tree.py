__author__ = 'Dodd'
import unit
import fptree
class tree:
	frequent=[]
	def __init__(self,headnode,headtable):
		self.headnode=headnode
		self.headtable=headtable
		#tree.FP_growth(self.headnode,self.headtable,None)
		#tree.printTree(self.headnode)
		#tree.printheadtable(self.headtable)
		pass
	def printfrequent(self):
		print(tree.frequent)
	def FP_growth(self,headnode,headtable,a):
		if tree.checkTreeOneWay(headnode):
			tree.frequent+=list(unit.generateCombination(headtable,a))
			pass
		else:
			for item in headtable:
				#datas为条件模式基
				datas=unit.generateSubset(headtable,item)
				if datas:
					f=fptree.fptree(datas,3)
					f.fp_tree()
					f.tree=tree.tree(f.getRootTree(),f.headtable)
					f.tree.FP_growth(f.headnode,f.headtable,list(a)+list(item))
				pass
			pass
		pass
	def checkTreeOneWay(nodex):
		nodesx=nodex
		#print(nodesx)
		while nodesx:
			#print(nodesx)
			if len(nodesx.child)>1:
				return False
			if len(nodesx.child)>0:
				nodesx=nodesx.child[0]
			if len(nodesx.child)==0:
				break
			nodesx=nodesx.child[0]
		return True
	def printTree(node):
		if len(node.child)!=0:
			print(node.name+str(node.count))
			for nodes in node.child:
				tree.printTree(nodes)
				pass
		else:
			print(node.name+str(node.count))
		print('--------------')
	def printheadtable(headtable):
		print(headtable)
		for x in headtable:
			print(headtable[x])
			y=headtable[x]
			i=0
			print(x)
			while y.next:
				y=y.next
				print(y)
				i+=1
				pass
			print(i)
			pass