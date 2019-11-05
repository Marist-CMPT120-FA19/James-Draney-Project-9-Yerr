#James Draney Project 9
#james.draney1@marist.edu
#cmpt120L 200
#Letsrocktoday

def main(q):
    x=[]
    y=[]

    for i in range (2,q+1):
        if i not in x:
            y.append(i)

            for z in range(i*i,q+1,i):
                x.append(z)
    return y

q=int(input("Enter a number q: "))      
print(main(q))
      


main(q)
        
    
