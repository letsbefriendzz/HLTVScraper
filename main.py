from __future__ import generator_stop
from contextlib import nullcontext
from distutils.log import error
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
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
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

# test harness:

StartDates = GenerateMonthArray(2021)[0]
EndDates = GenerateMonthArray(2021)[1]

players = {
    #FAZE
    "ropz":"11816",
    "broky":"18053",
    "twistzz":"10394",

    #GAMBIT
    "hobbit":"8528",
    "sh1ro":"16920",
    "ax1le":"16555",

    #NAVI
    "s1mple":"7998",
    "b1t":"18987",
    "electronic":"8918",

    #LIQUID
    "elige":"8738",
    "naf":"8520",

    #HEROIC
    "stavn":"10994",

    #FURIA
    "KSCERATO":"15631",

    #ASTRALIS
    "blameF":"15165",

    #G2
    "huNter-":"3972",
    "NiKo":"3741",

    #NIP
    "device":"7592",

    #VP
    "jame":"13776",
    "yekindar":"13915",

    #VITALITY
    "zywoo":"11893"
}

def RatingAccessError():
    print("Error accessing Rating2.0 from HLTV\nYou've likely been IP banned temporarily.")

def PlotPlayers():
    for i in players:
        p1id = players[i]
        p1name = i
        p1ratings = []

        print("Fetching and plotting " + p1name + " statistics.")

        j = 0
        while j < 12:
            rating = float(hltv_access.GetRating(p1id, p1id, StartDates[j][0], EndDates[j][0]))
            print(rating)
            if(rating < 0):
                raise RatingAccessError
            if rating < 0.7 and j > 1:
                p1ratings.append(p1ratings[j - 1])
            else:
                p1ratings.append(rating)
            #sleep in fear of getting ip banned from hltv lol
            sleep(0.5)
            j += 1

        plt.plot(MONTHS, p1ratings, label=str(p1name + " Rating 2.0"))

#plots collected data onto a graph for funzo kabunzo
PlotPlayers()
plt.xlabel('Month')
plt.ylabel('Rating 2.0')
plt.title("Rating 2.0 over 2021")
ax = plt.gca()
ax.set_ylim([0.8, 1.5])
plt.legend()
plt.show()
