# -*- coding: UTF-8 -*-

import getUrl
import urllib2
import HTMLParser

def getContent():
    article = {}
    h = HTMLParser.HTMLParser()
    target_url = getUrl.getUrl()
    print target_url
    response = urllib2.urlopen(target_url)
    html = response.read()
    flag_title = html.find('<title>')
    flag_title_end = html.find('</title>', flag_title)
    article['title'] = html[flag_title + 7: flag_title_end]
    print article['title']
    flag_start = html.find('<div class="article-text')
    flag_end = html.find('The above text is a transcript of this podcast',
        flag_start)
    flag_end = flag_end - 8
    print flag_start
    print flag_end
    paragraphs = []
    cursor = flag_start
    while cursor < flag_end:
        flag_p = html.find('<p>', cursor)
        flag_p_end = html.find('</p>', flag_p)
        paragraphs.append(html[flag_p + 3:flag_p_end])
        cursor = flag_p_end
    text = article['title'] + '\n\n\n\n'
    for para in paragraphs:
        para = h.unescape(para)
        para = para.replace('<em>', '')
        para = para.replace('</em>', '')
        para = para.replace('</a>', '')
        flag_a = para.find('<a')
        while flag_a!= -1:
            flag_a_end = para.find('>', flag_a)
            para = para[:flag_a] + para[flag_a_end + 1:]
            flag_a = para.find('<a')
        # print para
        text += para + '\n\n'
    article['content'] = text
    return article

if __name__ == "__main__":
    getContent()
