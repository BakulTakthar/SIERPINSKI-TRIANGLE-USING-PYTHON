import random as ran

import matplotlib.pyplot as mpt

pointA = (0,0)
pointB = (3,3)
pointC = (0,4.242640687)
pointALPHA = (1,2)

def plotting(number):
    
    mpt.scatter(0,0)
    mpt.scatter(3,0)
    mpt.scatter(1.5, 3)
    mpt.scatter(1.4,1) #alpha point
    
    
    Ax = 0 
    Ay = 0
    
    Bx = 3
    By = 0
    
    Cx = 1.5 
    Cy = 3
    
    AlphaX = 1.4
    AlphaY = 1
    
    for i in range(0, number):
        
        randvalue = ran.randrange(0,3)
        
        
        if randvalue == 0: # point A
            cordiX = (AlphaX + Ax)/2
            cordiY = (AlphaY + Ay)/2
            
            mpt.scatter(cordiX, cordiY, color = 'black', s = 1)
            
           # print(cordiX,',', cordiY)
            
            
        elif randvalue == 1: # point B
            cordiX = (AlphaX + Bx)/2
            cordiY = (AlphaY + By)/2
            
            mpt.scatter(cordiX, cordiY, color = 'black', s = 1) 
            
           # print(cordiX,',' ,cordiY)
            
            
        elif randvalue == 2: # point A','
            cordiX = (AlphaX + Cx)/2
            cordiY = (AlphaY + Cy)/2
            
            
            mpt.scatter(cordiX, cordiY, color = 'black', s = 1)
            
           # print(cordiX,',' ,cordiY)
            
            
        else:
            pass
    
        AlphaX = cordiX
        AlphaY = cordiY
    
    print("the code ran")
    
    mpt.show()
    
plotting(int(input("no. of plots >>>")))