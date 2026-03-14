# conditions
customer_age = 70
is_student = False
if customer_age < 18:
    print(f"Entry is free")
elif is_student or customer_age > 65:
    print(f"Entry is 50% off")
else:
    print(f"Entry is full price")

    