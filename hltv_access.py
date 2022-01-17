import requests
import player
import sys
from bs4 import BeautifulSoup

# returns a player obejct after scraping
def GetPlayer(playerCode = "13915", playerName = "yekindar", startDate = "2021-01-01", endDate = "2021-12-31", rankingFilter = "Top20"):
    res = requests.request("GET", "https://www.hltv.org/stats/players/" + str(playerCode) + "/" + str(playerName) + "?startDate=" + str(startDate) + "&endDate=" + str(endDate) + "&rankingFilter=" + str(rankingFilter))
    page = BeautifulSoup(res.content, 'html.parser')
    stats = page.find_all('div', class_="summaryStatBreakdownDataValue")
    name = page.find_all('h1', class_="summaryNickname text-ellipsis")[0]
    return player.player(name.string, stats[0].string, stats[1].string, stats[2].string, stats[3].string, stats[4].string, stats[5].string)

# returns string representing the rating 2.0 of the player
def GetRating(playerCode = "13915", playerName = "yekindar", startDate = "2021-01-01", endDate = "2021-12-31", rankingFilter = "Top20"):
    res = requests.request("GET", "https://www.hltv.org/stats/players/" + str(playerCode) + "/" + str(playerName) + "?startDate=" + str(startDate) + "&endDate=" + str(endDate) + "&rankingFilter=" + str(rankingFilter))
    page = BeautifulSoup(res.content, 'html.parser')
    stats = page.find_all('div', class_="summaryStatBreakdownDataValue")
    try:
        return str(stats[0].string)
    except:
        return -1

# returns the player name of the player
def GetPlayerName(playerCode = "13915", playerName = "yekindar"):
    res = requests.request("GET", "https://www.hltv.org/player/" + playerCode + "/" + playerName)
    page = BeautifulSoup(res.content, 'html.parser')
    name = page.find_all('h1', class_="playerNickname")[0].string
    return name