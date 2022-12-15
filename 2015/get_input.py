import requests, os, sys
season = "2015"
day = sys.argv[1]

data = requests.get(
        f"https://adventofcode.com/{season}/day/{day}/input",
        cookies={"session": os.getenv("AdventSessionKey")}
).text

open(f"{day.zfill(2)}.in", "w").write(data)