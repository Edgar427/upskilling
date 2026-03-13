food_preference = {"🍔", "🍕", "🍤"}

restaurants = {
    "seafood_cove": {"🍤", "🍣", "🐟", "🦀"},
    "hungry_jacks": {"🍔", "🍟", "🍦", "🍕"},
    "potting_shed": {"🥦", "🥕", "🍞", "🥑"},
}

# Result should be hungry_jacks with {'🍔', '🍕'} being matched.
best_matched_food = set()
best_matched_restaurant = None

restaurants.update({"kyaw ba":{"🍔", "🍕", "🍤"}})


for restaurant,menu in restaurants.items():
   commonfood = food_preference.intersection(menu)
   if len(commonfood) > len(best_matched_food):
      best_matched_food = commonfood
      best_matched_restaurant = restaurant

print(f"The best match is {best_matched_restaurant} with {best_matched_food} as food")
    

    
   


