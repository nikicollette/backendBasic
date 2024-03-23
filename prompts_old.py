CATEGORY_PROMPT = """
# You are given a name and description of a women's clothing product. 
# Generate a list of relevant product categories for the type of the clothing.
# The word must be a noun.
# The word must only be one word. 
# At least five types must be provided. 
# 
# Examples of types of clothing include: 
# "top", "bottom", "jeans", "skirt", "shirt", "tank", "tee-shirt", "t-shirt", "tee", "pants", "hoodie", "jacket", 
# "jumper","sweater"

{name}
{description}
"""

DESCRIPTOR_PROMPT = """
Given the name and description of a women's clothing product, perform the following steps:

1. Extract all attributive nouns and descriptors from the name and description.
2. Generate 8 new attributive nouns and descriptors that describe the clothing item from the extracted values.
3. Combine the extracted and generated values into a single list. 

Follow the following rules:
1. All values must only be one word and must not be a color.
2. Only return one list containing the combined values from the extracted and generated values
3. There is no need to distinguish which values are extracted vs. generated 

Examples of descriptors include:
"slim-fit", "cropped", "mini", "sleeveless", "a-line", "short", "knit", "ribbed", "mohair", "wool"

{name}
{description}
"""

COLOR_PROMPT = """
Given the name and description of a women's clothing product, perform the following steps:

1. Extract all information about the color of the product
2. If there is no information about the color of the product, return none and do not complete steps 3 and 4
3. If there is information about the color of the product, generate 8 additional colors that describe the colors
4. Combine the extracted and generated values into a single list. 

Follow the following rules:
1. All values must be a color.
2. Only return one list containing the combined values from the extracted and generated values
3. There is no need to distinguish which values are extracted vs. generated 
4. Must include one color that is from this list [green, red, blue, purple, blue, pink, white, black, yellow, orange, brown]
5. If there are no colors mentioned in the description return "none"


{name}
{description}
"""