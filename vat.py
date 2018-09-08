def price_no_vat(price, vat_rate):
    vat = price/100*vat_rate
    price_no_vat = price - vat
    return price_no_vat
print(price_no_vat(100, 18))    
