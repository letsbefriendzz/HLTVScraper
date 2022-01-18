import requests
import player
from datetime import datetime
from bs4 import BeautifulSoup

#CONSTANTS

MONTH_END = [ '31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31' ]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# top 20 players of 2021
PLAYERS = {
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
    "kscerato":"15631",

    #ASTRALIS
    "blamef":"15165",

    #G2
    "hunter-":"3972",
    "niko":"3741",

    #NIP
    "device":"7592",

    #VP
    "jame":"13776",
    "yekindar":"13915",

    #VITALITY
    "zywoo":"11893"
}

#generates strings representing the start and end dates of all 12 months for data collection purposes (a la htlv!)
def GenerateMonthArray(year):
    StartDates = []
    EndDates = []
    i = 0
    while i < 12:
        start = str(str(year) + "-" + str(i + 1) + "-01")
        end = str(str(year) + "-" + str(i + 1) + "-" + MONTH_END[i])
        # print(start + " - " + end)
        StartDates.append(str(datetime.strptime(start, '%Y-%m-%d').date()))
        EndDates.append(str(datetime.strptime(end, '%Y-%m-%d').date()))
        i += 1

    return [StartDates, EndDates]

# error thrown when hltv is being a nuisance
def StatAccessError():
    print("Error accessing Rating2.0 from HLTV\nYou've likely been IP banned temporarily.")

# returns a player obejct after scraping
def GetPlayer(playerCode = "13915", playerName = "yekindar", startDate = "2021-01-01", endDate = "2021-12-31", rankingFilter = "Top20"):
    res = requests.request("GET", "https://www.hltv.org/stats/players/" + str(playerCode) + "/" + str(playerName) + "?startDate=" + str(startDate) + "&endDate=" + str(endDate) + "&rankingFilter=" + str(rankingFilter))
    page = BeautifulSoup(res.content, 'html.parser')
    stats = page.find_all('div', class_="summaryStatBreakdownDataValue")
    name = page.find_all('h1', class_="summaryNickname text-ellipsis")[0]
    return player.player(name.string, stats[0].string, stats[1].string, stats[2].string, stats[3].string, stats[4].string, stats[5].string)

# returns string representing the respective stat of the player
# 0 = Rating 2.0
# 1 = DPR
# 2 = KAST
# 3 = Impact
# 4 = ADR
# 5 = KPR
def GetPlayerStat(playerName = "yekindar", startDate = "2021-01-01", endDate = "2021-12-31", rankingFilter = "Top20", stat = 0):
    res = requests.request("GET", "https://www.hltv.org/stats/players/" + str(PLAYERS[playerName]) + "/" + str(playerName) + "?startDate=" + str(startDate) + "&endDate=" + str(endDate) + "&rankingFilter=" + str(rankingFilter))
    page = BeautifulSoup(res.content, 'html.parser')
    stats = page.find_all('div', class_="summaryStatBreakdownDataValue")
    try:
        return str(stats[stat].string)
    except:
        raise StatAccessError()

# returns the player name of the player
def GetPlayerName(playerCode = "13915", playerName = "yekindar"):
    res = requests.request("GET", "https://www.hltv.org/player/" + playerCode + "/" + playerName)
    page = BeautifulSoup(res.content, 'html.parser')
    name = page.find_all('h1', class_="playerNickname")[0].string
    return name

def GetRating(playerName, startDate, endDate, rankingFilter):
    return GetPlayerStat(playerName, startDate, endDate, rankingFilter, 0)

def GetDPR(playerName, startDate, endDate, rankingFilter):
    return GetPlayerStat(playerName, startDate, endDate, rankingFilter, 1)

def GetKAST(playerName, startDate, endDate, rankingFilter):
    return GetPlayerStat(playerName, startDate, endDate, rankingFilter, 2)

def GetImpact(playerName, startDate, endDate, rankingFilter):
    return GetPlayerStat(playerName, startDate, endDate, rankingFilter, 3)

def GetADR(playerName, startDate, endDate, rankingFilter):
    return GetPlayerStat(playerName, startDate, endDate, rankingFilter, 4)

def GetKPR(playerName, startDate, endDate, rankingFilter):
    return GetPlayerStat(playerName, startDate, endDate, rankingFilter, 5)