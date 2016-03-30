from itertools import combinations
import tree
def generateCombination(headtable,a,support):
	lis=[]
	lisc=[]
	ans=[]
	
	base=str(",".join(str(i) for i in a))
	for x in headtable.keys():

		if(headtable[x].count>=support):
			lis.append(x)
			#y=[]
			#y.append(x)
			#lisc.append(y)
	lenlis=len(lis)
	for i in range(2,lenlis+1):
		lisc+=list(combinations(lis,i))
	#print(lisc)
	st=None
	for x in lisc:
		count=999
		st=base
		if x:
			for i in x:
				st=st+","+i
				count=min(count,headtable[i].count)
				pass
		if st:
			ans.append((st,count))
	return ans
def generateSubset(headtable,item,a,frequent):
	datas=[]
	node=headtable[item]
	while node:
		l=[]
		count=node.count
		lis=node
		while lis.parent.name!='null':
			#print(lis.parent.name)
			lis=lis.parent
			l.append(lis.name)
		node=node.next
		#y=a+l
		if len(l)>0:
			#frequent.append((",".join(str(i) for i in y),count))
			for x in range(0,count):
				datas.append(l)
				pass
	#print(item)
	#print(datas)
	return datas
	pass