#!/bin/bash

# $1 = bucket
# $2 = prefix
# s3 = filename

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.
$1=filename

aws s3 ls s3://$2 --recursive | grep $1 | awk '{print $4}' > s3_path

while read line
do
	aws s3 cp $1 `echo 's3://hli-workflow-sdrad-pdx/'$(dirname $line)'/'` --sse;
done < s3_path










