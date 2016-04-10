# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getContent import getContent
from os import listdir
from os.path import isfile, join
from time import gmtime, strftime

def sendemail(article_title):
    if article_title == -1:
        print "already got it"
        return

    msg = MIMEMultipart()
    file_log = open('log', 'a')

    att1 = MIMEText(open('text/' + article_title + '.txt', 'rb').read(), 'base64',
        'gb2312')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename = "' +article_title +\
        '.txt' + '"'
    msg.attach(att1)
    msg['to'] = 'target1'
    msg['from'] = 'dhuo@tcd.ie'
    msg['subject'] = 'hello world'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('username', 'password')
        server.sendmail(msg['from'], msg['to'], msg.as_string())
        server.quit()
        print 'heihei'
        file_log.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\t" + \
            msg['to'] + article_title + '\n')
    except Exception, e:
        print str(e)
    msg['to'] = 'target2'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('username', 'password')
        server.sendmail(msg['from'], msg['to'], msg.as_string())
        server.quit()
        print 'heihei'
        file_log.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\t" + \
            msg['to'] + '\t' + article_title + '\n')
    except Exception, e:
        print str(e)
    file_log.close()


def getText():
    article = getContent()
    article_title = article['title']
    article_content = article['content']
    files = [f for f in listdir('text') if isfile(join('text', f))]
    if article_title + '.txt' in files:
        print "already there"
        return -1
    file_out = open('text/' + article_title + '.txt', 'w')
    file_out.write(article_content.encode("utf-8"))
    file_out.close()
    return article_title

if __name__ == '__main__':
    article_title = getText()
    sendemail(article_title)
