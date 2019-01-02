import datetime
import os
import re


def response(flow):
    with open('/tmp/linked-in-names-%s.txt' % datetime.datetime.now().date(), "a") as f:
        names = re.findall(r'firstName":"[a-zA-Z:",. ]+',flow.response.text)
        for name in names:
            clean = name.lstrip().rstrip().replace('firstName":"','').replace('","lastName":"',' ').replace('","','').lower()
            f.write(clean + "\n")
