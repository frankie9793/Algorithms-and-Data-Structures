def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    counter = 0
    while counter < k:
        second = second.next
        counter += 1
    #Handle removal of head node
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next

#Complexities: Time O(N) Space O(1)