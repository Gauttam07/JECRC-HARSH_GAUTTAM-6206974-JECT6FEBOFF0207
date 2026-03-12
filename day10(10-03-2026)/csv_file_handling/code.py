import csv
from datetime import date

file = open('expense.csv', 'a+')
r = csv.reader(file)
#w = csv.writer(file)
# w.writerow(['Date', 'Category', 'Amount'])
# w.writerows(
#     [
#         [date.today(), 'Travel', 2000],
#         [date.today(), 'Food', 550],
#         [date.today(), 'Entertainment', 1700]
#     ]
# )
file.seek(0)
print(list(r))
file.close()