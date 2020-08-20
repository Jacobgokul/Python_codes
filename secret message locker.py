import random
pwdlen = random.randint(4,10)
print("Secert message locker")

def pwdcheck():
    global pwd
    pwd = input('Enter according to lenght '+ str(pwdlen) +': ')
    
    if len(pwd) == pwdlen:
        print('Message')
        display()
    else:
        print('no, enter specified length')
        pwdcheck()
 
def display():
    print('looking for an message')
    global  passcode
    passcode = input('enter password: ')
    messagecheck()    
   
def messagecheck():
     if passcode == pwd:
         displaymsg()
     else:
         print('Wrong password')
         wrong()
         
def wrong():
    print('Only 2 chance, enter crt passwod')
    global n
    n = 2
    while(n > 0):
        n -= 1
        passcode = input('Enter msg '+ str(n) +' time left: ')
        if passcode == pwd:
            displaymsg()
            break
    else:
        print('message deleted')
        print(msg.replace(msg,'none'))
            

def getmsg():
    global msg
    msg = input('leave message: ')

def displaymsg():
    print(msg)

getmsg()
pwdcheck()