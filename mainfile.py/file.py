# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        if "Python" in data :
            print("Found")
        else:
            print("Not Found")

check_for_word()

def check_for_line():
    word = "Python"
    line_no = 1 #line_no is a variable that keeps track of the current line number in the file.
    data = True # data is being initialised
    with open("practice.txt", "r") as f:
        while data:  # till the data is true/valid
            data = f.readline()
            if word in data: #in is a keyword in Python used to check if one string is part of another.
                print(line_no)
                return #This ends the function immediately after finding the word.No further lines will be checked once the word is found.
            line_no += 1
check_for_line()