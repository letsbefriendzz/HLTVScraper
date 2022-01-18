from __future__ import generator_stop
import hltv_access
from time import sleep

# test harness:

playerADR = {}

for player in hltv_access.PLAYERS:
    print(player + " ADR:")
    print(hltv_access.GetADR(player, "2021-01-01", "2021-12-31", "Top10"))