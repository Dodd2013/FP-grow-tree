import fptree
import tree
sample=[
    ['milk','eggs','bread','chips'],
    ['eggs','popcorn','chips','beer'],
    ['eggs','bread','chips'],
    ['milk','eggs','bread','popcorn','chips','beer'],
    ['milk','bread','beer'],
    ['eggs','bread','beer'],
    ['milk','bread','chips'],
    ['milk','eggs','bread','butter','chips'],
    ['milk','eggs','butter','chips']
]
f=fptree.fptree(sample,3)
f.fp_tree()
f.tree=tree.tree(f.getRootTree(),f.headtable)
f.tree.FP_growth(f.headnode,f.headtable,None)
f.tree.printfrequent()