import qrcode
import time

start_time = time.time()
# with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\qr code\\websites_list.csv", "r") as file:
#     for line in file:
#         data = line.strip().split(",")
#         # print(data[0], data[1])
#         qrcode.make(data[1]).save(f"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\qr code\\qrimg\\{data[0]}.png", scale=10)

# print("Done in", round(time.time() - start_time, 2), "seconds")


with open("websites_list.csv", "r") as file:
    for line in file:
        data = line.strip().split(",")
        # print(data[0], data[1])
        qrcode.make(data[1]).save(f"qrimg/{data[0]}.png", scale=10)

print("Done in", round(time.time() - start_time, 2), "seconds")