from time import *
import random as rd
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try :
            if partest[i]!= usertest[i]:
                 error += 1
        except :
            error += 1

    return error


def speed_time(time_s,time_e,userinput):
    time_delay = time_e -time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)





test = ["hello world","i am from india","i am a python coder"]
test1=rd.choice(test)

print("typing speed")
print(test1)
print()
print()
time_1 =time()
testinput = input("enter :")
time_2 = time()

print('speed :',speed_time(time_1,time_2,testinput) ,"word per second")
print('error :',mistake(test1,testinput))