import copy
# shallow copy function to use copy we need import copy module
l1 = [1,3,6,8.9,[10,20,30],"Python"]
l2 = copy.copy(l1)
print(f"l1 = {l1}",id(l1))
print(f"l2 = {l2}",id(l2))
l1[0] = 11
print(f"l1 = {l1}",id(l1))
print(f"l2 = {l2}",id(l2))
l2[4][0] = 50 # when inner list are modified in shallow copy both the list will be updated other changes will not be updated
print(f"l1 = {l1}",id(l1))
print(f"l2 = {l2}",id(l2))
# deep copy
print('########################################')
l3 = [1,3,4.5,[10,20,30],"Python"]
l4 = copy.deepcopy(l3)
l3[2] = 5
l3[3][2] = 40
print(f"l3 = {l3}", id(l3))
print(f"l4 = {l4}", id(l4)) # any chnages made in 1 list doesn't reflect in 2nd list unlike shallow copy
print('########################################')
d1 =  {'id':2, 'name':'Sivansh', 'marks':{'eng':89,'sic':90,'math':85.5}}
d2 = copy.deepcopy(d1)
d1['name'] = 'Surya'
d1['marks']['math'] = 90
print(f"d1 = {d1}",id(d1))
print(f"d2 = {d2}",id(d2))
