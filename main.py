from __future__ import generator_stop
import sys
from turtle import st
import requests
import player
import json
import hltv_access
import user_io
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

MonthEnd = [ '31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31' ]
#generates strings representing the start and end dates of all 12 months for data collection purposes (a la htlv!)
def GenerateMonthArray(year):
    StartDates = []
    EndDates = []
    i = 0
    while i < 12:
        start = str(str(year) + "-" + str(i + 1) + "-01")
        end = str(str(year) + "-" + str(i + 1) + "-" + MonthEnd[i])
        # print(start + " - " + end)
        StartDates.append([str(datetime.strptime(start, '%Y-%m-%d').date())])
        EndDates.append([str(datetime.strptime(end, '%Y-%m-%d').date())])
        i += 1

    return [StartDates, EndDates]

#yekindar = get_stats.GetPlayer()
#yekindar.PrintPlayer()


#probably a better way to do this than hardcoding but whatever! :)

# test harness:

StartDates = GenerateMonthArray(2021)[0]
EndDates = GenerateMonthArray(2021)[1]

p1name      = "ropz"
p1id        = "11816"

p2name      = "broky"
p2id        = "18053"

p1 = hltv_access.GetPlayerName(p1id, p1name)
p1ratings = []

p2 = hltv_access.GetPlayerName(p2id, p2name)
p2ratings = []

i = 0
while i < 12:
    p1ratings.append(float(hltv_access.GetRating(p1id, p2name, StartDates[i][0], EndDates[i][0])))
    p2ratings.append(float(hltv_access.GetRating(p2id, p2name, StartDates[i][0], EndDates[i][0])))
    #sleep in fear of getting ip banned from hltv lol
    sleep(0.2)
    i += 1

#plots collected data onto a graph for funzo kabunzo
plt.plot(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], p1ratings, label=str(p1name + " Rating 2.0"))
plt.plot(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], p2ratings, label=str(p2name + " Rating 2.0"))
plt.xlabel('Month')
plt.ylabel('Rating 2.0')
plt.yticks( ( 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3 ) )
plt.title("Rating 2.0 over 2021")
plt.legend()
plt.show()