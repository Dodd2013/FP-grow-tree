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
##参数说明 sample为事务数据集 []为递归过程中的基,support为最小支持度
support=3
ff=FP_Grow_tree.FP_Grow_tree(sample,[],support)
##打印频繁集
ff.printfrequent()