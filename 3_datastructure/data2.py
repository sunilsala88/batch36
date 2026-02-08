
d1={'tlsa':900,'amzn':600,'goog':390}

#access
print(d1['amzn']) #old

print(d1.get('amzn')) #new

#how to add new elem in dict

d1['nifty50']=800 #old
print(d1)

d1.update({'banknifty':908})
print(d1)

#update existing

d1['nifty50']=900 #old
print(d1)

d1.update({'banknifty':909})
print(d1)

#remove

d1.pop('amzn')
print(d1)

a=d1.popitem()
print(d1)
print(a)

del d1['goog']
print(d1)


#set
s2={44,55,66,55}
print(s2)
s2.add(77)
print(s2)


#string
s1='python'

s1=s1+'a'
print(s1)

s1.replace('p','')

print(s1[0])