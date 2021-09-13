from TwitterAPI import TwitterAPI, TwitterPager
# try importing some critical thought for fuck's sake and stop worshiping some "technoking" fraudster
# https://en.wikipedia.org/wiki/Criticism_of_Tesla,_Inc
SEARCH_TERM = 'getting Trevor Milton for misleading'
PRODUCT = 'fullarchive'
LABEL = 'prod'
api = TwitterAPI(<consumer key>,
                 <consumer secret>,
                 <access token key>,
                 <access token secret>)
r = TwitterPager(api,'tweets/search/%s/:%s'  % (PRODUCT, LABEL), {'query':SEARCH_TERM})
for item in r.get_iterator():
    if 'text' in item:
        print(item)
    elif 'message' in item and item['code'] == 88:
        print('SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
        break
# https://twitter.com/hashtag/$TSLAQ?f=live