import requests
from bs4 import BeautifulSoup
import re



player = input("Which player? (format: lebron-james)\n")
stats = []
numbers = []
stat = input("Which stats (all caps, space separated)?\n")
stats = stat.split(" ")
for stat in stats:
    number = input(f"How many {stat}: ")
    numbers.append(int(number))
assert(len(stats) == len(numbers))

intervals = input("Enter game counts (space separated, 1 to 25): ").split(" ")
intervals = [int(x) for x in intervals]



url = "https://www.statmuse.com/nba/ask/" + player + "-1st-quarter-game-log"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("visual-answer").prettify()

totals = [0 for i in intervals]

statLists = []
for stat in stats:
    indices = [m.start() for m in re.finditer(stat, results)]
    L = []
    for i in indices:
        value = re.sub("[^0-9]", "", results[i:i+50])
        if len(value) != 0:
            L.append(int(value))
    statLists.append(L)




for i in range(max(intervals)):
    #print(i)
    happened = True
    for j in range(len(stats)):
        if not happened: break
        value = statLists[j][i]
        #print(f"{stats[j]}: {value}")
        if value < numbers[j]:
            #print("breaking") 
            happened = False
            break
    if happened:
        for j in range(len(intervals)):
            if intervals[j] > i:
                totals[j] += 1

probs = []
odds = []

for i in range(len(intervals)):
    prob = totals[i] / intervals[i]
    probs.append(prob)
    if prob == 1:
        odds.append(-100000)
    elif prob > 0.5:
        odds.append(int(-1 * 100 * prob/(1 - prob)))
    else:
        odds.append("+" + str(int((100 - (prob) * 100) / (prob))))





print(f"Player: {player}")
statsStr = ""
for i in range(len(stats)):
    number = numbers[i]
    stat = stats[i]
    statsStr += f"{number} {stat} "
print(statsStr)

for i in range(len(intervals)):
    print(f"Last {intervals[i]}: Probability {probs[i]}, Fair Odds: {odds[i]}")





#stat = "PTS"
#indices = [m.start() for m in re.finditer(stat, results)]
#sum = 0
#for i in indices:
#    value = re.sub("[^0-9]", "", results[i:i+50])
    #team: [i-100+10:i-100+13]
