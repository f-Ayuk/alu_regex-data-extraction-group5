#!/usr/bin/python
import re

# sample string with product codes
string = "The following products are on sale: ABC123, XYZ789, PQR456, LMN234"

# regular expression for product codes
regex = "[A-Z] {3}\\d {3}"

# find all matches in the string
matches = re.findall(regex, string)

# print the matches
print(matches)
