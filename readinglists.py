import csv
import os
import re

def write_to_csv(csvfile, list_input):

	try:
		with open(csvfile, "a", newline='') as fopen:
			csv_writer = csv.writer(fopen, quoting=csv.QUOTE_ALL)
			csv_writer.writerow(list_input)

	except:
		return False

def extract(rootdir, csvfile):
	records = []
	record = []
	month = ""
	recordstr = ""

	try:
		for dirpath, dirnames, filenames in os.walk(rootdir):
			for filename in filenames:
				f = open(os.path.join(dirpath, filename), "r", encoding="utf-8-sig", errors="ignore")
				for line in f:
					regex = re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s[0-9]{4}')
					match = regex.search(line)
					if match:
						month = line.rstrip().lstrip()
						print(month)
						record = []
						recordstr = ""
					elif line == "\n" or line == "\r\n":
						if len(record) > 1:
							record.insert(0, month)
							if len(record) < 6:
								record += [''] * (6 - len(record))
							write_to_csv(csvfile, record)
						record = []
						recordstr = ""
					else:
						record.append(line.rstrip().lstrip())
				f.close()
		return True

	except Exception as e:
		return e

if __name__ == "__main__":
	rootdir = './readinglists'
	csvfile = "readinglists.csv"
	file_to_delete = open(csvfile, "w")
	file_to_delete.close()
	header = ["month", "title", "author", "publisher", "format", "isbn_or_year"]
	write_to_csv(csvfile, header)
	result = extract(rootdir, csvfile)
	if result == True:
		print("All done")
	else:
		print(f"Something went wrong - {result}")
