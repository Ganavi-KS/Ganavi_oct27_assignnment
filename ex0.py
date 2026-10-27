total = 0

for i in range(1, 4):
    price = float(input(f"Enter price of product {i}: "))
    total += price

gst_rate = float(input("Enter GST rate: "))

gst = total * gst_rate / 100
final_bill = total + gst

print("Total Price =", total)
print("GST =", gst)
print("Final Bill =", final_bill)