from ast import Return
from asyncio.windows_events import NULL
from datetime import datetime

# gets a start or end date from the user - returns the formatted YYYY-MM-DD
# date from using the datetime.strptime().date() methods.
def GetDate(se = "start date"):
    UsrInp = input("Enter the " + se + " [YYYY-MM-DD]:\t")
    try:
        return str(datetime.strptime(UsrInp, '%Y-%m-%d').date())
    except:
        return NULL