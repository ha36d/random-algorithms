'''
Trees: Convert binary tree to doubly linked list
'''

class BinaryTree(object):
    def __init__(self,val=0,right=None,left=None):
        self.val = val
        self.right = right
        self.left = left

class LinkedList(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
        
def create_linked_list(root):
    
    if (root == None):
        return None
    list1 = create_linked_list(root.left)
    list2 = create_linked_list(root.right)
    
    result = concat_linked_list(list1,LinkedList(root.val))
    return concat_linked_list(result,list2)


    
def concat_linked_list(list1,list2):
    
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1val = list1.val
        list1 = list1.next
        alist = concat_linked_list(list1,list2)
        mylist = LinkedList(list1val)
        mylist.next = alist
        return mylist
    else:
        list2val = list2.val
        list2 = list2.next
        alist = concat_linked_list(list1,list2)
        mylist = LinkedList(list2val)
        mylist.next = alist
        return mylist

def create_binary_tree(data,nodeList=None):
    bt = None
    
    
    while data != []:
        if nodeList is None:
            if data != []:
                bt = BinaryTree(data[0])
                nodeList = []
                nodeList.append(bt)
                data.pop(0)
        else:
            if data != []:
                nodeList[0].left = BinaryTree(data[0])
                data.pop(0)
                nodeList.append(nodeList[0].left)
            if data != []:
                nodeList[0].right = BinaryTree(data[0])
                data.pop(0)
                nodeList.append(nodeList[0].right)
            nodeList.pop(0)
        

    return bt
        
def main():
    
    data = [100,50,200,25,75,350]
    
    bt = create_binary_tree(data)
    
    print(bt.val)
    print(bt.left.val)
    print(bt.right.val)
    
    
    print("-----")

    linked_list = create_linked_list(bt)
    
    print(linked_list.val)
    print(linked_list.next.val)
    print(linked_list.next.next.val)
    print(linked_list.next.next.next.val)
    
    
    return linked_list

main()
