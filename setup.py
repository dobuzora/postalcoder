import urllib.request
import zipfile
import sys
import os

def sprint(s, message):
    print("[" + s + "] " + message)

# Download
sprint("START","start setup.py")

url = "https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/47okinaw.zip"
title = "okinawa.zip"

sprint("DOWNLOAD",url)

try:
    urllib.request.urlretrieve(url, "{0}".format(title))
    sprint("DOWNLOAD", "done!")
except:
    sprint("ERROR", "please check url or Internet")

sprint("ZIP", "...")
with zipfile.ZipFile(title) as dzip:
    dzip.extractall('okinawa-post')

sprint("REMOVE", "remove " + title)
os.remove(title)

sprint("COMPLATE", "all setup done")


