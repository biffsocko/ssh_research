#!/home/biff/notebook/jupyterenv/bin/python3
###################################################
# TR Murphy
# data_extractor.py
#
# this parses the secure_monitor file and pulls
# out inconsistancies and creates a csv file
#
# this version added mapping the country code to
# ip address
###################################################

import pygeoip

######################################################
# MAIN
######################################################
gi = pygeoip.GeoIP('/home/biff/notebook/geoip-dat/geoipdat/GeoLiteCity.dat')
input="secure_monitor"
output="secure.csv"

try:
    infile = open(input, "r")
except IOError:
    print("could not open "+input+" exiting")
    exit(1)

try:
   out=open(output,'w')
except IOError:
    print("could not open "+outfile+" exiting")
    exit(1)


for line in infile:
    # remove bad formating from the logs
    if "opening log" in line:
        continue;
    tmp=line.split()

    # remove bad formating from the logs
    if(len(tmp) != 8):
        if(len(tmp) != 10):
            continue

    # invalid is when user does not exist
    if("invalid" in line):
        day=tmp[0]
        month=tmp[1]
        date=tmp[2]
        time=tmp[3]
        timezone=tmp[4]
        year=tmp[5]
        user=tmp[9]
        ip=tmp[11]
    else:
        # we get here when the user exists but failed to 
        # login
        day=tmp[0]
        month=tmp[1]
        date=tmp[2]
        time=tmp[3]
        timezone=tmp[4]
        year=tmp[5]
        user=tmp[7]
        ip=tmp[9]
    
    country=gi.country_code_by_addr(ip)
    #country=gi.country_name_by_addr(ip)

    if(country is None):
       country="unknown" 

    print(day+","+month+","+date+","+time+","+timezone+","+year+","+user+","+ip+","+country)
    out.write(day+","+month+","+date+","+time+","+timezone+","+year+","+user+","+ip+","+country+"\n")

exit(0)
