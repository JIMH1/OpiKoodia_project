import datetime
import random
import time


points = {}
player = input("Give your name ")
points[player] = 0
rounds = int(input("Rounds: "))
for r in range(0, rounds):
    time.sleep(0.5)
    print("Get ready..")
    time.sleep(random.randint(1,12))
    then = datetime.datetime.now()
    t = input("GO!! ")
    now = datetime.datetime.now()
    diff = then-now
    reaction_time = round(abs(diff.total_seconds()), 2)
    print("Reaction time: {} seconds".format(reaction_time))
time.sleep(0.5)