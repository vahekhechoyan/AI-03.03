# 1
# Write a program that takes a sentence and creates a dictionary where each word is a key, and the value is the number of times that word appears.
# Use a sample sentence and break it into words to fill the dictionary. 
# Example: For the sentence "the cat and the hat", the dictionary should be {"the": 2, "cat": 1, "and": 1, "hat": 1}.

# def word_count(sentence):
#     words = sentence.lower().split()
#     word_dict = {word: words.count(word) for word in set(words)}
#     return word_dict

# sentence = "The cat and the hat."
# print(word_count(sentence))



# 2
# Create a dictionary to store student names as keys and their scores as values.
# Use a few sample names and scores to populate the dictionary. Print out each student’s name and score on a new line.

# students = {
#     "Alice": 85,
#     "Bob": 90,
#     "Charlie": 78,
#     "David": 92
# }

# for name, score in students.items():
#     print(f"{name}: {score}")




# 3
# Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...}). 
# Use this dictionary to convert a list of numbers into words and print each word on a new line.

# num_to_word = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five"
# }

# numbers = [1, 3, 5, 2, 4]

# for num in numbers:
#     print(num_to_word[num])




# 4
# Create a dictionary to represent a store’s inventory with items as keys and quantities as values. Print the quantity of a specific item (e.g., "Apples").
# Update the quantity of an item and print the dictionary to show the change.

# inventory = {
#     "Apples": 10,
#     "Bananas": 5,
#     "Oranges": 8,
#     "Grapes": 12
# }

# print("Apples:", inventory["Apples"])

# inventory["Apples"] += 5

# print(inventory)




# 5
# Write a program that takes a sentence and uses a set to find all unique words. Print each unique word on a new line.

# def unique_words(sentence):
#     words = set(sentence.lower().split())
#     for word in words:
#         print(word)

# sentence = "The boy bay apples."
# unique_words(sentence)




# 6
# Given two lists of numbers, use sets to find and print the common elements between them.

# def find_common_elements(list1, list2):
#     common_elements = set(list1) & set(list2)
#     for element in common_elements:
#         print(element)

# list1 = [1, 2, 3, 4, 5,7,9]
# list2 = [4, 5, 6, 7, 8,9,11,13]
# find_common_elements(list1, list2)




# 7
# Given a list of numbers, use a set to find any duplicates in the list and print them. You can add numbers to a set one by one and check if they are already present.


# def find_duplicates(numbers):
#     duplicates = {num for num in numbers if numbers.count(num) > 1}
#     print(set(duplicates))

# numbers = [1, 2, 2, 3, 4, 4, 5,6,7,8,6,9]
# find_duplicates(numbers)



# 8
# Use a set to create a list of vocabulary words from a paragraph. Break the paragraph into individual words, add each word to the set, and print the final set of unique words.
# def extract_vocabulary(paragraph):
#     words = set(paragraph.lower().split())
#     print(words)

# paragraph = "Python is fun. Python is powerful."
# extract_vocabulary(paragraph)



# 9
# Հայտարարել երկու set: Տպել դրանց միավորումը, հատումը, սիմետրիկ տարբերությունը:

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# print('Union:', set1 | set2)

# print('Intersection:', set1 & set2)

# print('Symmetric Difference:', set1 ^ set2)




# 10
# Հայտարարել երկու զանգված: Երկու զանգվածներն էլ նույնն են՝ բացառությամբ որ մի զանգվածը պարունակում է մեկ էլեմենտ ավելի շատ: Գտնել այդ էլեմենտը:

# def find_extra_element(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
    
#     extra_element = list(set2 - set1)  
#     return extra_element[0] if extra_element else list(set1 - set2)[0]

# list1 = [1, 2, 3, 4, 5,6]
# list2 = [1, 2, 3, 4, 5, 6,9]

# print("Extra element:", find_extra_element(list1, list2))




# 11
# Գրել ծրագիր որը կստանա երկու set և կվերադարձնի True, եթե մեկը մյուսի ենթաբազմություն է, False հակառակ դեպքում:

# def is_subset(set1, set2):
#     return set1.issubset(set2)

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}

# print(is_subset(set1, set2)) 

# set3 = {1, 6}
# print(is_subset(set3, set2))




# 12
# Հայտարարել set` բաղկացած ամբողջ թվերից: Set-ում եղած բոլոր կենտ թվերը ջնջել, և ավելացնել տվյալ քանակությամբ զույգ թվեր:

# def modify_set(numbers_set, num_of_even_numbers_to_add):
    
#     numbers_set = {num for num in numbers_set if num % 2 == 0}
    
#     even_numbers_to_add = [num * 2 for num in range(1, num_of_even_numbers_to_add + 1)]
#     numbers_set.update(even_numbers_to_add)
    
#     return numbers_set

# numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# modified_set = modify_set(numbers_set, 3)

# print(modified_set)




