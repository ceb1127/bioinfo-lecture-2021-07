#!/usr/bin/python3

data = {"A":0, "C":0, "G":0, "T":0}

with open("covid19.fasta","r") as handle: 
	for line in handle:
		if line.startswith(">"):
			continue
		for base in line.strip():
			data[base] += 1

print(f"A: {data['A']}")
print(f"C: {data['C']}")
print(f"G: {data['G']}")
print(f"T: {data['T']}")
