"""
The text file Final.txt contains the student's grades on a final exam.
This program is going to analyse the grades and return three functions.
First, the program will output the total number of grades found on Final.txt.
Then, it will calculate the average grade of the numbers by dividing the sum of the numbers by the total numbers.
Afterwards, the program will output the percentage of grades that are above average.

First function will output number of grades.
Second function will loop through the scores and output the average.
Third function will also loop and output the percantage that are above the average.
"""
"""
# function 1 
def main():
    file = open("Final.txt", 'r')
    data = file.read
    numbers = data.split()
    print("Number of grades: ", len(numbers))
# function 2 
    infile = open("Final.txt", 'r')
    total = 0
    number_of_grades = 0
    line = float(infile.readline())
    while line != "":
        number_of_grades += 1
        total += float(line)
        line = infile.readline()
        average = total / number_of_grades
    print("Average grade: ", average)
# function 3
def calculate_percent_above_average(numbers, average):
    above_average = 0
    length = len(numbers)
    for index in range (length):
        if numbers[index] > average:
            above_average = above_average +1
    return above_average / length

calculate_percent_above_average()
main()

"""

def main():
    file = open("Final.txt", "r")
    data = file.read()
    numbers = data.split()
    print("Number of grades: ", len(numbers))
    infile = open("Final.txt", "r")
    total = 0
    number_of_lines = 0
    line = float(infile.readline())
    while line != "":
        number_of_lines += 1
        total += float(line)
        line = infile.readline()
        average = total / number_of_lines
    print("Average grade: ", average)

# def calculate_percent_above_average(numbers, average):
#     above_average = 0
#     length = len(numbers)
#     for index in range (length):
#         if numbers [index] > average:
#             above_average = above_average +1
#     return above_average / length
#     print("Percentage of grades above average: ", (return) + "%")

# calculate_percent_above_average()
main()
