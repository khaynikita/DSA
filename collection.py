from collections import Counter
a="aaaaaabbbbccc"
my_counter=Counter(a)
print(my_counter)
print(my_counter.items)   #Counter({'a': 6, 'b': 4, 'c': 3})
print(my_counter.keys)
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))