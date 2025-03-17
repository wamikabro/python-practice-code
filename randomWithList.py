import random
pets = ['Dog', 'Cat', 'Moose']

print(random.choice(pets))

# indirectly it is 
# pets[random.randint(0, len(pets) - 1)]
# it means it will randomely select an index from 0 to the lenghth of the given list


# This function modifies the list in place, rather than returning a new list. 
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)