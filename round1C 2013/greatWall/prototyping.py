'''
Created on May 27, 2013

@author: Yubin Bai
'''

from bintrees import RBTree

infinity = (1 << 33) - 1

if __name__ == "__main__":
    tree = RBTree()
    tree[infinity] = 0
    tree[-1 * infinity] = 0
    
    print(tree.floor_item(0))
    print(tree.ceiling_item(0))
