#Task 1
integers = input("Please enter a list of random numbers, each separated by a space: ")

integer_list = [int(integer) for integer in integers.split()]

print(sum(integer_list))

#Task 2
fav_books = ("The 7 Husbands of Evelyn Hugo", "Blossoms of The Savannah", "Kigogo", "Looking For Alaska", "Qwani Anthology")
for book in fav_books:
    print(book)

#Task 3
name = input("Please enter your name: ")
age = input("Please enter your age in numbers: ")
fav_colour = input("Please enter your favourite colour: ")

info = {"name": name, "age": int(age), "favourite colour": fav_colour}
print(info)

#Task 4
first_input_set = input("Please enter a random set of numbers separated by spaces: ")
first_set = set(map(int, first_input_set.split()))

second_input_set = input("Please enter another random set of numbers separated by spaces: ")
second_set = set(map(int, second_input_set.split()))

third_set = first_set & second_set
print(f"The common numbers you entered were {third_set}")

#Task 5
words = input("Please enter random words separated by spaces: ")
words_list = list(words.split())
odd_list = []

for word in words_list:
    if len(word) % 2 != 0:
        odd_list.append(word)

print(f"These words you entered have an odd number of characters {odd_list}.")