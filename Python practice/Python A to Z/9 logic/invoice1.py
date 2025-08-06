from datetime import datetime

def generate_invoice(buyer, products, seller="ABC Store", discount=0.0, tax_rate=0.0, payment_method="Cash"):
    # Invoice metadata
    invoice_no = "INV-" + datetime.now().strftime("%Y%m%d%H%M%S")
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Header
    print("\n" + "="*50)
    print(f"{'INVOICE':^50}")
    print("="*50)
    print(f"Invoice No   : {invoice_no}")
    print(f"Date         : {date}")
    print(f"Seller       : {seller}")
    print(f"Buyer        : {buyer}")
    print(f"Payment      : {payment_method}")
    print("="*50)

    # Product Table Header
    print("{:<20} {:>5} {:>10} {:>10}".format("Product", "Qty", "Price", "Total"))
    print("-"*50)

    # Product lines
    subtotal = 0
    for name, qty, price in products:
        total = qty * price
        subtotal += total
        print("{:<20} {:>5} {:>10.2f} {:>10.2f}".format(name, qty, price, total))

    print("-"*50)

    # Discounts and Tax
    discount_amount = subtotal * discount
    taxed_amount = (subtotal - discount_amount) * tax_rate
    grand_total = subtotal - discount_amount + taxed_amount

    # Totals
    print(f"{'Subtotal:':<35} {subtotal:>10.2f}")
    if discount > 0:
        print(f"{'Discount (' + str(int(discount*100)) + '%):':<35} -{discount_amount:>10.2f}")
    if tax_rate > 0:
        print(f"{'Tax (' + str(int(tax_rate*100)) + '%):':<35} +{taxed_amount:>10.2f}")
    print("="*50)
    print(f"{'GRAND TOTAL:':<35} {grand_total:>10.2f} BDT")
    print("="*50)
