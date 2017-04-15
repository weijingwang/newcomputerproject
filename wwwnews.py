import webbrowser

print ("Answer the following questions to find the Top World news on any specified Date (Use Numbers - EX: 12/14/2002 MONTH/DAY/FULL YEAR)")
print ("This program relies on The Wall Street Journal's Digital Archive for the News")
month = int(raw_input("Month:"))
year = int(raw_input("Year:"))
day = int(raw_input("Day:"))
date = "The Top World News On %s/%s/%s" % (month, day, year) 
print date
webbrowser.open("http://www.wsj.com/public/page/archive-%s-%s-%s.html" % (year, month, day))


