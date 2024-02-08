lis1=['sahar','aref','sAmaneh','ali']
lis2=['maman','baba','samaneh','sahar']
list1=[i.lower() for i in lis1]
list2=[i.lower() for i in lis2]
print(list1,list2)
mutualName=[name for name in list1 if name in list2]

print(mutualName)