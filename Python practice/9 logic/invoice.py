from datetime import datetime

# Seller and Buyer Info
seller = "ABC Store"
buyer = input("Enter customer name: ")

# Products
products = []
while True:
    name = input("Product name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    qty = int(input("Quantity: "))
    price = float(input("Unit price: "))
    total = qty * price
    products.append((name, qty, price, total))

# Invoice Number and Date
invoice_no = "INV-" + datetime.now().strftime("%Y%m%d%H%M%S")
date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Print Invoice
print("\n" + "="*40)
print(f"INVOICE NO: {invoice_no}")
print(f"DATE      : {date}")
print(f"SELLER    : {seller}")
print(f"BUYER     : {buyer}")
print("="*40)
print("{:<20} {:<5} {:<10} {:<10}".format("Product", "Qty", "Price", "Total"))
print("-"*40)

grand_total = 0
for p in products:
    print("{:<20} {:<5} {:<10} {:<10}".format(p[0], p[1], p[2], p[3]))
    grand_total += p[3]

print("-"*40)
print(f"{'Grand Total:':<35} {grand_total} BDT")
print("="*40)




# def generate_invoice(buyer, products, seller="ABC Store"):
#     # Invoice Number and Date
#     invoice_no = "INV-" + datetime.now().strftime("%Y%m%d%H%M%S")
#     date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

#     # Print Invoice
#     print("\n" + "="*40)
#     print(f"INVOICE NO: {invoice_no}")
#     print(f"DATE      : {date}")
#     print(f"SELLER    : {seller}")
#     print(f"BUYER     : {buyer}")
#     print("="*40)
#     print("{:<20} {:<5} {:<10} {:<10}".format("Product", "Qty", "Price", "Total"))
#     print("-"*40)

#     grand_total = 0
#     for item in products:
#         name, qty, price = item
#         total = qty * price
#         print("{:<20} {:<5} {:<10} {:<10}".format(name, qty, price, total))
#         grand_total += total

#     print("-"*40)
#     print(f"{'Grand Total:':<35} {grand_total} BDT")
#     print("="*40)
