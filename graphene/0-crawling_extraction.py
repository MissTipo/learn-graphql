"""A script for crawling and extracting data from the web."""

# import graphene
import extraction
import requests

# define the extraction function


def extract(my_url):
    """Extract url from web."""
    html = requests.get(my_url).text
    extracted = extraction.Extractor().extract(html, source_url=my_url)
    print(extracted)


extract('https://www.howtographql.com/basics/1-graphql-is-the-better-rest/')
