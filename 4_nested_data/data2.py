
a={'tsla':500,'aapl':200}
# v=a['tsle']
v=a.get('tsle')
print(v)

b=None
print(type(a))