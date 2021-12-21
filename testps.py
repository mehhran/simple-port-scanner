import portscanner

hosts = ['www.google.com', 'www.yahoo.com', 'www.msn.net']

port = 80

for h in hosts:
    portscanner.ps(h,port)