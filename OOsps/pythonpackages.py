from email.feedparser import headerRE
from imaplib import Literal

import prettytable
from prettytable import TableStyle
from prettytable.prettytable import VAlignType

table = prettytable.PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

table.add_column("cost_of_living",[123,456,678,987,567,678,567],"c",'t')

table.align = 'c'

print(table.get_string(fields = ['City name', 'Area']))
print(table.get_string(start = 0, end =3))

print(table)