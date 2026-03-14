# operators
principal = 240_000
annual_rate = 0.05
years = 2
final_amount = principal * (1 +annual_rate) ** years
compound_interest = final_amount - principal
print(compound_interest)