num_elements = int(input("Enter the number of elements: "))
elements = input("Enter the elements ").split('-')
elements = [int(x) for x in elements]
elements_to_insert = int(input("Enter the element to be inserted: "))
position = int(input("Position: "))
elements.insert(position - 1, element_to_be_inserted)
print(elements)
