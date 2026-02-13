from DataStructures.List import single_linked_list as sll

def new_queue():
    nq = {
        'elements': sll.new_list(),
        'size': 0
    }
    return nq
def enqueue(my_queue, element):
    sll.add_last(my_queue['elements'], element)
    my_queue['size'] += 1
    return my_queue

def dequeue(my_queue):
    element = my_queue['elements']['first']
    sll.remove_first(my_queue['elements'])
    my_queue['size'] -= 1
    return element

def peek(my_queue):
    return sll.first_element(my_queue['elements'])

def size(my_queue):
    return my_queue['size']