import qrcode

filename = "google_qr"
url = "https://www.google.com"

img = qrcode.make(url)
img.save(f"{filename}.png", scale=10)

print(f"QR code saved as {filename}.png")

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
