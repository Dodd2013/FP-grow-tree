import FP_Grow_tree
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
##参数说明 sample为事务数据集
ff=FP_Grow_tree.FP_Grow_tree(sample,[],3)
##打印频繁集
ff.f.tree.printfrequent()