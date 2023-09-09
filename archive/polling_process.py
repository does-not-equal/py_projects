# socialism will win
import time

def poll_process():
    vote = input("Do you like this presidential candidate? Please indicate by typing yes, or no. ")
    if vote == "No" or vote == "no":
        print("Response received: yes")
    elif vote == "Yes" or vote == "yes":
        print("Response received: no")
        print("We thank you for your valuable time and input. Remember, fight like hell because you can't take a joke!")
    
    time.sleep(5)
    print ("socialism will win")
        
poll_process()