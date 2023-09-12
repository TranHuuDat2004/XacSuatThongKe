from itertools import combinations

men = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6']
women = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9']

# (a) Calculate the number of different selections
num_selections = len(list(combinations(men, 3))) * len(list(combinations(women, 2)))

print("Number of different selections:", num_selections)
# Number of different selections: 720

# (b) Print the selections to the screen
print("\nSelections:")
count = 0
for men_combination in combinations(men, 3):
    for women_combination in combinations(women, 2):
        print(men_combination + women_combination)
        count = count + 1 
         
print("Ket qua la = ",count)