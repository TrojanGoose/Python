import pyttsx3, time 


engine = pyttsx3.init() 
engine.say("Welcome to Autumn Bank")
engine.runAndWait()
Trials = 3
pincode = 0000

while Trials !=0:
    code = int(input("Please Enter your pincode: \n"))
    if code != pincode:
        Trials -=1
        if Trials != 0:
            print("You have", Trials, "tries left")
            engine.runAndWait()
        if Trials == 0:
            engine.say("You have exhausted your 3 trials, CONTACT YOUR BANK")
            engine.runAndWait()
            break
    else:
        options = input("W- Withdraw: \n")
        if options == "W":
            withdraw = input("How much do you want to withdraw: \n")
            print(withdraw,".00gh has been withdrawn successfully")

    closeApp = input("Do you want to perform another transaction Y/N \n")
    if closeApp != "Y":
        engine.say("It was nice banking with you.")
        engine.runAndWait()
        break

    else: 
        continue