import requests
import os

def retrieve_input_text(season, day):
    return requests.get(
            f"https://adventofcode.com/{season}/day/{day}/input",
            cookies={"session": os.getenv("AdventSessionKey")}
    ).text