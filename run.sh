#!/bin/bash

echo "Running run.sh"
echo "Using go-flows to convert the pcap to a csv"
# go-flows run features 4tuple_bidi.json export csv output.csv source libpcap $1
echo "Done"

echo "Analysing the csv to detect network attacks"
python ./main.py output.csv
echo "Done"

echo "Find the result in the output.csv file"
