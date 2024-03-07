"""Redis na DPB cvičení 02"""
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

SCOREBOARD = "scoreboard"
r.zadd(SCOREBOARD, {"Alfréd": 888, "Pepa": 10, "Mára": 568, "Jóža": 943,
                    "Vlasta": 981, "Honza": 999, "Klára": 875, "Petr": 163,
                    "Markéta": 99, "Vítek": 9, "Lenka": 73})
print("Top 3")
print(r.zrevrange(SCOREBOARD, 0, 2, withscores=True))
print("Nejhorší skóre")
print(r.zrange(SCOREBOARD, 0, 0, withscores=True))
print("Počet hráčů s méně než 100 body")
print(r.zremrangebyscore(SCOREBOARD, 0, 100))
print("Hráči s 850 až 1000 body")
print(r.zrangebyscore(SCOREBOARD, 850, 1000, withscores=True))
print("Pozice Alfréda v žebříčku a jeho skóre")
print(r.zrevrank(SCOREBOARD, "Alfréd", withscore=True))
r.zincrby(SCOREBOARD, 12, "Alfréd")
print("Pozice Alfréda v žebříčku a jeho skóre po zvýšení o 12")
print(r.zrank(SCOREBOARD, "Alfréd", withscore=True))
