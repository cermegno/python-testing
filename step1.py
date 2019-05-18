import redislite
r = redislite.StrictRedis()
r.set('foo', 'bar')
print r.get('foo')
r.hmset('survey1',{'division':'ENT','state':'NSW','feedback':'hello world'})
r.hmset('survey2',{'division':'COMM','state':'NSW','feedback':'great'})
r.hmset('survey3',{'division':'ENT','state':'VIC','feedback':'awesome'})
response = "Full Report\n"
for eachsurvey in r.keys('survey*'):
    response += "Division : " + r.hget(eachsurvey,'division') + "<br>\n"
    response += "State    : " + r.hget(eachsurvey,'state') + "<br>\n"
    response += "Feedback : " + r.hget(eachsurvey,'feedback') + "<br>\n"
    response += " ----------------------<br>"
print response
