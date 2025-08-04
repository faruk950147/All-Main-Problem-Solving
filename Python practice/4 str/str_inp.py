# write a program
# input = "my23name45is"
# # output = "si23eman45ym"
# output = ""
# for i in input:
#     if i.isalpha():
#         output = i + output
#     else:
#         output = i + output
# print(output)

input_str = "my23name45is"

# Step 1: just letter reverse
letters = [c for c in input_str if c.isalpha()]
reversed_letters = letters[::-1]

# Step 2: now input string character by character
output = ""
letter_index = 0

for c in input_str:
    if c.isalpha():
        # letter replace with reversed letter
        output += reversed_letters[letter_index]
        letter_index += 1
    else:
        # digit keep as it is
        output += c

print(output)
