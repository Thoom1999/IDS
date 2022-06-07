#!/bin/bash

go-flows run features 4tuple_bidipcap2pkts.json export csv output.csv source libpcap $1

