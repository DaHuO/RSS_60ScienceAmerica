# -*- coding: UTF-8 -*-

import urllib2

def getUrl():
    target_url = 'http://www.scientificamerican.com/podcast/60-second-science/'
    response = urllib2.urlopen(target_url)
    html = response.read()
    flag = html.find('data-podcast-title')
    flag = html.find('<a href="', flag)
    flag2 = html.find('">', flag)
    page_url = html[flag + 9: flag2]
    return page_url

if __name__ == "__main__":
    getUrl()
