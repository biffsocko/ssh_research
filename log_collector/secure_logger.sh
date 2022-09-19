#!/bin/sh

ps -eaf | grep secure_logger.pl | grep -v grep > /dev/null 2>&1
if [ $? -ne 0 ]
then
    nohup /root/bin/secure_logger.pl &
fi
exit 0
