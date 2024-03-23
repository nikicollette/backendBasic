from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.utils.function_calling import convert_pydantic_to_openai_function

# from langchain_core.output_parsers import JsonKeyOutputParser
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser, JsonOutputFunctionsParser


from typing import List
from pydantic import BaseModel, Field
import os

from prompts import CATEGORY_PROMPT, COLOR_PROMPT, DESCRIPTOR_PROMPT
os.environ["OPENAI_API_KEY"] = "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"

llm = ChatOpenAI(model="gpt-3.5-turbo")


#category
class Category(BaseModel):
    """
    type/category of clothing
    """
    #check without the mainCategory description if it still returns tops, pants, dresses, and skirts

    mainCategory: str = Field(description="value must be 'tops', 'pants', 'dresses', or 'skirts'")
    categories: List[str] = Field(description="additional clothing types")


_category_prompt = ChatPromptTemplate.from_template(CATEGORY_PROMPT)

category_func = convert_pydantic_to_openai_function(Category)


def get_category_chain(vals: dict):
    valid_categories = ['tops', 'pants', 'dresses', 'skirts']
    category = (_category_prompt | llm.bind(functions=[category_func]) | JsonKeyOutputFunctionsParser(key_name="mainCategory")).invoke(vals)
    if category not in valid_categories:
        return None
    else:
        return category

    # return (_descriptor_prompt | llm).invoke(vals)

#descriptors
class Descriptors(BaseModel):
    """
    descriptors of the clothing
    """
    descriptors: List[str] = Field(description="all descriptors")

_descriptor_prompt = ChatPromptTemplate.from_template(DESCRIPTOR_PROMPT)
descriptor_func = convert_pydantic_to_openai_function(Descriptors)


def get_descriptor_chain(vals: dict):
    descriptors = (_descriptor_prompt | llm.bind(functions=[descriptor_func]) |
            JsonKeyOutputFunctionsParser(key_name="descriptors")).invoke(vals)
    if not descriptors:
        return None
    else:
        return descriptors


#colors
class CategorizeColor(BaseModel):
    """
    Find the color from valid_colors that is closest to the input.
    """
    input_color: str = Field(description="input color")
    closest_color: str = Field(description="a color from valid colors closest to the input. must be one word.")

_color_prompt = ChatPromptTemplate.from_template(COLOR_PROMPT)
color_func = convert_pydantic_to_openai_function(CategorizeColor)
# print(color_func)

def get_color_chain(vals: dict):
    valid_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple', 'black', 'grey', 'white', 'brown', 'silver', 'gold']
    vals["categories"] = valid_colors

    # valid_color = (_color_prompt | llm).invoke(vals)

    valid_color = (_color_prompt | llm.bind(functions=[color_func]) | JsonKeyOutputFunctionsParser(key_name="closest_color")).invoke(vals)



    # return (_color_prompt | llm.bind(functions=[color_func])).invoke(vals)
    # valid_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple', 'black', 'grey', 'white', 'brown', 'silver', 'gold']
    # valid_color = (_color_prompt | llm).invoke(vals).content
    print(f"valid colors results {valid_color}")
    if valid_color not in valid_colors:
        return None
    else:
        return valid_color




# print(get_descriptor_chain({'title': 'Clara Cashmere Crew Cardigan', 'description': "Like your dreams, your 401k, or our sweaters, some things are just worth the investment. Made with high-quality materials like regeneratively grown cotton, recycled cashmere, and traceable wool, you'll buy one today and wear it for life."}))