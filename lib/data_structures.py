spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Returns a list of names of the spicy foods."""
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns a list of spicy foods with heat level greater than 5."""
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    """Prints each spicy food with its name, cuisine, and heat level."""
    for food in spicy_foods:
        heat_level_emoji = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the spicy food that matches the given cuisine."""
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # Return None if no matching cuisine is found

def print_spiciest_foods(spicy_foods):
    """Prints spicy foods with heat level greater than 5."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    """Returns the average heat level of all spicy foods."""
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Integer division

def create_spicy_food(spicy_foods, new_food):
    """Adds a new spicy food to the list and returns the updated list."""
    spicy_foods.append(new_food)
    return spicy_foods