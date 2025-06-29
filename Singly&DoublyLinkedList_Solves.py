# -*- coding: utf-8 -*-
"""CSE220_Lab Assignment 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q5fSZRj1_OlwWD2qUEdDMLGraiD1zryM

1.   Be careful in which question you are required to change the given Linked list and where you are required to create a new one
2.   Be careful of the first node and the last node [aka corner cases]
3.   Do not use any other data structure other than Linked List

**You must run this cell to install dependency**
"""

! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

"""**You must Run this cell for your driver code to execute successfully**"""

#Run this cell
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()



"""Task 1: Building Blocks"""

def check_similar(building_1, building_2):
    flag = True

    while building_1 and building_2:
        if building_1.elem!=building_2.elem:
            flag = False
        building_1 = building_1.next
        building_2 = building_2.next
    if building_1 or building_2:
        flag = False

    if flag:
        return "Similar"
    else:
        return "Not Similar"


  #TO DO



print('==============Test Case 1=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Similar'
unittest.output_test(returned_value, 'Similar')
print()

print('==============Test Case 2=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 3=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 4=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

"""Task 2: Remove Compartment"""

def remove_compartment(head,n):
    count = 0
    temp = head

    while temp:
        count += 1
        temp = temp.next
    if n>count:
        return head
    if n==count:
        return head.next
    if n<count:
        temp = head
        for i in range(count-1-n):
            temp = temp.next
        temp.next = temp.next.next
    return head

  #TO DO


print('==============Test Case 1=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,2)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->72
print()
print('==============Test Case 2=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,7)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72
print()
print('==============Test Case 3=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,6)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 15-->34-->41-->56-->72
print()

"""Task 3: Assemble Conga Line"""

def assemble_conga_line(conga_line):
    temp = conga_line

    while temp.next:
        if temp.next.elem<temp.elem:
            return False
        temp = temp.next
    return True

  #TO DO


print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print True
unittest.output_test(returned_value, True)
print()
print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,44,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print False
unittest.output_test(returned_value, False)
print()

"""Task 4: Word Decoder"""

def word_Decoder(head):
    count  = 0
    num = 0
    temp = head
    while temp != None:
        count += 1
        temp = temp.next
    x = 13 % count
    temp = head
    new_head = None
    for i in range(count):
        if i%x==0 and i!=0:
            n = Node(temp.elem, new_head)
            new_head = n
        temp = temp.next
    result = Node(None, new_head)

    return result





#Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N

"""Task 5: Alternate Merge"""

def alternate_merge(head1, head2):
    new = Node(head1.elem, head2)
    temp = new.next
    head1 = head1.next
    head2 = head2.next
    while head1 and head2:
        temp.next = head1
        head1 = head1.next
        temp = temp.next
        temp.next = head2
        head2 = head2.next
        temp = temp.next
    return new






  #TO DO


print('==============Test Case 1=============')
head1 = createList(np.array([1,2,6,8,11]))
head2 = createList(np.array([5,7,3,9,4]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4


print('==============Test Case 2=============')
head1 = createList(np.array([5, 3, 2, -4]))
head2 = createList(np.array([-4, -6, 1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    5 → -4 -> 3 → -6 -> 2 -> 1 -> -4


print('==============Test Case 3=============')
head1 = createList(np.array([4, 2, -2, -4]))
head2 = createList(np.array([8, 6, 5, -3]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3

"""Task 6: Sum of Nodes"""

def sum_dist(head, arr):
    l = 0
    add = 0
    temp = head
    while temp != None:
        l += 1
        temp = temp.next

    for i in range(len(arr)):
        temp = head
        count = 0
        if arr[i]>l:
            add += 0
        elif arr[i]<l:
            while count<arr[i]:
                temp = temp.next
                count += 1
            add += temp.elem

    return add


  #TO DO



print('==============Test Case 1=============')
LL1 = createList(np.array([10,16,-5,9,3,4]))
dist = np.array([2,0,5,2,8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4
unittest.output_test(returned_value, 4)
print()

"""Bonus Task: ID Generator"""

def idGenerator(head1, head2, head3):
    temp1 = head1
    temp2 = head2
    temp3 = head3
    add = 0
    new = Node(None)
    while temp1:
        n = Node(temp1.elem, new)
        new = n
        temp1 = temp1.next

    # temp1 = new
    # for i in range(5):
    #     if temp1.next==None:
    #         while temp2 and temp3:
    #             if (temp2.elem + temp3.elem)<10:
    #                 temp1.next = Node(temp2.elem + temp3.elem, None)
    #             elif (temp2.elem + temp3.elem)>=10:
    #                 temp1.next = Node((temp2.elem + temp3.elem)%10, None)
    #             temp2 = temp2.next
    #             temp3 = temp3.next
    #     temp1 = temp1.next

    return new


  #TO DO


print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5