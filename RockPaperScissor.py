import random
computer=0 
you=0
options=["rock","paper","scissor"]
while True:
    start= input("Type rock/paper/scissor to start or 'q' to quit ").lower()
    if start=="q":
        break
    if start not in options:
        continue
    else:
        randomno=random.randint(0,2)
        computerpick =options[randomno]
        print("computer chose", computerpick )
        if start=="rock" and computerpick=="scissor":
            print("YOU WON")
            you+=1
            print("yourscore :", you,"computer:",computer)
        elif start=="scissor" and computerpick=="paper":
            print("YOU WON")
            you+=1
            print("yourscore :", you,"computer:",computer)
        elif start=="paper" and computerpick=="rock":
            print("YOU WON")
            you+=1
            print("yourscore :", you,"computer:",computer)
        elif start==computerpick:
            print("TIE")
        else:
            print("COMPUTER WON")
            computer+=1
            print("yourscore :", you,"computer:",computer)
print("GOODBYE")
quit()
