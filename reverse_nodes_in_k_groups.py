import random

# LINKED LIST IMPLEMENTATION AND HELPER FUNCTIONS #

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None
    
    # insert_node_at_head method will insert a LinkedListNode at 
    # head of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method. 
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result
    
def reverse_linked_list(head, k):
	previous, current, next = None, head, None
	for _ in range(k):
		# temporarily store the next node
		next = current.next
		# reverse the current node
		current.next = previous
		# before we move to the next node, point previous to the
        # current node
		previous = current
		# move to the next node 
		current = next
	return previous, current

def reverse_k_groups(head, k):

    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy
 

    while(ptr != None):

        tracker = ptr

        for i in range(k):

            if tracker == None:
                break
       
            tracker = tracker.next

        if tracker == None:
            break
    
        previous, current = reverse_linked_list(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next

def linked_list_to_list(linked_list_node):
    temp = linked_list_node
    output = []

    while temp:

        output.append(temp.data)
        
        temp = temp.next

    return output
    
# TEST CASE GENERATION STARTS HERE #

def generate_test_cases(N):

    test_cases = []

    # Helper function to check if an input (tuple) is already present in a list
    def not_present(lst, input):
        for i in lst:
            if i[0] == input[0] and i[1] == input[1]:
                return False
        return True
   
    # Helper function to generate a single test case
    def add_test_case(n, k):
        return ( [random.randint(1, 1000) for _ in range(n)] , k)
    
    # Category 1: n and k equal to 1
    counter = 0
    while counter < N:
        case = add_test_case(1, 1)
        if not_present(test_cases, case):
            test_cases.append(case)
            counter += 1

    # Category 2: n is greater than 1 and k equal to 1
    counter = 0
    while counter < N:
        n = random.randint(2, 500)
        case = add_test_case(n, 1)
        if not_present(test_cases, case):
            test_cases.append(case)
            counter += 1

    # Category 3: n is greater than or equals to k and is a multiple of k
    counter = 0
    while counter < N:
        k = random.randint(2, 499)
        n = random.randint(k, 500) 

        if n % k == 0:
            case = add_test_case(n, k)
            if not_present(test_cases, case):
                test_cases.append(case)
                counter += 1

    

    # Category 4: n is greater than k and is not a multiple of k
    counter = 0
    while counter < N:
        k = random.randint(2, 499)
        n = random.randint(k+1, 500) 

        if n % k != 0:
            case = add_test_case(n, k)
            if not_present(test_cases, case):
                test_cases.append(case)
                counter += 1

    # Public Test Cases

    # Category 1
    while True:
        case = add_test_case(1, 1)
        if not_present(test_cases, case):
            test_cases.append(case)
            break

    # Category 2
    while True:
        case = add_test_case(4, 1)
        if not_present(test_cases, case):
            test_cases.append(case)
            break

    # Category 3
    while True:
        case = add_test_case(6, 3)
        if not_present(test_cases, case):
            test_cases.append(case)
            break

    # Category 3 again
    while True:
        case = add_test_case(6, 2)
        if not_present(test_cases, case):
            test_cases.append(case)
            break

    # Category 4
    while True:
        case = add_test_case(7, 3)
        if not_present(test_cases, case):
            test_cases.append(case)
            break

    return test_cases

N = 20
data = generate_test_cases(N)

# Public Test Cases

with open( 'reverse_nodes_in_k_groups_public_test_cases.yaml', 'w') as file:
    file.write('testcases:\n')

    for idx, (lst, integer) in enumerate(data[-5:], start=1):

        # Reversing nodes in k groups

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lst)

        result = reverse_k_groups(input_linked_list.head, integer)

        output = linked_list_to_list(result)

        if idx == 1:

            file.write(f'  - name: "testcase {idx} - n and k equal to 1"\n')

        elif idx == 2:

            file.write(f'  - name: "testcase {idx} - n > 1 and k equals to 1 "\n')

        elif idx == 3:

            file.write(f'  - name: "testcase {idx} - n >= k and is a multiple of k"\n')

        elif idx == 4:

            file.write(f'  - name: "testcase {idx} - n >= k and is a multiple of k"\n')

        else:
            
            file.write(f'  - name: "testcase {idx} - n > k and is not a multiple of k"\n')

        file.write('    inputs:\n')
        file.write(f'      - 1: {lst}\n')
        file.write(f'      - 2: {integer}\n')
        file.write('    output:\n')
        file.write(f'      - 1: {output}\n')



# Private Test Cases
with open('reverse_nodes_in_k_groups_private_test_cases.yaml', 'w') as file:
    
    file.write('testcases:\n')

    # Loop over the data and format it into the desired YAML structure
    for idx, (lst, integer) in enumerate(data, start=1):

        # Reversing nodes in k groups

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lst)

        result = reverse_k_groups(input_linked_list.head, integer)

        output = linked_list_to_list(result)

        # Generating the YAML file

        if idx <= N:
            file.write(f'  - name: "testcase {idx} - n and k equal to 1"\n')

        elif idx > N and idx <= 2*N:
            file.write(f'  - name: "testcase {idx-N} - n > 1 and k equals to 1 "\n')

        elif idx > 2*N and idx <= 3*N:
            file.write(f'  - name: "testcase {idx-(2*N)} - n >= k and is a multiple of k"\n')

        elif idx > 3*N and idx <= 4*N:
            file.write(f'  - name: "testcase {idx-(3*N)} - n > k and is not a multiple of k"\n')

        else:
            file.write(f'  - name: "testcase {idx-(4*N)} - public testcases"\n')

        file.write('    inputs:\n')
        file.write(f'      - 1: {lst}\n')
        file.write(f'      - 2: {integer}\n')
        file.write('    output:\n')
        file.write(f'      - 1: {output}\n')



