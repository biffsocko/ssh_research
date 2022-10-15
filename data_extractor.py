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
import calendar

######################################################
# MAIN
######################################################
gi = pygeoip.GeoIP('/home/biff/notebook/geoip-dat/geoipdat/GeoLiteCity.dat')
input="secure_monitor"
output="secure2.csv"

country_ledger="country_codes"
country_dict={}
country_counter=0

user_ledger="user_codes"
user_dict={}
user_counter=0

abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
DEBUG=0
stillrunning=0

#########################################################
# open the input and output files
#########################################################
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

try:
    countrylisting=open(country_ledger, 'w')
except IOError:
    print("could not open "+country_ledger+" exiting")
    exit(1)

try:
    userlisting=open(user_ledger, 'w')
except IOError:
    print("could not open "+user_ledger+" exiting")
    exit(1)


for line in infile:

    #########################################################
    # print out a dot every 10000 entries to show that this 
    # is still running
    #########################################################
    stillrunning = stillrunning +1
    if(stillrunning == 10000):
        print(".",end=" ", flush=True)
        stillrunning=0

    #########################################################
    # remove bad formating from the logs
    #########################################################
    if "opening log" in line:
        continue;
    tmp=line.split()

    #########################################################
    # remove bad formating from the logs
    #########################################################
    if(len(tmp) != 8):
        if(len(tmp) != 10):
            continue
    
    #########################################################
    # invalid is when user does not exist
    #########################################################
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
        #########################################################
        # we get here when the user exists but failed to 
        # login
        #########################################################
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

    #########################################################
    # give country a numeric value
    #########################################################
    if(country is None):
       country="unknown" 
    
    if(country in country_dict):
        country=str(country_dict[country])
    else:
        countrylisting.write(country+" "+str(country_counter)+"\n")
        if(DEBUG > 1):
            print(country+" "+str(country_counter))
        country_dict[country] = country_counter
        country=str(country_counter)
        country_counter = country_counter + 1
       
    #########################################################
    # give user a numeric value
    #########################################################
    if(user in user_dict):
        user=str(user_dict[user])
    else:
        userlisting.write(user+" "+str(user_counter)+"\n")
        if(DEBUG > 1):
            print(user+" "+str(user_counter))
        user_dict[user] = user_counter
        user=str(user_counter)
        user_counter = user_counter + 1
    

    #########################################################
    # Make day a numeral for the import csv
    #########################################################
    if(day == "Sun"):
        day="0"
    elif(day == "Mon"):
        day="1"
    elif(day == "Tue"):
        day="2"
    elif(day == "Wed"):
        day="3"
    elif(day == "Thu"):
        day="4"
    elif(day == "Fri"):
        day="5"
    elif(day == "Sat"):
        day="6"
        
        
    #########################################################
    # make Month a numeral for the import csv
    #########################################################
    month = str(abbr_to_num[month])

    if(DEBUG > 0):
        print(day+","+month+","+date+","+time+","+timezone+","+year+","+user+","+ip+","+country)
    out.write(day+","+month+","+date+","+time+","+timezone+","+year+","+user+","+ip+","+country+"\n")


countrylisting.close()
userlisting.close()
out.close()
infile.close()
exit(0)

