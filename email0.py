# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getContent import getContent

def sendemail(article_title):

    msg = MIMEMultipart()

    att1 = MIMEText(open(article_title + '.txt', 'rb').read(), 'base64',
        'gb2312')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename = "' +article_title +\
        '.txt' + '"'
    msg.attach(att1)
    msg['to'] = 'wujiuliu_65@kindle.cn'
    msg['from'] = 'dhuo@tcd.ie'
    msg['subject'] = 'hello world'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('dhuo@tcd.ie', '')
        server.sendmail(msg['from'], msg['to'], msg.as_string())
        server.quit()
        print 'heihei'
    except Exeption, e:
        print str(e)
    msg['to'] = 'whdd_1202_25@kindle.cn'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('dhuo@tcd.ie', '')
        server.sendmail(msg['from'], msg['to'], msg.as_string())
        server.quit()
        print 'heihei'
    except Exeption, e:
        print str(e)


def getText():
    article = getContent()
    article_title = article['title']
    article_content = article['content']
    file_out = open(article_title + '.txt', 'w')
    file_out.write(article_content.encode("utf-8"))
    file_out.close()
    return article_title

if __name__ == '__main__':
    article_title = getText()
    sendemail(article_title)
