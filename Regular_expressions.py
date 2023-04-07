import re
from pprint import pprint
import csv


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def create_text(contacts_list):
    full_name = r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)"
    subust_name = r"\1,\4,\7"
    phone = r'(8|\+7)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(?(\доб.)*\s*(\d+)*\)?'
    subust_phone = r'+7(\2)\3-\4-\5 \6\7'
    new_data = []
    for i in contacts_list:
        text = ','.join(i)
        text1 = re.sub(full_name, subust_name, text)
        new_str = re.sub(phone, subust_phone, text1)
        str_list = new_str.split(',')
        while len(str_list) > 7:
            str_list.remove('')
        new_data.append(str_list)
    return new_data


def double_delete(text):
    person_data = {}
    for data in text:
        if data[0] in person_data:
            con_val = person_data[data[0]]
            for ind in range(len(con_val)):
                if data[ind]:
                    con_val[ind] = data[ind]
        else:
            person_data[data[0]] = data
    return list(person_data.values())


if __name__ == '__main__':
    with open("phonebook.csv", "w", newline='') as f:
        datawriter = csv.writer(f, delimiter=';')
        datawriter.writerows(double_delete(create_text(contacts_list)))
