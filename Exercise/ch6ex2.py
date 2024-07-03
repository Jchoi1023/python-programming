#CIS41 - Jihye Choi
#Create friend dictionary and add new friends to the dictionary

#1 Creat a dictionary of friends that you met in 2017 and 2018 
friends = {"2017" : ['Jane', 'Lydia', 'Sienna'], "2018": ['John', 'Nathan', 'David']}

#2 Print the friends' names in the dictionary 
print(friends)

#3 Enter friend
name = input("Enter a name of a friend: ")

# 4 Show the you met the friend in 2017 or 2018
for year, list in friends.items():
        if name in list: 
            print(f"{name} is in {year}.")
            break
else:
    print(f"You don't have any friend with the name {name}")

#5 Add a new friend to the list
new_friend = input("Enter the name of a new friend: ")
year_to_add = input("Enter the year you want to add: ")

if year_to_add == "2017":
    friends["2017"].append(new_friend)
elif year_to_add == "2018":
    friends["2018"].append(new_friend)
else:
    print("Invalid year entered")

#6 Show 2017 and 2018 friends' lists
print(friends)

'''
{'2017': ['Jane', 'Lydia', 'Sienna'], '2018': ['John', 'Nathan', 'David']}
Enter a name of a friend: Nathan
Nathan is in 2018.
Enter the name of a new friend: Sam
Enter the year you want to add: 2017
{'2017': ['Jane', 'Lydia', 'Sienna', 'Sam'], '2018': ['John', 'Nathan', 'David']}

{'2017': ['Jane', 'Lydia', 'Sienna'], '2018': ['John', 'Nathan', 'David']}
Enter a name of a friend: Sam
You don't have any friend with the name Sam
Enter the name of a new friend: Sam
Enter the year you want to add: 2018
{'2017': ['Jane', 'Lydia', 'Sienna'], '2018': ['John', 'Nathan', 'David', 'Sam']}

'''