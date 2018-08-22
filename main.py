import csv

import pandas as pd
print pd.read_csv('/Users/ronkerbs/PycharmProjects/FinalProject/data1.tsv', sep = "\t")


#
# with open('/Users/ronkerbs/PycharmProjects/FinalProject/data1.tsv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
#     for row in spamreader:
#         print ', '.join(row)

# print "fdfdgf"