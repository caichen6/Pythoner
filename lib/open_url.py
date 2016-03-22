import urllib2
import urllib
url = 'http://itsm3.management.ccb/CAisd/pdmweb3.exe?action=Login'

response = urllib2.urlopen('http://itsm3.management.ccb/CAisd/pdmweb3.exe')
html = response.read()
print html



'''


values = {
    'target':'http://itsm3.management.ccb/CAisd/pdmweb3.exe',
    'SMENC' : 'UTF-8',
    'SMLOCALE':'US-EN',
    'APPID':'258783471',
    'smquerydata':'',
    'smauthreason':'0',
    'smagentname':'xfapfyNR5ovO5tcj0C1QhDqHPBN/z/Vg/7YoR+7KBn7SgUSz3jcc0yxO9MU8Z+ji',
    'postpreservationdata':'',
    'smusrmsg':'',
    "j_username":'caichen2.zh',
    "j_userpwd":'caichen123'
    }

cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
f=opener.open(url)
response = urllib2.Request(url,data)



##data=urllib.urlencode(values)
print data
##req = urllib2.Request(url,data)
response = urllib2.urlopen(url,data)
page = response.read()
print page
    
'''

'''

response = urllib2.urlopen('http://itsm3.management.ccb/CAisd/pdmweb3.exe')
html = response.read()
print html
'''
