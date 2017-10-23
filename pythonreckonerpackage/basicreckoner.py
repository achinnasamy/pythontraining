import random
import sys
import os
print("hello world")
print('first python program')
#firstprogram
'''
to
print
helloworld'''
name="Dharshekth Vel"
print(name)

value="hello"
print(value)

number=12345
print(number)

data=';eytrye'
print(data)
name=12345
print(name)

print("3+2:",3+2)
print("3-2:",3-2)
print("3*2",3*2)
print("5/2:",5/2)
print("3%3:",3%3)
print("3**2:",3**2)
print("17//6):",17//6)


v_1='string val'
print(v_1)
print('\n'*5)


new_list=['one',"two",'three','four','five']
print(new_list[0])
print(new_list[1])
new_list[0]="oneee"

print(new_list[0])

#print subset
print(new_list[1:3])


# john von neumann
# richard feynman
# neils bohr
# arya bhatta
#


# denis ritchie
# tree, graph, map, hashmap, dictionary, associative array
second_list=['six','seven','eight','nine']

#list within a list
final_list=[new_list,second_list]
print(final_list)

print(final_list[1][2])

new_list.append('ten')
print(new_list)

print(final_list)


new_list.insert(2,"eleven")
print(new_list)

new_list.remove("ten")
print(new_list)

new_list.sort()
print(new_list)

new_list.reverse()
print(new_list)

new_list.append("twelve")

new_list.reverse()
print(new_list)

del new_list[2]
print(new_list)

list_len=new_list+second_list
print(list_len)

print(len(list_len))

print(max(list_len))


list_numbers=[1,5,4,6,10]
list_numbers2=[9,2,11,3]
print("\n"*10)
print(list_numbers)
list_numappend=list_numbers+list_numbers2
print(list_numappend)
list_numappend.sort()
print(list_numappend)





#tuples
new_tuple=(1,5,3)
print(new_tuple)

second_tuple=list(new_tuple)
second_tuple.insert(1,9)
print(second_tuple)
final_tuple=tuple(second_tuple)
print(final_tuple)

#dictionary
new_dict={'a':'apple','b':'banana','c':'cucumber'}
print(new_dict['b'])
del new_dict['c']
new_dict['a']='apricot'
print(new_dict)
print(len(new_dict))
print(new_dict.get('a'))
print(new_dict.keys())
print(new_dict.values())


#dictionary 2
new_dict={'C':'Dennis Ritchie','Java':'James Gosling','C++':'Bjarne Stroustrup'}
print(new_dict)

print(new_dict['Java'])
del new_dict['C']
print(new_dict)
new_dict['Java']='Gosling'
print(new_dict)
print(len(new_dict))

print(new_dict.get('C++'))
print(new_dict.keys())
print(new_dict.values())
print(max(new_dict))
print(min(new_dict))
print(min(new_dict.values()))
print(min(new_dict.keys()))
print(max(new_dict.values()))
print(max(new_dict.keys()))


#if else
age=40
if age<58:
    print("You still have years to work")
else:
    print("You are eligible for retirement ")

#if elif else


#for
for x in range(0,10):
    '''
    not working
    print(x, ' ' , end=' ')'''



#function
def addnumbers(num1,num2):
    sumnum=num1+num2
    return sumnum

print(addnumbers(5,4))


#user i/p
'''
print("Enter a ds name")
name=sys.stdin.readline()
if name=="array" or name=="stack" or name=="queue":
    print(name,' is a linear ds')
elif name=="linked list" or name=="trees" or name=="graphs" :
    print(name,'is a non-linear ds')
else:
    print(name,'is invalid')

'''

print("Enter name")
name=sys.stdin.readline()
print("hello",name)



#strings

new_string="Ada was the first programmer"
print(new_string[0:3])
print(new_string[-10:])
print(new_string[:-10])
print(len(new_string))
print(new_string[:4],"was a computer programmer")

