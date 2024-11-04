# Question: Merge two sorted linked lists into one sorted linked list.

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def merge(l1, l2):

    new_list = Node(0)
    temp = new_list

    while l1 and l2:
        
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next

    temp.next = l1 if l1 else l2
    return new_list.next

# Example usage
# Create two sorted linked lists
l1 = Node(1, Node(2, Node(4)))
l2 = Node(1, Node(3, Node(4)))
merged_list = merge(l1, l2)
# Print merged linked list
while merged_list:
    print(merged_list.val, end=' ')
    merged_list = merged_list.next  # Output: 1 1 2 3 4 4