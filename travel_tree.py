class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data ,end=' ')
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
    def in_order_traversal(self):
            def _in_order_traversal(root):
                if root is None:
                    pass
                else:
                    _in_order_traversal(root.left)
                    print(root.data,end=' ')
                    _in_order_traversal(root.right)
            _in_order_traversal(self.root)
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data,end=' ')
        _post_order_traversal(self.root)
    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data,end=' ')
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)
    
alpha = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BinarySearchTree()
for x in alpha:
    bst.insert(x)
bst.pre_order_traversal()  
print('')
bst.in_order_traversal()    
print('')
bst.post_order_traversal()  
print('')
bst.level_order_traversal() 
print('')




# def in_order_traversal(self):
#     def _in_order_traversal(root):
#         if root is None:
#             pass
#         else:
#             _in_order_traversal(root.left)
#             print(root.data,end=' ')
#             _in_order_traversal(root.right)
#         _in_order_traversal(self.root)

# 함수 호출 횟수 개선

# def in_order_traversal_revised(self):
#     def _in_order_traversal(root):
#         if root is None:
#             pass
#         else:
#             if root.left!=None:
#                 _in_order_traversal(root.left)
#             print(root.data,end=' ')
#             if root.right!=None:
#                 _in_order_traversal(root.right)
#         _in_order_traversal(self.root)