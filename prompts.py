CATEGORY_PROMPT = """
You are given a title and description of a women's clothing product. 
You must generate 5 words that describe the clothing type. 
The clothing type must be a noun and one word. 

Examples of clothing types include: 
"top", "bottom", "jeans", "skirt", "shirt", "tank", "tee-shirt", "t-shirt", "tee", "pants", "hoodie", "jacket", 
"jumper","sweater"

{title}
{description}
"""

DESCRIPTOR_PROMPT = """
You are given a title and description of a women's clothing product. 
Perform the following steps:

1. Extract all attributive nouns and descriptors from the name and description.
2. Generate 8 new attributive nouns and descriptors that describe the clothing item from the extracted values.

All values must only be one word and must not be a color.

Examples of descriptors include:
"slim-fit", "cropped", "mini", "sleeveless", "a-line", "short", "knit", "ribbed", "mohair", "wool"

{title}
{description}
"""

COLOR_PROMPT = """
Given an input, {input}, categorize it given the following categories: {categories}

{input}
{categories}
"""