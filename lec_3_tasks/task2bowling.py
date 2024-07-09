import random
from bowlinggameart import logo
is_running=True
max_score=30
def roll():
    ball=[0,1,2,3,4,5,6,7,8,9,10]
    x=int(random.choice(ball))
    return x        
scores=[0,0]

while max(scores)<max_score and is_running==True:
    print(logo)
    chance=2
    comp_chance=2
    remaining=10
    while chance!=0:
        choice=input("Do you want to bowl? Type 'y' for yes or 'exit' to exit:").lower()
        if choice=='y':
            bowl = roll()
            if remaining >= bowl:
                remaining-=bowl
                if bowl==10:
                    print("Its a strike!!")
                    scores[0]+=bowl
                    break     
                elif remaining==0 and chance==1 and bowl!=10:
                    print("Its a spare, good going.")
                    scores[0]+=bowl
                    break
                elif bowl!=10 and bowl!=0 and remaining!=0:
                    scores[0]+=bowl
                    chance-=1
                    print(f"You dropped {bowl} pins.Remaining pins are:{remaining}")        
                elif bowl==0:
                    print("It is a guttergame by you.")
                    chance-=1
            else:
                print(f"Invalid bowl, you can't knock down {bowl} pins when only {remaining} pins remain.")
        elif choice=="exit":
            quit()
        else:
             print('Invalid input. Try again') 

    remaining=10         

    while comp_chance!=0:
        bowl_comp=roll()
        if remaining>=bowl_comp:
            remaining=remaining-bowl_comp
            if bowl_comp==10 and comp_chance==2:
                    print("Its a strike by computer")
                    scores[1]+=bowl_comp
                    break
            elif remaining==0 and comp_chance==1:
                    print("Its a spare for computer.")
                    scores[1]+=bowl_comp
                    break
            elif bowl_comp!=10 and bowl_comp!=0 and remaining!=0:
                    scores[1]+=bowl_comp
                    comp_chance-=1
                    print(f"Computer dropped {bowl_comp} pins.Remaining pins are:{remaining}") 
            elif bowl_comp==0:
                    print("It is a guttergame by computer.")
                    comp_chance-=1
        else: 
             continue            
    print(f"Current scores : You-{scores[0]} and Computer-{scores[1]}")            
if scores[0] > scores[1]:
     print(f"You have beaten the computer, you have {scores[0]} points and computer has {scores[1]} points.")
elif scores[0] < scores[1]:
     print(f"You have lost to the computer, you have {scores[0]} points and computer has {scores[1]} points.")                     
else:
    print("It's a draw.")      