print ("Choose number of layers:")
y = int(input())
print ("Choose size of layers:")
z = int(input())
from termcolor import colored
print ((z*(y+1)+2)*' '+colored('/\\\n','green')+(z*(y+1)+1)*' '+colored('/..\\\n','green')+z*(y+1)*' '+colored('/.  .\\','green'))
for x in range(0,y):
    e = ''
    a = 0
    while a < z*2:
        e += colored('*','green')
        a += 1
        print ((z*(y-x+1)-a)*' '+colored('/. ','green')+(z*x*colored('*','green')+e)*2+colored(' .\\','green'))
print (((z*(y+1)+3)*2)*colored('-','green'))
t = max(0,(y+z)//2-3)
for w in range (0,y*z):
    print ((z*(y+1)+2-t)*' '+colored('|','red')+t*2*colored('*','red')+colored('|','red'))
