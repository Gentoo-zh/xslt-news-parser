#!/usr/bin/env python3


import sys

try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    import xml.etree.ElementTree as ElementTree

if __name__ == "__main__":
    xml = ElementTree.ElementTree(file=sys.stdin)

    poster = xml.find("./poster").text
    date = xml.find("./date").text
    title = xml.find("./title").text
    news = xml.find("./body")

    print("Poster: %s" % poster)
    print("Date: %s" % date)
    print("Title: %s" % title)
    print("News:\n%s" % ElementTree.tostring(news, encoding="unicode"))
