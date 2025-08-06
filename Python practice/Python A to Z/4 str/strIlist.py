# given a string and a list of words, return the words that are present in the string
# input: string = "Sky is blue"
# output: "blue is Sky"

# method 1
def reverse_string(string):
    return " ".join(string.split(" ")[::-1])

print(reverse_string("Sky is blue"))

# method 2
string = "Sky is blue"
new_string = string.split(" ")
rev_string = new_string[::-1]
print(" ".join(rev_string))

# method 3
string = "Sky is blue"
print(" ".join(string.split(" ")[::-1]))

