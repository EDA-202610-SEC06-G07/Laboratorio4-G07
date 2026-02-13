from DataStructures.List import single_linked_list as sll

def new_queue():
    nq = {
        'elements': None,
        'size': 0
    }
    return nq
def enqueue(my_queue, element):
    return my_queue['elements'].sll.add_last(element)

def dequeue(my_queue):
    element = my_queue['elements']['first']
    my_queue['elements'].sll.remove_first()
    return element

def peek():
    pass

def size(my_queue):
    return my_queue['size']