from itertools import permutations

# Define the books and their quantities
books = {
    'Mathematics': 4,
    'Physics': 3,
    'Chemistry': 2,
    'Language': 1
}

# Calculate the total number of books
total_books = sum(books.values())

# Create a list of subjects based on the book quantities
subjects = []
for subject, quantity in books.items():
    subjects.extend([subject] * quantity)

# Find all possible arrangements
arrangements = list(permutations(subjects, total_books))

# Print the number of different arrangements
print("Number of different arrangements:", len(arrangements))
# Number of different arrangements: 3628800

# Print the arrangements
for arrangement in arrangements:
    print(arrangement)
