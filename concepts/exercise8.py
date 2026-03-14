def apply_discount(originalprice, percent):
    if percent >= 100:
        return 0
    else:
    
        discounted = originalprice * (percent / 100)
        discountedprice = originalprice - discounted
        return discountedprice

new_price = apply_discount( percent=10, originalprice=80)
print(new_price)