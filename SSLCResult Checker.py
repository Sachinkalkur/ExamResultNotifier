#!/usr/bin/python
from bs4 import BeautifulSoup
import re
import urllib2
import cookielib
import time
import sys


    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
        print "SMS has been sent."
    except IOError:
        print "Error while sending message"
        sys.exit(1)


while True:
    SSLcUrl = 'http://www.karresults.nic.in/'
    parsed_html = urllib2.urlopen(SSLcUrl)
    whole_html = parsed_html.read()
    soup = BeautifulSoup(whole_html, 'html.parser')
    output = soup.findAll('a')
    print output
    string_match = "PUC Results"
    for links in output:
        match = re.findall(string_match, str(links))
        print match
        if match:
            second_string = 'href="#"'
            second_match = re.findall(second_string, str(links))
            print second_match
            if second_match == []:
                sys.exit(1)
            else:
                print "Rechecking in 15 minutes.............."
                print "Start : %s" % time.ctime()
                time.sleep(90)
                print "End : %s" % time.ctime()


