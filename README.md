# Convert reading list files to CSV

Possible awk solution:
```bash
$ awk -v RS="" '!/^[A-Za-z]+\s[0-9]{4}$/ {gsub(/\n/, "|"); print $0}' readinglists/*.txt
```