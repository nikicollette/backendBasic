from scrapers import scraper_list
from grab_mongo import get_database
import os
from openai import OpenAI
from langchain_funcs import get_category_chain, get_descriptor_chain, get_color_chain
dbname = get_database()
tops = dbname["tops"]
pants = dbname["pants"]
dresses = dbname["dresses"]
skirts = dbname["skirts"]

#list of collections
os.environ["OPENAI_API_KEY"] = ""
client = OpenAI()
collection_list = [tops, pants, dresses, skirts]


def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

# for scraper in scraper_list:
#     results = scraper()

def process_scraper(results):
    # results = scraper_list[0]()
    # if results.empty:
    #     #see if this prevents iterating through all scrapers?
    #     break

    # grab everything in the database from the current scraper company
    base_url = results.iloc[0].loc['base_url']
    print(f"BASE URL {base_url}")

    # grab all hrefs for the company based on base_url already in the dataframe
    db_hrefs = []
    for collection in collection_list:
        # Search through collection and filter based on base_url field
        cursor = collection.find({'base_url': base_url})

        # Iterate over the results and grab unique hrefs
        for document in cursor:
            db_hrefs.append(document['href'])
            print(f"RESULT href {document['href']}")
        # result = collection.find({"base_url": base_url})
        # if result:
        #     db_search.append(result)
    print(f"DB HREFS {db_hrefs}")

    # iterate through href list and for each href check if it already exists in the database
    for index, result in results.iterrows():
        href = result.href
        # if it already exists in the database, then we don't need to perform langchain funcs
        if href in db_hrefs:
            # print(f"INSIDE ALREADY EXISTS {result.title} + {href}")
            db_hrefs.remove(href)

            # this is for when duplicates are already in and you want a fresh start
            dbname["tops"].delete_many({"href":href})
            print(f"deleted all {result.title}")
        # else:
        print(f"trying lanchain funcs {result.title}")
            # call langchain funcs
        category = get_category_chain({'title': result.title, 'description': result.description})
        descriptor = get_descriptor_chain({'title': result.title, 'description': result.description})
        valid_color = get_color_chain({'input': result.color})
        if not category:
            raise ValueError("Did not get category")
        if not descriptor:
            raise ValueError("Did not get descriptor")
        if not valid_color:
            raise ValueError("Did not get valid color")

        # if not (category and descriptor and valid_color):
        #     raise ValueError("Did not get from langchain")

        # print(f"category is {category}, descriptor is {descriptor}, color is {valid_color}")

        #create the document
        document = result.to_dict()
        document['category'] = category
        document['descriptor'] = descriptor
        document['valid_color'] = valid_color

        embedding_input = f"""
        This clothing item is of type {category}. The item is called {result.title}. The item contains the colors {valid_color} and {result.color}.
        The item is bought from {result.company_name}. The description for the item is {result.description}
        """

        document['item_embedding'] = get_embedding(embedding_input)

        # print(f"DOCUMENT: {document}")
        #add document to correct db
        collection = dbname[category]
        # print(f"collection: {collection}")
        print(f"document to insert: {document}")
        collection.insert_one(document)
        # except Exception as e:
        #     print(f"there was an error + {e}")

# whatever is left in the list, remove from database
# print(f"hrefs to delete: {db_hrefs}")
# for remaining_href in db_hrefs:
#     query = {"href": remaining_href}
#     for collection in collection_list:
#         if collection.find(query):
#             collection.delete_one(query)

if __name__ == "__main__":
    # results = scraper()
    # process_scraper(results)
    process_scraper()