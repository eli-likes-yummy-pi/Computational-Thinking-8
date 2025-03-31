# Beginning: create variables
Hulk_points = 0
SpiderMan_points = 0
IronMan_points = 0
DoctorStrange_points = 0 
Thor_points = 0

# Middle: ask questions

# Question 1:

answer = input("Would you rather be A)strong, or B)smart\n")

if answer == "A":
    Hulk_points += 1
    Thor_points += 1
elif answer == "B":
    SpiderMan_points += 1
    IronMan_points += 1
    DoctorStrange_points += 1

# Question 2:

answer = input("Would you prefer to be A)funny, or B)serious in battle\n")

if answer == "A":
    SpiderMan_points += 1
    IronMan_points += 1
    Thor_points += 1
elif answer == "B":
    DoctorStrange_points += 1
    Hulk_points += 1

# Question 3:

answer = input("What is the biggest priority, A) gaining aura, B) saving lives, C) killing bad guys\n")

if answer == "A":
    SpiderMan_points -= 1
elif answer == "B":
    SpiderMan_points += 1
    IronMan_points += 1
elif answer == "C":
    Thor_points += 1
    Hulk_points += 1
    DoctorStrange_points += 1

# Question 4 

answer = input("Why is being a superhero important, A) to save lives/stop bad guys the police can't, B) for the fate of the universe, C) to get famous and recognized\n")

if answer == "A":
    SpiderMan_points += 1
    Hulk_points += 1
    Thor_points += 1
elif answer == "B":
    DoctorStrange_points += 2
elif answer == "C":
    IronMan_points += 1

# Question 5 

answer = input("How caring are you to normal people, A) never leave them behind in fight, B) would save them, but not first priority, C) not as important as stopping the bad guy\n")

if answer == "A":
    SpiderMan_points += 1
    IronMan_points += 1
elif answer == "B":
    DoctorStrange_points += 1
    Thor_points += 1
elif answer == "C":
    Hulk_points += 1

# Ending: find the results

if SpiderMan_points > IronMan_points and Thor_points and DoctorStrange_points and Hulk_points:
    print("You are most like Spider-Man!")
elif IronMan_points > SpiderMan_points and Thor_points and DoctorStrange_points and Hulk_points:
    print("You are most like Iron-Man!")
elif Thor_points > Hulk_points and IronMan_points and DoctorStrange_points and SpiderMan_points:
    print("You are most like Thor!")
elif Hulk_points > DoctorStrange_points and IronMan_points and SpiderMan_points and Thor_points:
    print("You are most like Hulk!")
elif DoctorStrange_points > SpiderMan_points and IronMan_points and Thor_points and Hulk_points:
    print("You are most like Doctor Strange!")

