spam = 42
cheese = spam
spam = 100
print(spam) # 100
print(cheese) # 42


# x----------------------x
spam = [0,1,2,3,4,5]
cheese = spam # The reference is being copied, not the list.

cheese[1] = 'Hello!' # This changes the list value.
print(spam) # that's why even spam got changes
# x----------------------x

