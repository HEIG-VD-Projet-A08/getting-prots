import requests
import sys
import csv
import os

name = str(sys.argv[1])

size = sys.argv[2]
nameData = "Data_" + str(size) + ".txt"
nameFile = name + ".txt"
path = "./"


dataExists = os.path.isfile(path + nameData)


if dataExists:
	print("File already exists.")
else:
	file = open(nameData, "w")

	print("Getting data...")
	r = requests.get("https://www.uniprot.org/uniprot/?query=&sort=score&columns=id,length,comment(SUBCELLULAR LOCATION)&format=tab&limit="+ str(size))
	print("Status of the request: " + str(r.status_code))


	file.write(r.text)
	file.close()


file = open(nameData, "r+")
csv_file = open(nameFile, "w")
list_of_prots = list(csv.reader(file, delimiter='\t'))


for i in range(1,len(list_of_prots)):
	if not list_of_prots[i][2]:
		list_of_prots[i][2] = 0
	else:
		list_of_prots[i][2] = 1

csvWriter = csv.writer(csv_file, delimiter='\t')

for item in list_of_prots:
	csvWriter.writerow(item)


file.close()
csv_file.close()
