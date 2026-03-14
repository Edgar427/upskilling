class Product:
    def __init__(self, name, calories, price_per_kg):
        self.name = name
        self.calories = calories
        self.price_per_kg = price_per_kg

    def get_price(self, weight_kgs):
        return self.price_per_kg * weight_kgs


banana = Product("🍌", calories=105, price_per_kg=1.0)
tomato = Product("🍅", calories=22, price_per_kg=2.1)
potato = Product("🥔", calories=162, price_per_kg=0.9)

banana_weight = float(input("Enter banana weight (kg): "))
tomato_weight = float(input("Enter tomato weight (kg): "))
potato_weight = float(input("Enter potato weight (kg): "))

print("Banana price:", banana.get_price(banana_weight))
print("Tomato price:", tomato.get_price(tomato_weight))
print("Potato price:", potato.get_price(potato_weight))