from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QTextEdit, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QTextOption
from PyQt5.QtCore import Qt


# Define a dictionary containing meal options and recipes
meals = {
    'breakfast': {
        'meal_name': 'Breakfast',
        'recipes': ["Sausage & Crescent Roll Breakfast Casserole", "Ham and Swiss Omelet", "Almond-Vanilla Yogurt Parfaits"],
        'ingredients': {
            'Sausage & Crescent Roll Breakfast Casserole': ["pork sausage", "refrigerated crescent rolls", "shredded part-skim mozzarella cheese", "eggs", "milk", "salt", "pepper"],
            'Ham and Swiss Omelet': ["ham", "Swiss cheese", "eggs", "milk", "salt", "pepper"],
            'Almond-Vanilla Yogurt Parfaits': ["almond granola", "vanilla yogurt", "fresh berries"]
        },
        'quantities': {
            'Sausage & Crescent Roll Breakfast Casserole': ["1 pound", "1 tube", "2 cups", "8", "2 cups", "1/2 teaspoon salt", "1/4 teaspoon pepper"],
            'Ham and Swiss Omelet': ["1 cup", "1/2 cup", "4", "2 tablespoons", "1/4 teaspoon salt", "1/4 teaspoon pepper"],
            'Almond-Vanilla Yogurt Parfaits': ["1 cup", "1 cup", "1 cup"]
        }
    },
    'lunch': {
        'meal_name': 'Lunch',
        'recipes': ["Chicken Caesar Salad", "Vegetarian Wrap", "Tomato Basil Pasta"],
        'ingredients': {
            'Chicken Caesar Salad': ["grilled chicken breast", "romaine lettuce", "Parmesan cheese", "croutons", "Caesar dressing"],
            'Vegetarian Wrap': ["whole wheat tortilla", "hummus", "mixed vegetables", "feta cheese"],
            'Tomato Basil Pasta': ["spaghetti", "tomatoes", "fresh basil", "olive oil", "garlic", "Parmesan cheese"]
        },
        'quantities': {
            'Chicken Caesar Salad': ["1 cup", "2 cups", "1/2 cup", "1/2 cup", "2 tablespoons"],
            'Vegetarian Wrap': ["1", "2 tablespoons", "1 cup", "1/4 cup"],
            'Tomato Basil Pasta': ["8 oz", "2 cups", "1/2 cup", "2 tablespoons", "2 cloves", "1/4 cup"]
        }
    },
    'dinner': {
        'meal_name': 'Dinner',
        'recipes': ["Grilled Salmon with Lemon Dill Sauce", "Beef and Broccoli Stir-Fry", "Vegetable Lasagna"],
        'ingredients': {
            'Grilled Salmon with Lemon Dill Sauce': ["salmon fillets", "lemon", "fresh dill", "olive oil", "salt", "pepper"],
            'Beef and Broccoli Stir-Fry': ["beef sirloin", "broccoli florets", "soy sauce", "brown sugar", "garlic", "ginger", "sesame oil"],
            'Vegetable Lasagna': ["lasagna noodles", "ricotta cheese", "spinach", "zucchini", "mozzarella cheese", "marinara sauce"]
        },
        'quantities': {
            'Grilled Salmon with Lemon Dill Sauce': ["4 fillets", "1", "2 tablespoons", "2 tablespoons", "1/2 teaspoon", "1/4 teaspoon"],
            'Beef and Broccoli Stir-Fry': ["1 pound", "3 cups", "1/4 cup", "2 tablespoons", "2 cloves", "1 teaspoon", "1 tablespoon"],
            'Vegetable Lasagna': ["9 sheets", "2 cups", "2 cups", "1 medium", "2 cups", "2 cups"]
        }
    }
}

class RecipeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Explore Recipes")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)

        font = QFont("Roboto", 12, QFont.Normal)

        self.meal_field = QLineEdit()
        self.meal_field.setFont(font)
        self.meal_field.setPlaceholderText("Enter your meal choice (breakfast, lunch, or dinner)")
        self.meal_field.setStyleSheet(
            "QLineEdit { border: 2px solid #CCCCCC; border-radius: 10px; padding: 10px; }"
            "QLineEdit:focus { border-color: #007AFF; }"
        )
        layout.addWidget(self.meal_field)

        self.explore_button = QPushButton("Explore Recipes")
        self.explore_button.setFont(font)
        self.explore_button.setStyleSheet(
            "QPushButton { background-color: #007AFF; color: white; border-radius: 10px; padding: 10px; }"
            "QPushButton:hover { background-color: #0056B3; }"
        )
        self.explore_button.clicked.connect(self.explore_recipes)
        layout.addWidget(self.explore_button)

        self.recipe_text = QTextEdit()
        self.recipe_text.setFont(font)
        self.recipe_text.setReadOnly(True)  # Set QTextEdit to read-only
        self.recipe_text.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)  # Enable word wrap
        self.recipe_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Enable vertical scrollbar as needed
        layout.addWidget(self.recipe_text)

    def explore_recipes(self):
        meal_choice = self.meal_field.text().strip().lower()
        if meal_choice in meals:
            meal_options = meals[meal_choice]
            recipes_text = f"Options for {meal_options['meal_name']}:\n"
            for i, recipe in enumerate(meal_options['recipes'], start=1):
                recipes_text += f"{i}. {recipe}\n"
            recipes_text += "\nChoose a recipe (1-3):"
            recipe_choice, _ = QInputDialog.getInt(self, "Recipe Choice", recipes_text, min=1, max=len(meal_options['recipes']))
            if recipe_choice:
                recipe_name = meal_options['recipes'][recipe_choice - 1]
                ingredients = meal_options['ingredients'][recipe_name]
                quantities = meal_options['quantities'][recipe_name]
                recipe_text = f"Recipe for {recipe_name}:\n"
                for i in range(len(ingredients)):
                    recipe_text += f"{quantities[i]} {ingredients[i]}\n"
                self.recipe_text.setPlainText(recipe_text)
            else:
                QMessageBox.warning(self, "No Recipe Selected", "Please select a recipe.")
        else:
            QMessageBox.warning(self, "Invalid Meal Choice", "Please choose 'breakfast', 'lunch', or 'dinner.'")
