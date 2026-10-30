import random
import os
choices=["rock","paper","scissors"]

player=input("Enter your choices : ")

other=random.choice(choices)

x=type(player)

print("Your choice was : ",player)
print("Other choice was : ",other)
print("Type of user data: ",x)

if(player==other):
 print("next times")
 
elif player=="rock" and other=="paper" :
 print("you fail : ")
 
elif player=="scissors" and other=="rock" :
 print("you fail : ")
 
elif player=="paper" and other=="scissors" :
 print("you fail : ")
 
else:
 print("You win")
 
folder_path=r"C:\Users\thoon\Desktop\ko"

file_path=os.path.join(folder_path)

print("Saved to : ",folder_path)