# 13
# Ստեղծել ծրագիր, որը կներառի օգտատերերի տվյալների ներմուծումը, պահպանումը բառարանում և ցուցակում,
# ապա ցույց կտա օգտատերերին ըստ ներմուծված անվան(“Not found”, եթե այդպիսի օգտատեր գոյություն չունի)։ 
# Յուրաքանչյուր օգտատեր պետք է ունենա հետևյալ դաշտերը՝ ID, անուն, ազգանուն, Էլ. փոստ, գաղտնաբառ և հեռախոսահամար:


# def add_user(users_dict, users_list):

#     user_id = input("Օգտատերի ID: ")
#     first_name = input("Անուն: ")
#     last_name = input("Ազգանուն: ")
#     email = input("Էլ. փոստ: ")
#     password = input("Գաղտնաբառ: ")
#     phone = input("Հեռախոսահամար: ")
    

#     user = {
#         'ID': user_id,
#         'Անուն': first_name,
#         'Ազգանուն': last_name,
#         'Էլ. փոստ': email,
#         'Գաղտնաբառ': password,
#         'Հեռախոսահամար': phone
#     }
    

#     users_dict[user_id] = user
#     users_list.append(user)

# def search_user_by_name(users_list, name):

#     found_users = [user for user in users_list if user['Անուն'].lower() == name.lower()]
    
#     if found_users:
#         for user in found_users:
#             print(f"ID: {user['ID']}, Անուն: {user['Անուն']}, Ազգանուն: {user['Ազգանուն']}, Էլ. փոստ: {user['Էլ. փոստ']}, Հեռախոսահամար: {user['Հեռախոսահամար']}")
#     else:
#         print("Not found")


# users_dict = {}
# users_list = []


# add_user(users_dict, users_list)


# name_to_search = input("Որոնել օգտատիրոջ անունը: ")
# search_user_by_name(users_list, name_to_search)




# 14
#  Movie Recommendation System (Dictionaries + Sets)
# Given a dictionary of users and the movies they have watched, suggest movies that their friends have watched but they haven’t.

# def recommend_movies(users_movies, user):

#     user_movies = users_movies[user]
    

#     recommended_movies = set()
    

#     for friend, movies in users_movies.items():
#         if friend != user:
#             recommended_movies.update(movies - user_movies)
    
#     return recommended_movies


# users_movies = {
#     "Alice": {"Avatar", "The Dark Knight", "Home Alone", "Titanic"},
#     "Bob": {"Avatar", "Home Alone", "Matrix", "Star Wars"},
#     "Charlie": {"The Dark Knight", "Star Wars", "Titanic", "Avatar"},
#     "David": {"Titanic", "Avatar", "Home Alone"}
# }


# user = "Alice"
# recommended = recommend_movies(users_movies, user)

# print(f"Movies recommended for {user}: {', '.join(recommended)}")




# 15
#  Word Frequency Analyzer (Dictionaries)
# Given a paragraph of text, count how many times each word appears and find the most common words.



# def word_frequency_analyzer(paragraph):
    
#     words = paragraph.lower().split()
    
    
#     word_count = {}
    
#     for word in words:
       
#         word = word.strip('.,!?()[]{}":;')
        
       
#         word_count[word] = word_count.get(word, 0) + 1
    
    
#     most_common = max(word_count, key=word_count.get)
#     return word_count, most_common, word_count[most_common]


# paragraph = "Hello world! This is a test. Hello again, world. Test test."


# word_count, most_common_word, count = word_frequency_analyzer(paragraph)


# print("Word Frequency:", word_count)
# print(f"The most common word is '{most_common_word}' which appears {count} times.")




# 16
# Social Media Friend Suggestion (Dictionaries + Sets)
# Suggest friends for a user by finding friends of friends who are not already direct friends.


# def suggest_friends(users_friends, user):
  
#     user_friends = users_friends.get(user, set())
    
    
#     suggested_friends = set()

    
#     for friend in user_friends:
        
#         friends_of_friend = users_friends.get(friend, set())
        
        
#         suggested_friends.update(friends_of_friend - user_friends - {user})

#     return suggested_friends


# users_friends = {
#     "Alice": {"Bob", "Alan", "David"},
#     "Bob": {"Alice", "Alan", "Tom"},
#     "Charlie": {"Alice", "Bob", "David"},
#     "David": {"Alice", "Alan", "Tom"},
#     "Eve": {"Bob", "David"}
# }


# user = "Alice"
# suggested = suggest_friends(users_friends, user)


# print(f"Friend suggestions for {user}: {', '.join(suggested)}")




# 17
#  Unique Product Categories (Dictionaries + Sets)
# Given a list of purchased products and their categories, return the unique product categories bought.

# def unique_product_categories(purchased_products):
    
#     categories = set()

    
#     for product, category in purchased_products.items():
#         categories.add(category)
    
#     return categories


# purchased_products = {
#     "Laptop": "Electronics",
#     "Shoes": "Fashion",
#     "Shirt": "Fashion",
#     "Smartphone": "Electronics",
#     "Blender": "Home Appliances",
#     "Washing Machine": "Home Appliances"
# }


# unique_categories = unique_product_categories(purchased_products)

# print(f"Unique product categories: {', '.join(unique_categories)}")