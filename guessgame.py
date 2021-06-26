import sys        #for exiting purpose

print("Haii👋\nwelcome!")
print("What's up")
print("Let's start the game")
end = 0
ends = 0
kl = 0
h = -1
n = int(input("Enter the code between 1 to 15 : ")) #inputing the  code
print("ALERT🔔 :\n(Remember one thing You have only four chances):")
for k in range(2):
    if (n > 15 or n == 0):
        n = int(input("Please Enter the code  between 1 to 15 :!!!!? if not! we exit from the Game This last 2 Chance "))
        end  =  end + 1
        if(end == 2):
            print("your chance is execeed\nTry for the next time\nThank you 🤗\nStay Safe")
            sys.exit()    
       
   


for g in range(1,16): #setting the values
    if (n == g):         # Check whether value matches
        for j in range(n):
            h += 1     # Setting the hidden number
        break    
assumeno = h

for i in range(4):
    ends = ends + 1
    l = int(input("Guess the number: "))   #entering the guess number
   
    if (l > assumeno):     # Checking the conditions   
        print("your guess number is larger than the exact result")
    elif (l == assumeno):
        print("your guess number is correct\n\nCongratulation\nYou won the game")
        ends = ends - 1
        break
    else:
        print("Your guess number is lower than the exact result")
   
def endloop():    #if loss then print the definition below
    if(ends == 4):
        print("Sorry😔\nYou loss the game!!!\nYour chance is reached four times\nTry not to use too many chances\nThank you\nStay Safe")
       
endloop()
