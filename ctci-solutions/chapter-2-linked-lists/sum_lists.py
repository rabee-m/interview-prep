#Cracking the Coding Interiew pg 95 2.5
"""
Prompt: You have two numbers repersented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
e.g.) 7 -> 1 -> 6 + 5 -> 9-> 2 is 617 + 295 and output is 2 -> 1 -> 9
"""

class LinkedList:
    def __init__(self, data):
        self.value = data
        self.next = None

def sum_lists_reverse(llist1, llist2):
    currNode1 = llist1
    currNode2 = llist2
    carryOver = 0
    sum_llist = None
    while (currNode1 is not None and currNode2 is not None):
        #null nodes have value 0
        valNode1 = currNode1.value if currNode1 is not None else 0
        valNode2 = currNode2.value if currNode2 is not None else 0

        valNewNode = (valNode1 + valNode2 + carryOver) % 10 
        carryOver = (valNode1 + valNode2) // 10
        NewNode = LinkedList(valNewNode)
        if sum_llist is None:
            sum_llist = NewNode
        else:
            sum_llist.next = NewNode
        
        #update nodes
        currNode1 = currNode1.next if currNode else None
        currNode2 = currNode2.next if currNode else None
    
    return sum_llist

#Add forward sum implementation
#e.g.) Adding 6 -> 1 -> 7 + 2 -> 9 -> 5 = 9 -> 1 -> 2 (617 + 295)


#Things to do
#Find the larger number and add zero padding to the front until lengths match
#Store the previous node and add carryOvers directly to it
#TODO: Not finished
def sum_list_forward(llist1, llist2):
    #Get length of list1 and list2
    lenList1 = 0
    currNode = llist1
    while(llist1):
        lenList1 += 1
        llist1 = llist1.next
    lenList2 = 0
    currNode = llist2
    while(llist2):
        llist2 += 1
        llist2 = llist2.next
    
    smallerList = llist2 if lenList1 > lenList2 else llist1
    lengthDiff = lenList2 - lenList1
    #Add zero padding to smaller list
    # 1-> 2 -> 3
    # 0-> 1-> 2-> 3
    while(lengthDiff != 0):
        zeroNode = LinkedList(0)
        zeroNode.next = smallerList
        smallerList = zeroNode
        lengthDiff -= 1
    
    currNode1 = llist1
    currNode2 = llist2
    sumllist = LinkedList(0)
    prevSumllistNode = sumllist
    while (currNode1 is not None and currNode2 is not None):
        sumVal = currNode1 + currNode2
        carryOver = sumVal % 10
        prevSumllistNode.value += carryOver

