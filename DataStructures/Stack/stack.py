from DataStructures.List import single_linked_list as sll
from DataStructures.List import list_node as ls
def new_stack():
    ns = {
        'size': 0,
        'first': None,
        'last': None
    }
    return ns

def push(my_stack, element):
    nn = ls.new_single_node(element)
    sll.add_first(my_stack, nn)
    return my_stack

def pop(my_stack):
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')
    else:
        removed = my_stack['first']
        sll.remove_first(my_stack)
        return removed
    
def is_empty(my_stack):
    return my_stack['size'] == 0

def top(my_stack):
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')
    else:
        return my_stack['first']

def size(my_stack):
    return my_stack['size']