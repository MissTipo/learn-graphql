import requests

# define the query
my_query = """
{
    website(url:"https://www.howtographql.com/basics/1-graphql-is-the-better-rest/"){
        title
        image
        description
    }
}
"""
# define the response
my_response = requests.post("http://127.0.0.1:5050",
                            params={'query': my_query})
print(my_response.text)
