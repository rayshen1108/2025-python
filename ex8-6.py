import array
a = array.array('i', [1, 2, 3, 4])
a = array.array('f', [1, 2, 3, 4])
#a = array.array("c" ,["1", "2", "3", "4"]) # wrong case

print(a)

print(a[0])

for item in a:
    print(item)
