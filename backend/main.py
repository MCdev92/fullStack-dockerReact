from typing import List
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

# Define your Recipe class
class Recipe(BaseModel):
    id: int
    title: str
    ingredients: str
        
# Create database
DB: List[Recipe] = [
    Recipe(id=1, title="Panda Express Chicken Terriyaki: ", ingredients=
           """(250g Skinless chicken thighs) 
           (3 cloves Garlic)
           (25mL sugar free maple syrup)
           (4 tbspsSoy sauce)
           (1/2 tbsp Ginger Black pepper)
           (1 tbsp Lemon juice sauce) (Leftover Marinade 3g Corn starch 40mL Water)"""),
    Recipe(id=2, title="Spicy Thai Basil Chicken: ", ingredients=
           """(⅓ cup chicken broth)
           (1 tablespoon oyster sauce)
           (1 tablespoon soy sauce, or as needed)
           (2 teaspoons fish sauce)
           (1 teaspoon white sugar)
           (1 teaspoon brown sugar)
           (2 tablespoons vegetable oil)
           (1 pound skinless, boneless chicken thighs, coarsely chopped)
           (¼ cup sliced shallots)
           (4 cloves garlic, minced)
           (2 tablespoons minced Thai chilies, Serrano, or other hot pepper)
           (1 cup very thinly sliced fresh basil leaves)
           (2 cups hot cooked rice)"""),
    Recipe(id=3, title="Thai Red Curry with Chicken: ", ingredients=
           """(6 tbsp Thai Red Curry Paste) 
           (1 quantity homemade Thai Red Curry Paste) 
           (2 large garlic cloves , minced)
           (2 tsp fresh ginger , finely grated)
           (1 tbsp lemongrass paste or finely chopped fresh)
           (3 tbsp vegetable oil (or canola or peanut)
           (1 cup (250 ml) chicken broth/stock , low sodium)
           (400 ml / 14 oz coconut milk (full fat!)
           (6 kaffir lime leaves (Note 4)
           (1 tbsp sugar (white, brown or palm)
           (2 tsp fish sauce , plus more to taste)
           (350g / 12 oz chicken thighs (boneless and skinless), cut into 0.75 / 1/3″ thick slices (Note 5)
           (150g / 5 oz pumpkin or butternut squash, cut into 1.5cm / 3/5" cubes (~1 heaped cup)
           (120g / 4oz green beans , trimmed and cut into 5cm/2″ pieces)
            """),
    Recipe(id=4, title="Healthy Salmon Bowl: ", ingredients=
           """ |- Salmon -| -->
              • 350-400g raw skinless salmon (cut into cubes for 2 servings)
              • 1 tbsp garlic (fresh or powder)
              • 1 tsp chilli flakes
              • 1 tsp paprika
              • 1 tbsp light & dark soy sauce
              • 15-20g honey
              • 1/2 lemon juice
              • Mix till each piece is well coated
              • Cook salmon on medium-low heat for 2-3 mins each side till golden brown
              |- Cucumber Salad -| -->
              • 1/2 cucumber cut into slices
              • 1-2 tbsp light soy sauce
              • 1/2 tsp garlic
              • 1/2 tsp chilli flakes or paprika (depends if you want it spicy)
              • 1 tsp rice vinegar of lemon juice
              |- Serve -| -->
              • 100g cooked jasmine rice per serving(200g for 2 servings)
              • Cucumber salad
              • Sliced carrot
              • Sliced red onion
              • 50g avocado per serving (100g for 2 servings)
              • Spicy lemon mayo (light mayo, sriracha & lemon juice)
              • Garnish with green onion and sesame seeds

              """),
Recipe(id=5, title="Instant Pot Chicken Tortilla Soup: ", ingredients=
       """
            • Olive Oil
            • Onion and Garlic
            • Diced Green Chiles
            • Fire Roasted Diced Tomatoes
            • Red Enchilada Sauce
            • Chili Powder and Cumin
            • Black Beans
            • Chicken Broth
            • Chicken Breast
            • Corn
            • Salt and pepper """),
    
]

# Change your path to api and return database
@app.get("/api")
def read_root():
    return DB
