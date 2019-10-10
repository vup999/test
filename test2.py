
name=['Zebra','Chris', 'Susan']
print(name)
print('The first object in list is :' + str(name[0]))
print('---------')
name.insert(1,'James')
name.insert(0,'8')
name.sort(reverse=1)
print(name)
print('there are ' + str(name.__len__()) + ' characters')
print()
print('Below is the first two :')
print(name[0:2])