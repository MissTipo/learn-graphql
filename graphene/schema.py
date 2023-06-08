"""A script for crawling and extracting data from the web."""

import graphene
import extraction
import requests

# define the extraction function


def extract(my_url):
    """Extract url from web."""
    html = requests.get(my_url).text
    extracted = extraction.Extractor().extract(html, source_url=my_url)
    print(extracted)


extract('https://www.howtographql.com/basics/1-graphql-is-the-better-rest/')

# define the schema


class my_website(graphene.ObjectType):
    """Define the schema."""

    url = graphene.String(required=True)
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()

# define the query


class Query(graphene.ObjectType):
    """Define the query for retrieving the schema objects."""

    website = graphene.Field(my_website, url=graphene.String())

    def resolve_website(self, info, url):
        """Resolve the website object."""
        extracted = extract(url)

        if extracted is None:
            return ValueError("Failed to extract data from the provided URL.")
        return my_website(url=url,
                          title=extracted.title,
                          description=extract.description,
                          image=extracted.image,
                          )


schema = graphene.Schema(query=Query)
