from flask import Markup
from modules.tableGen import SimpleTable


def talkgroups():
    pageContent = Markup(
        '''<li><a href="/talkgroups/TG50100">TG50100</a></li>
            <li><a href="/talkgroups/index">TG50105</a></li>
            <li><a href="/talkgroups/index">TG50110</a></li>
            <li><a href="/talkgroups/index">TG50115</a></li>
            <li><a href="/talkgroups/index">TG50120</a></li>'''
    )
    return pageContent

def tableContent():
    pageContent = Markup(SimpleTable([['12:03', 'KR0SIV', 'TG50100', 'WB5OD', '24'], ['12:04', 'N1TVI', 'TG50100', 'WB5OD', '12']]))
    return pageContent

def upTime():
    import uptime
    import datetime
    sec = str(uptime.uptime())
    stripped = sec.split(".", 1)[0]
    srvUptime = str(datetime.timedelta(seconds=int(stripped)))
    #return srvUptime
    return '8:23:15'