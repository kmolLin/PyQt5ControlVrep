
import math
import vrep
import sys


def catch():                           # def catch button
    deg = math.pi/180

    vrep.simxFinish(-1)
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID!= -1:
        print("Connected to remote server")
    else:
        print('Connection not successful')
        sys.exit('Could not connect')

    errorCode,Catch=vrep.simxGetObjectHandle(clientID,'catch',vrep.simx_opmode_oneshot_wait)

    if errorCode == -1:
        print('Can not find Catch')
        sys.exit()
        
    errorCode=vrep.simxSetJointTargetPosition(clientID,Catch,0*deg, vrep.simx_opmode_oneshot)
        

def putoff():                              # def Put button
        deg = math.pi/180

        vrep.simxFinish(-1)
        clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
        if clientID!= -1:
            print("Connected to remote server")
        else:
            print('Connection not successful')
            sys.exit('Could not connect')

        errorCode,Catch=vrep.simxGetObjectHandle(clientID,'catch',vrep.simx_opmode_oneshot_wait)

        if errorCode == -1:
            print('Can not find Catch')
            sys.exit()            
       
    
        errorCode=vrep.simxSetJointTargetPosition(clientID,Catch,60*deg, vrep.simx_opmode_oneshot)
        
        
        
        
def couclate(x,y,z):
            L1 = 135.0
            L2 = 145.0
            a1x = 145.0
            a1y = 0.0

		#X ,Y= 0,0

		#x = -189.443
		#y = -58.074

		##Y theata


            theataRoateRad = math.acos((a1x*x+a1y*y)/(a1x*math.sqrt(x*x+y*y)))
            print(theataRoateRad)
            theataRoate = math.degrees(theataRoateRad)
            print(theataRoate)
            theate = float((x*x+z*z-L1*L1-L2*L2)/(2*L1*L2))

            print(theate)
            rad = math.acos(theate)
            print(rad)
            tha = math.degrees(rad)

	    	#tha為算出來的角度

            print("算出來的",tha)


		#thn = arcos(x/(sqrt(x^2+y^2)))
		#tha = (x^2+y^2+L1^2+L2^2)/(2(sqrt(x^2+y^2)*L1))

            theatanr = math.acos(x/(math.sqrt(x*x+z*z)))
            theatan = math.degrees(theatanr)
            #theataN的角度
            print("theatan角度",theatan)
            theatalphar = math.acos((x*x+z*z+L1*L1-L2*L2)/(2*math.sqrt(x*x+z*z)*L1))

            theatalpha = math.degrees(theatalphar)
            #theatAlpha的角度
            print("theatalpha角度",theatalpha)

        #theata2 = theatan + theatAlpha
            
            test2 = theatan+theatalpha
            theata2 = 90-test2
            print("theata2",theata2)
        #theata3 = tha - theata2
            theata3 = tha - test2

            print("theata3",theata3)
            return(theata2,theataRoate,theata3)


def moveMachineHand(a, b, c):
    deg = math.pi/180
    vrep.simxFinish(-1)
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID!= -1:
        print("Connected to remote server")
    else:
        print('Connection not successful')
        sys.exit('Could not connect')

    errorCode1,Joint1=vrep.simxGetObjectHandle(clientID,'joint1',vrep.simx_opmode_oneshot_wait)
    errorCode2,Joint2=vrep.simxGetObjectHandle(clientID,'joint2',vrep.simx_opmode_oneshot_wait)
    errorCode3,Joint3=vrep.simxGetObjectHandle(clientID,'joint3',vrep.simx_opmode_oneshot_wait)


    if errorCode1 == -1:
        print('Can not find joint1')
        sys.exit()            
    if errorCode2 == -1:
        print('Can not find joint2')
        sys.exit()            
    if errorCode3 == -1:
        print('Can not find joint3')
        sys.exit()            
        

    
    errorCode1=vrep.simxSetJointTargetPosition(clientID,Joint2,a*deg, vrep.simx_opmode_oneshot)
    errorCode2=vrep.simxSetJointTargetPosition(clientID,Joint1,b*deg, vrep.simx_opmode_oneshot)
    errorCode3=vrep.simxSetJointTargetPosition(clientID,Joint3,c*deg, vrep.simx_opmode_oneshot)

    print("answer=",a,b,c)
        
