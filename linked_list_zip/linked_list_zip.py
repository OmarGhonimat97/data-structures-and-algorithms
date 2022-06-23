from code_challenge05.linked_list.linked_list import LinkedList, Node


# def zip_lists(ll1, ll2):
#
#     ll1.current = ll1.head
#     ll2.current = ll2.head
#
#     ll2.current.next = ll1.next
#     ll1.current.next = ll2.next
#
#     while ll1.current != None and ll2.current != None:
#
#         ll1.next = ll1.current.next
#         ll2.next = ll2.current.next
#
#         ll2.current.next = ll1.next
#         ll1.current.next = ll2.current
#
#         ll1.current = ll1.next
#         ll2.current = ll2.next
#         ll2.head = ll2.current

def zip_lists(ll1, ll2):

    current1 = ll1.head
    current2 = ll2.head
    while current1 != None and current2 != None:

        ll1.next = current1.next
        ll2.next = current2.next

        current2.next = ll1.next
        current1.next = current2

        current1 = ll1.next
        current2 = ll2.next
        ll2.head = current2
    return str(ll1)

# def zip_lists(l1, l2):
#     current1 = l1.head
#     current2 = l2.head
#     #result= current2
#     while current2:
#         if current1:
#           #  l1.insertBefore(current1.value, current2.value)
#             l1.insert_after(current1.value, current2.value)
#             current1 = current1.next.next
#             current2 = current2.next
#         else:
#             l1.append(current2.value)
#             current2 = current2.next


# def zip_lists(ll1, ll2):
#     current1 = ll1.head
#     current2 = ll2.head
#
#
#     while current2:
#
#         current1.next = current1.next.next
#         current2.next = current2.next.next
#
#         current2.next = current1.next
#         current1.next = current2.next
#
#         current1 = current1.next
#         current2 = current2.next
#         current2 = current2.next

if __name__ == '__main__':
    l_l_1 = LinkedList()
    l_l_2 = LinkedList()

    l_l_1.append(1)
    l_l_1.append(2)
    l_l_1.append(3)

    l_l_2.append(4)
    l_l_2.append(5)
    l_l_2.append(6)

    print(l_l_1)
    print(l_l_2)
    zip_lists(l_l_1, l_l_2)
    print(l_l_1)
    print(l_l_2)
