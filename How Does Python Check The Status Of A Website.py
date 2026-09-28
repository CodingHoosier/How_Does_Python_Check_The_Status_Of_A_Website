# https://www.youtube.com/watch?v=9obvBlxaoiE
# How Does Python Check The Status Of A Website?
import urllib.request
# Check the status of google.com
target_url = "https://www.google.com"
req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
code = urllib.request.urlopen(req).getcode()
print("Website Status Code:", code)
# Now check the status of ebay.com. 
# It will fail because eBay doesn't want to be accessed by a bot.
try:
    target_url = "https://www.ebay.com"
    req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
    code = urllib.request.urlopen(req).getcode()
    print("Website Status Code:", code)
except Exception as e:
    print ("eBay.com access error: ", e)
