print ("Choose number of layers:")
y = int(input())
print ("Choose size of layers:")
z = int(input())
print ((z*(y+1)+2)*' '+'/\\\n'+(z*(y+1)+1)*' '+'/..\\\n'+z*(y+1)*' '+'/.  .\\')
for x in range(0,y):
    e = ''
    a = 0
    while a < z*2:
        e += '*'
        a += 1
        print ((z*(y-x+1)-a)*' '+'/. '+(z*x*'*'+e)*2+' .\\')
print (((z*(y+1)+3)*2)*'-')
t = max(0,(y+z)//2-3)
for w in range (0,y*z):
    print ((z*(y+1)+2-t)*' '+'|'+t*2*'*'+'|')
