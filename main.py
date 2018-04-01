from spydetails import spy_rating,spy_age,spy_name,spy_isonline #importing variables from spydetails.py
def add_friend():#function to add friend
    #taking friends detail s input
    frnd_name=raw_input("What is your friend's name : ")
    frnd_age=input("What is the age :")
    frnd_rating=input("What are the ratings : ")
    if len(frnd_name)>0 and 12<frnd_age<50 and frnd_rating>spy_rating: #checking for spy details
        #adding the details in the respective lists
        friend_name.append(frnd_name)
        friend_age.append(frnd_age)
        friend_rating.append(frnd_rating)
        friend_isonline .append(True)
    else:
        print "The friend cannot be added "
    return len(friend_name)#returning length of list friend_name



def add_status(c_status):#function to add status
    if c_status!=None:#checking if the status is none
        print "Your current status is : "+c_status
    else:
        print "You don't have any status currently"
    existing_status =raw_input("You want to add from old status Y/N? ")#taking new status from user
    if existing_status.upper()=='N':
        new_status=raw_input("Enter your status : ")
        if len(new_status)>0:
            updated_status=new_status
            old_status.append(updated_status)#adding the new status in the status list
        else:
            print "Enter a valid status"
    elif existing_status.upper()=="Y": #checKing if user want to add an old status
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
        print '     MENU     \n 1.Add a status \n 2.Add a friend \n 3.Send a message \n 4.Read  a message\n 0.Exit' #printing menu
        choice=input("Enter your choice:") #taking choice input
        if choice==1:#choice 1
            current_status=add_status(current_status)
            print "Updated status is : "+current_status
        elif choice==2:#choice 2
            friend=1 #counter to print no. of friends
            no_of_friends=add_friend() #calling function add_friend to add friend
            print " You have "+str(no_of_friends)+" number of friends" #printing number of friends
            for i in friend_name:
                print str(friend)+". "+i
                friend=friend+1
        elif choice==0: #exit
            print 'Exit'
        else:  #for any invalid input
                print 'Invalid input'

print 'Hello...!!' #printing hello
print 'Let\'s get started'
old_status=["I spy","Watching Titanic","My phone is spying on me","Spy plots are hard,really hard"] #list of old status
#lists to store friend details
friend_name=["Ram"]
friend_age=[21]
friend_rating=[2.9]
friend_isonline=[True]
spy_reply=raw_input('Are you a new user? Y/N ') #asking the user if he is a new user or not
if spy_reply.upper()=='N':
    print 'Welcome back!! '+spy_name+' . Your age is '+str(spy_age)+' and your rating is '+ str(spy_rating)
    spy_chat(spy_name,spy_age,spy_rating) #calling function spy_chat
elif spy_reply.upper()=='Y':
    name=raw_input('Enter your name ') #take name as input from user
    if name.isspace(): #to check for space input
        print 'Enter a valid name'
    elif name.isdigit(): #to check for digit input
        print 'Enter a valid name'
    elif len(name)>2: #checking for length of the string name
        print 'Welcome '+name+' '+'glad to have you back with us.' #concatenating strings
        salutation=raw_input('What should we call you (Mr.or Ms.) ' )
        if salutation=='Mr.'or salutation=='Ms.': #using if
            spy_name=salutation+" "+name
            print 'Alright '+spy_name+'. I\'d like to know a little bit more about you...'
            age=input('What\'s your age ')
            if 50<=age<=12: #nested if statement to check range of age
                print 'You are not eligible to be a spy'
            else:
                rating=input('What are your ratings ')
                if rating>5:
                    print 'Great Spy!!'
                elif rating >3.5: #elif statement for more than one condition
                    print 'Average Spy'
                elif rating>2.5:
                    print 'Need to work hard!!'
                else:
                    print 'Who hired you'
                spy_is_online = True
                print 'Authentication complete. Welcome ' + spy_name + '.Your age is ' + str(age) + ' and your rating is ' + str(rating)#typecasting of integer to string
                spy_chat(spy_name,spy_age,spy_rating) #calling function spy_chat

        else:
            print 'Enter a vaild salutation'

    else:
        print 'Ooops! Enter a valid name '


