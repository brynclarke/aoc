import os, sys
from colorama import Fore
day = sys.argv[1].zfill(2)

os.system(f"{day}.py {day}.in {Fore.GREEN}")
print(Fore.RESET, end="")