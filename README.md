# ssh_research
files and source code for a research paper I wrote based on ssh attack data


# extracting the raw data files:

the secure_monitor raw data logs were split into mulitpile files using the linux split command, to stich themback together just do this:
cat secure_monitor.gz.partaa > secure_monitor.gz
cat secure_monitor.gz.partab >> secure_monitor.gz
cat secure_monitor.gz.partac >> secure_monitor.gz

gunzip secure_monitor.gz
