# ------------------------------
# Chicken Biriyani Ingredient Checker
# ------------------------------

# Ingredients for Chicken Biriyani
chicken_biriyani = ["Rice", "Chicken", "Onion", "Garlic", "Yogurt", "Spices", "Saffron"]

# Substitution dictionary
substitutions = {
    "Yogurt": ["Buttermilk", "Cream"],
    "Saffron": ["Turmeric"],
    "Chicken": ["Paneer", "Tofu", "Vegetables"]
}

# ------------------------------
# Function to check ingredients
# ------------------------------
def check_chicken_biriyani(available):
    missing = [ing for ing in chicken_biriyani if ing not in available]
    sub_replacements = {ing: substitutions[ing] for ing in missing if ing in substitutions}
    
    print("\n--- Chicken Biriyani Check ---")
    print(f"Ingredients you have: {[ing for ing in chicken_biriyani if ing in available]}")
    print(f"Missing Ingredients: {missing}")
    print(f"Substitutions available: {sub_replacements}")

# ------------------------------
# Main program
# ------------------------------
def main():
    print("=== Chicken Biriyani Ingredient Checker ===")
    available = input("Enter your available ingredients (comma separated): ").split(',')
    available = [item.strip().capitalize() for item in available]
    
    check_chicken_biriyani(available)

if __name__ == "__main__":
    main()
