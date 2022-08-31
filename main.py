from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv


with open("phonebook_raw.csv","r",encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)




if __name__ == '__main__':
    pprint(contacts_list)



