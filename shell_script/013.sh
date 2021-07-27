#!/bin/bash

for gene in `cat genelist.txt`
do
	python3 012.py ${gene}
done

