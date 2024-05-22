#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Student Name : Devapati LakshmiPrasanna
#Student ID : 700758768

# List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()
print(f"Sorted ages: {ages}")

# Find the min and max age
min_age = ages[0]
max_age = ages[-1]
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# Re-sort the list after adding min and max ages
ages.sort()
print(f"Updated sorted ages: {ages}")

# Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print(f"Median age: {median_age}")

# Find the average age
average_age = sum(ages) / n
print(f"Average age: {average_age}")

# Find the range of the ages
age_range = max_age - min_age
print(f"Range of ages: {age_range}")


# In[2]:


# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

print("Dog Dictionary:")
print(dog)

# Create a student dictionary with specified keys
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

print("\nStudent Dictionary:")
print(student)

# Get the length of the student dictionary
student_length = len(student)
print("\nLength of the student dictionary:", student_length)

# Get the value of skills and check the data type
skills = student['skills']
print("\nSkills:", skills)
print("Data type of skills:", type(skills))

# Modify the skills values by adding one or two skills
student['skills'].append('Machine Learning')
student['skills'].append('Deep Learning')

print("\nUpdated skills:", student['skills'])

# Get the dictionary keys as a list
student_keys = list(student.keys())
print("\nStudent dictionary keys:", student_keys)

# Get the dictionary values as a list
student_values = list(student.values())
print("Student dictionary values:", student_values)


# In[3]:


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Stella', 'Bethany', 'Cathy')
brothers = ('Dawood', 'Weller', 'Drake')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# Print siblings
print("Siblings:", siblings)

# How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Charlie', 'Kimberly')
family_members = siblings + parents

# Print family members
print("Family members:", family_members)


# In[4]:


# Define the initial sets and list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("\nIT companies after adding 'Twitter':", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update({'LinkedIn', 'Snapchat', 'TikTok'})
print("\nIT companies after adding multiple companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print("\nIT companies after removing 'Oracle':", it_companies)

# What is the difference between remove and discard
# `remove` will raise a KeyError if the item does not exist in the set
# `discard` will not raise an error if the item does not exist
it_companies.discard('NonExistentCompany')  # Will not raise an error

# Join A and B
A_union_B = A.union(B)
print("\nA union B:", A_union_B)

# Find A intersection B
A_intersection_B = A.intersection(B)
print("A intersection B:", A_intersection_B)

# Is A subset of B
A_subset_B = A.issubset(B)
print("Is A subset of B:", A_subset_B)

# Are A and B disjoint sets
A_disjoint_B = A.isdisjoint(B)
print("Are A and B disjoint sets:", A_disjoint_B)

# Join A with B and B with A
A_update_B = A.copy()
A_update_B.update(B)
B_update_A = B.copy()
B_update_A.update(A)
print("\nA updated with B:", A_update_B)
print("B updated with A:", B_update_A)

# What is the symmetric difference between A and B
A_symmetric_difference_B = A.symmetric_difference(B)
print("Symmetric difference between A and B:", A_symmetric_difference_B)

# Delete the sets completely
del A
del B
print("\nSets A and B deleted.")

# Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print("\nLength of age list:", len(age))
print("Length of age set:", len(age_set))


# In[5]:


import math

# Given radius
radius = 30

# Calculate the area of a circle
_area_of_circle_ = math.pi * radius ** 2

# Calculate the circumference of a circle
_circum_of_circle_ = 2 * math.pi * radius

# Display the calculated area and circumference
print("Area of the circle:", _area_of_circle_)
print("Circumference of the circle:", _circum_of_circle_)

# Take radius as user input and calculate the area
user_radius = float(input("Enter the radius of the circle: "))
user_area_of_circle = math.pi * user_radius ** 2
print("Area of the circle with radius", user_radius, "is:", user_area_of_circle)


# In[6]:


# Given sentence
sentence = "I am a teacher and I love to inspire and teach people"

# Split the sentence into words
words = sentence.split()

# Convert the list of words to a set to get unique words
unique_words = set(words)

# Find the number of unique words
num_unique_words = len(unique_words)

# Print the unique words and their count
print("Unique words:", unique_words)
print("Number of unique words:", num_unique_words)


# In[7]:


# Print the lines with tab escape sequence
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


# In[8]:


# Define the radius and calculate the area
radius = 10
area = 3.14 * radius ** 2

# Use string formatting to display the statement
output = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(output)


# In[9]:


# Read the number of students from the user
N = int(input("Enter the number of students: "))

# Initialize lists to store weights in pounds and kilograms
weights_lbs = []
weights_kgs = []

# Read weights of N students into a list
for i in range(N):
    weight_lbs = float(input(f"Enter the weight of student {i+1} (in lbs): "))
    weights_lbs.append(weight_lbs)

# Convert weights from pounds to kilograms and store them in a separate list
for weight_lbs in weights_lbs:
    weight_kgs = weight_lbs * 0.453592  # 1 pound = 0.453592 kilograms
    weights_kgs.append(round(weight_kgs, 2))

# Print the converted weights in kilograms
print("Weights in kilograms:", weights_kgs)


# In[ ]:




