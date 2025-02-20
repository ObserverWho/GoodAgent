from langchain.tools import Tool
import requests

def get_random_joke(_):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    return response.json()['setup'] + " - " + response.json()['punchline']

joke_tool = Tool(
    name="Joke Teller",
    func=get_random_joke,
    description="Useful for telling random programming jokes"
)
