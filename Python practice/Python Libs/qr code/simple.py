import qrcode

url = "https://www.google.com"

img = qrcode.make(url)
img.save("google_qr.png", scale=10)

print("QR code saved as google_qr.png")

# def generate_qr_code(url, filename):
#     # Generate QR code
#     img = qrcode.make(url)

#     # Save QR code image as PNG
#     img.save(f"{filename}.png", scale=10)

# if __name__ == "__main__":
#     url = "https://www.google.com"
#     filename = "google_qr"
#     generate_qr_code(url, filename)
#     print(f"QR code saved as {filename}.png")
