import sys
from functions import *
# Modules above


if sys.argv[1] == "rank":
    username = sys.argv[-1]
    getRank(username)
elif sys.argv[1] == "stats":
    username = sys.argv[-1]
    getStat(username)
else:
    print('Unknown error, make sure you\'re using "rank" or "stats"')
