# ssh_research
files and source code for a research paper I wrote based on ssh attack data

Contents:
===========
log_collector
      secure_logger.pl   -  the program used for capturing SSH data on the server.
      secure_logger.sh   -  the bash script used to restart secure_logger.pl if it crashed
      
data
       country_codes       -  how the countries sorted out during this research
       user_codes          -  how the users sourted out during this research
       secure2.csv.gz      -  the data file the analytics were run against - after the data was extracted
       secure_monitor.gz*  -  the raw logs captured by the secure_logger program on the server.  They were split using the UNIX Split command and 
                              can be reassembled by following this proceedure:
                              
                              cat secure_monitor.gz.partaa > secure_monitor.gz
                              cat secure_monitor.gz.partab >> secure_monitor.gz
                              cat secure_monitor.gz.partac >> secure_monitor.gz

                              gunzip secure_monitor.gz

data_extractor.py          -  parses the secure_monitor log and creates a csv for plotting data - also creates the user and country number mappings
plotdata/py                - plots the data 
read_data.py               - test program for plotting data
