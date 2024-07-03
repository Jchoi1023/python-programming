#CIS41 - Jihye Choi
#Friend lists and add new friends to the list

#1 Creat friend lists
friends_2017 = ['Jane', 'Lydia', 'Sienna']
friends_2018 = ['John', 'Nathan', 'David']

#2 Combine the two lists
friends_all = friends_2017 + friends_2018
# print(friends)

#3 Enter friend
name = input("Enter a name of a friend: ")

#4 Show the you met the friend in 2017 or 2018
if name in friends_all:
    if name in friends_2017:
        print(f"{name} is in 2017.")
    else:
        print(f"{name} is in 2018.")
else:
    print(f"You don't have any friend with the name {name}")

#5 Add a new friend to the list
new_friend = input("Enter the name of a new friend: ")
year_to_add = input("Enter the year you want to add: ")

if year_to_add == "2017":
    friends_2017.append(new_friend)
elif year_to_add == "2018":
    friends_2018.append(new_friend)
else:
    print("Invalid year entered")

#6 Show 2017 and 2018 friends' lists

print(friends_2017)
print(friends_2018)

'''
Enter a name of a friend: Lydia
Lydia is in 2017.
Enter the name of a new friend: Mike
Enter the year you want to add: 2018
['Jane', 'Lydia', 'Sienna']
['John', 'Nathan', 'David', 'Mike']

Enter a name of a friend: Sam
You don't have any friend with the name Sam
Enter the name of a new friend: Sam
Enter the year you want to add: 2018
['Jane', 'Lydia', 'Sienna']
['John', 'Nathan', 'David', 'Sam']
'''