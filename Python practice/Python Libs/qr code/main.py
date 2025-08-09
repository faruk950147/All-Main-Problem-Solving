import os
import qrcode
import time

start_time = time.time()
# with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\qr code\\websites_list.csv", "r") as file:
#     for line in file:
#         data = line.strip().split(",")
#         # print(data[0], data[1])
#         qrcode.make(data[1]).save(f"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\qr code\\qrimg\\{data[0]}.png", scale=10)

# print("Done in", round(time.time() - start_time, 2), "seconds")


# with open("websites_list.csv", "r") as file:
#     for line in file:
#         data = line.strip().split(",")
#         # print(data[0], data[1])
#         qrcode.make(data[1]).save(f"qrimg/{data[0]}.png", scale=10)
        
def generate_qr_codes(csv_file="websites_list.csv", output_folder="qrimg"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the CSV file and read lines
    with open(csv_file, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) < 2:
                print(f"Skipping invalid line: {line}")
                continue

            filename, url = data[0], data[1]

            # Generate QR code image
            img = qrcode.make(url)

            # Save image as PNG in output folder
            img.save(f"{output_folder}/{filename}.png", scale=10)

            print(f"Saved QR code for {url} as {output_folder}/{filename}.png")

if __name__ == "__main__":
    generate_qr_codes()


print("Done in", round(time.time() - start_time, 2), "seconds")