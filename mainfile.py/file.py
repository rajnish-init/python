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
    line_no = 1
    data = True
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return

            line_no += 1



check_for_line()