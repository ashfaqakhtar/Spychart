from spydetails import spy #importing variables from spydetails.py
from steganography.steganography import Steganography #importing Steganography library
from datetime import datetime #impoeting datetime library
def select_frnd():#function to select a friend
    print"Select your friend"
    serial_no=1
    for frnd in friends:#print list of friends
        print str(serial_no)+". "+ frnd['name']
        serial_no=serial_no+1
    user_selected_frnd=input("Enter your choice: ")#user selecting friend
    user_selected_frnd_index=user_selected_frnd-1
    return user_selected_frnd_index #to return the selected friend index
def send_message():# functon for sending message
    selected_friend = select_frnd()#calling the select_friend function
    original_image=raw_input("What is the name of original image : ")#take name of original image as input
    secret_text=raw_input("Enter your secret message : ")#entering the secret message
    output_path="output.jpg" #name of image after encoding the message
    Steganography.encode(original_image,output_path,secret_text)#calling encode() function to encode message in image
    print "Message Encoded"
    #dictonary to store details of a message
    new_chat={"message":secret_text,
              "time":datetime.now(),
              "send by me": True}
    friends[selected_friend]['chats'],append(new_chat)#appending ghats in the friends list
    print "Your secret message is ready"

def read_message():#function for reading message
    selected_friend=select_frnd() #calling select_friend function
    output_path=raw_input("Which image you want to decode? ")#the name of image to be decoded
    secret_text=Steganography.decode(output_path)#calling decode()function to decode
    print "The decoded message is "+secret_text #printing the secret text
    #dictionary to store details of message
    new_chat = {"message": secret_text,
                "time": datetime.now(),
                "send by me": False}
    friends[selected_friend]['chats'].append(new_chat)
def add_friend():#function to add friend
    #taking friends detail s input
    frnd={'name':"",
          'age':0,
          'ratings':0.0,
          'isonline':True,
          'chats':[]}#dictionary for details of friend
    frnd['name']=raw_input("What is your friend's name : ")
    frnd['age']=input("What is the age :")
    frnd['rating']=input("What are the ratings : ")
    if len(frnd['name'])>0 and 12<frnd['age']<50 and frnd['rating']>spy['rating']: #checking for spy details
        #adding the details in the respective lists
        friends.append(frnd)#appending friend details in friends list
    else:
        print "The friend cannot be added "
    return len(friends)#returning length of list friend_name

def add_status(c_status):#function to add status
    if c_status!=None:#checking if the status is none
        print "Your current status is : "+c_status #printing the current status
    else:
        print "You don't have any status currently"
    existing_status =raw_input("You want to add from old status Y/N? ")#taking new status from user
    if existing_status.upper()=='N':
        new_status=raw_input("Enter your status : ") #taking new status as input
        if len(new_status)>0:
            updated_status=new_status
            old_status.append(updated_status)#adding the new status in the status list
        else:
            print "Enter a valid status"
    elif existing_status.upper()=="Y": #checking if user want to add an old status
        serial_no=1
        for status in old_status:#printing the old status
            print str(serial_no)+". "+status
            serial_no=serial_no+1
        status_choice=input("Enter your choice : ")
        updated_status=old_status[status_choice-1] #updating the status
    return updated_status #returning the new updated status


def spy_chat(spy_name,spy_age,spy_rating): #function spy_chat to display menu
    current_status=None
    choice= -1 #choice variable set to -1
    print 'Here are your options ' + spy_name
    while choice!=0: #while loop will run until user choose to exit
        print '     MENU     \n 1.Add a status \n 2.Add a friend \n 3.Send a message \n 4.Read  a message\n 5.Read chats from a user \n 0.Exit' #printing menu
        choice=input("Enter your choice:") #taking choice input
        if choice==1:#choice 1
            current_status=add_status(current_status)
            print "Updated status is : "+current_status
        elif choice==2:#choice 2
            friend_no=1 #counter to print no. of friends
            no_of_friends=add_friend() #calling function add_friend to add friend
            print " You have "+str(no_of_friends)+" number of friends" #printing number of friends
            for i in friends: #printing name of friends
                print str(friend_no)+". "+i['name']
                friend_no=friend_no+1
        elif choice==3:
            send_message() #calling send_message()function
        elif choice==4:
            read_message()#calling the read_message()function
        elif choice==5: #to read a user,s message
            print "will read a user's message"
        elif choice==0: #exit
            print 'Exit'
        else:  #for any invalid input
                print 'Invalid input'

f=datetime.now() #calling function now() from datetime library
print f.strftime("%b %d %Y %H:%M:%S")#use of stringtimeformat
print 'Hello...!! Welcome to SPYCHAT.' #printing hello
print 'Let\'s get started'
old_status=["stay away","who are you","Gangadhar hi Shaktiman hai"] #list of old status
friends=[{'name':'Shahid','age':20,'rating':3.6,'isonline':True,'chats':[]},{'name':'Aanjal','age':21,'ratings':2.4,'isonline':True,'chats':[]}]#list to store friend details
spy_reply=raw_input('Are you a new user? Y/N ') #asking the user if he is a new user or not
if spy_reply.upper()=='N':
    print 'Welcome back!! '+spy['name']+" age is "+str(spy['age'])+' and your rating is '+ str(spy['rating'])
    spy_chat(spy['name'],spy['age'],spy['rating']) #calling function spy_chat
elif spy_reply.upper()=='Y':
    spy={'name':"",'age':0,'rating':0.0}#dictionary to store spy details
    spy['name']=raw_input('Enter your name ') #take name as input from user
    if spy['name'].isspace(): #to check for space input
        print 'Enter a valid name'
    elif spy['name'].isdigit(): #to check for digit input
        print 'Enter a valid name'
    elif len(name)>2: #checking for length of the string name
        print 'Welcome '+spy['name']+' '+'glad to have you back with us.' #concatenating strings
        salutation=raw_input('What should we call you (Mr.or Ms.) ' )
        if salutation=='Mr.'or salutation=='Ms.': #using if
            spy_name=salutation+" "+spy['name']
            print 'Alright '+spy_name+'. I\'d like to know a little bit more about you...'
            spy['age']=input('What\'s your age ')
            if 50<=spy['age']<=12: #nested if statement to check range of age
                print 'You are not eligible to be a spy'
            else:
                spy['rating']=input('What are your ratings ') #taking ratings as input
                if spy['rating']>5:
                    print 'Great Spy!!'
                elif spy['rating'] >3.5: #elif statement for more than one condition
                    print 'Average Spy'
                elif spy['rating']>2.5:
                    print 'Need to work hard!!'
                else:
                    print 'Who hired you'
                spy_is_online = True
                print 'Authentication complete. Welcome ' + spy['name'] + '.Your age is ' + str(spy['age']) + ' and your rating is ' + str(spy['rating'])#typecasting of integer to string
                spy_chat(spy['name'],spy['age'],spy['rating']) #calling function spy_chat

        else:
            print 'Enter a vaild salutation'

    else:
        print 'Ooops! Enter a valid name '