# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

"""
Approach:

I read the csv file with the help of DictReader from python csv library. Intially the data contains
of around 4 lakhs rows which was a lot. so I tried to shortened my data and considered only last
21 years of data from 2000 to 2021.

So, I just iterate over the my DictReader and look for the year. if year was between 2000 to 2001
then I appended that row in my list of dictionary.
"""

from csv import DictReader as d


def get():
    updated_dataset = []
    with open('/Users/vivekcr7/Desktop/projects/Company_Master/dataset/Maharashtra.csv',
              'r', encoding='latin1') as csv_file:
        dataset = d(csv_file)

        for data in dataset:
            try:
                if data['DATE_OF_REGISTRATION'] == 'NA':
                    continue

                if int(data['DATE_OF_REGISTRATION'][6:]) <= 21:
                    updated_dataset.append(data)
                else:
                    continue

            # some date format was YYYY-MM-DD so it was giving ValueError so I skipped that row.
            except ValueError:
                continue

    return updated_dataset


def get_zip_district_dic():
    zip_district_arr = []
    with open('/Users/vivekcr7/Desktop/projects/Company_Master/dataset/district_zip.csv',
              'r', encoding="UTF-8") as csv_file:
        csv_reader = d(csv_file)
        for data in csv_reader:
            zip_district_arr.append(data)

    zip_district_dictionary = {}

    for data in zip_district_arr:
        if data['Pin Code'] not in zip_district_dictionary:
            zip_district_dictionary[data['Pin Code']] = data['District']

    return zip_district_dictionary
