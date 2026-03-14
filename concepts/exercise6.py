total_expenses = {
    "food": 40,
    "transport": 0,
    "shopping": 190
}

total_expenses.update({"entertainment":20 })
# total_expenses["entertainment"] = total_expenses.get("entertainment", 0) + 20
total_expenses["entertainment"] = 20

total_expenses["food"] += 12 
# total_expenses["food"] = total_expenses.get("food", 0) + 12  

total_expenses.update({"transport": 10})
print(total_expenses)

for key,value in total_expenses.items():
    print(key)
    print(value)