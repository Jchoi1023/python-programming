#CIS41 Chapter 6 - Exercise 4 Jihye Choi
#Extra Credit - Figure skating medal counts

country_name = [ 'Canada', 'Italy', 'Germany', 'Japan', 'Russia', 'South Korea', 'United States']
medal_name = ['Gold', 'Silver', 'Bronze']
country = len(country_name)
medal = 3
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]

#print table
column_width = 15
header = "{:<{}}".format("Country", column_width) + ''.join(['{:<{}}'.format(medal, column_width) for medal in medal_name])
print(header)
for i in range(country):
    row = "{:<{}}".format(country_name[i], column_width)
    for j in range(medal):
        row += '{:<{}}'.format(counts[i][j], column_width)
    print(row)

#print total number of medals 
column_width = 15
header = "{:<{}}".format("Country", column_width) + ''.join(['{:<{}}'.format(medal, column_width) for medal in medal_name])
# print(header)

total_medals = 0  

for i in range(len(country_name)):
    row = "{:<{}}".format(country_name[i], column_width)
    for j in range(len(medal_name)):
        medal_count = counts[i][j]
        row += '{:<{}}'.format(medal_count, column_width)
        total_medals += medal_count 
    # print(row)

# Print the total number of medals
print("\nTotal Medals: {}".format(total_medals))

#Print the total number of gold, silver and bronze medals
column_width = 15
header = "{:<{}}".format("Country", column_width) + ''.join(['{:<{}}'.format(medal, column_width) for medal in medal_name])
# print(header)

total_medals = [0] * len(medal_name) 

for i in range(len(country_name)):
    row = "{:<{}}".format(country_name[i], column_width)
    for j in range(len(medal_name)):
        medal_count = counts[i][j]
        row += '{:<{}}'.format(medal_count, column_width)
        total_medals[j] += medal_count  
    # print(row)

# Print the total number of gold, silver, and bronze medals
for medal, total_count in zip(medal_name, total_medals):
    print("Total {} Medals: {}".format(medal, total_count))

#Remove countries without a gold medal from the table
column_width = 15
header = "{:<{}}".format("Country", column_width) + ''.join(['{:<{}}'.format(medal, column_width) for medal in medal_name])
print(header)

for i in range(len(country_name)):
    row = "{:<{}}".format(country_name[i], column_width)
    for j in range(len(medal_name)):
        row += '{:<{}}'.format(counts[i][j], column_width)
    # print(row)

# Remove countries without a gold medal
counts_with_gold = [row for row in counts if row[0] > 0]

# Print the updated table
for i in range(len(counts_with_gold)):
    row = "{:<{}}".format(country_name[i], column_width)
    for j in range(len(medal_name)):
        row += '{:<{}}'.format(counts_with_gold[i][j], column_width)
    print(row)


# Print the dictionary
medals_dict = {}

for i in range(len(country_name)):
    country_data = {}
    for j in range(len(medal_name)):
        country_data[medal_name[j]] = counts[i][j]
    medals_dict[country_name[i]] = country_data

for country, medals in medals_dict.items():
    print("{}: {}".format(country, medals))

    '''
    Country        Gold           Silver         Bronze         
Canada         0              3              0              
Italy          0              0              1              
Germany        0              0              1              
Japan          1              0              0              
Russia         3              1              1              
South Korea    0              1              0              
United States  1              0              1              

Total Medals: 14
Total Gold Medals: 5
Total Silver Medals: 5
Total Bronze Medals: 4

Country        Gold           Silver         Bronze         
Canada         1              0              0              
Italy          3              1              1              
Germany        1              0              1      

Canada: {'Gold': 0, 'Silver': 3, 'Bronze': 0}
Italy: {'Gold': 0, 'Silver': 0, 'Bronze': 1}
Germany: {'Gold': 0, 'Silver': 0, 'Bronze': 1}
Japan: {'Gold': 1, 'Silver': 0, 'Bronze': 0}
Russia: {'Gold': 3, 'Silver': 1, 'Bronze': 1}
South Korea: {'Gold': 0, 'Silver': 1, 'Bronze': 0}
United States: {'Gold': 1, 'Silver': 0, 'Bronze': 1}
'''