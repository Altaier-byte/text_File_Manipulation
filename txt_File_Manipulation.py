phrase = input("Enter the word you want to search and the line number: ")
line_number = 0
list_of_results = []

with open('fru_veg.txt', 'r') as read_file:

 for line in read_file:
    line_number += 1
    if phrase in line:
     list_of_results.append((line_number, line.rstrip()))
     print("Your search result is: " + str(list_of_results))

        