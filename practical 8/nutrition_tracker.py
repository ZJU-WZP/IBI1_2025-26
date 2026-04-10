class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fats):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fats = fats
apple = food_item("Apple", 60, 0.3, 15, 0.5)

def track_nutrition(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrates += item.carbohydrates
        total_fat += item.fats

    print("Total calories:", total_calories)
    print("Total protein:", total_protein, "g")
    print("Total carbohydrates:", total_carbohydrates, "g")
    print("Total fat:", total_fat, "g")

    if total_calories > 2500:
        print("Warning: Excessive calorie consumption!")

    if total_fat > 90:
        print("Warning: Excessive fat consumption!")

apple = food_item("Apple", 60, 0.3, 15, 0.5)
rice = food_item("Rice", 200, 4, 45, 0.4)
burger = food_item("Burger", 700, 25, 50, 40)
pizza = food_item("Pizza", 800, 30, 70, 35)

foods_eaten = [apple, rice, burger, pizza]
track_nutrition(foods_eaten)