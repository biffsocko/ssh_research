#!/usr/bin/perl
####################################################
# TR Murphy
# secure_logger.pl
#
# captures IP addresses from failed login attempts
# through ssh.  The data can be used later for
# analysis.  Most attempts are from ssh brute
# force attacks.  This is generated from
# /var/log/secure
####################################################


use File::Tail;

my $SECLOG="/var/log/secure";
my $MONLOG="/var/log/secure_monitor";
my $DATE = undef;
chomp($DATE=`date`);


if(! -f $SECLOG){
    print "$SECLOG is missing.  exiting\n";
    exit(1);
}

if(!(open(Fp, ">>$MONLOG"))){
    print "can not open $MONLOG .. exiting\n";
    exit(1);
}

autoflush Fp 1;
autoflush STDOUT 1;


print Fp "opening log $DATE\n";

my $file=File::Tail->new(name=>$SECLOG, maxinterval=>300, adjustafter=>7);
while (defined($line=$file->read)) {
     if($line =~m/(.*)(Failed password for)(.*)(from )(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)/g){
         chomp($DATE=`date`);
         my $user=$3;
         my $ip=$5;
         print Fp "$DATE - $user - $ip\n";
    }
}

exit(0);


