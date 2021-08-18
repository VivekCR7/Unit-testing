# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

"""
Approach:

For this task we need to plot the bar plot for the number
of registration vs district.

So, first I manually created the zipcode vs district .csv
file, then created a function in which I converted that .csv
file into a simple dictionary with the pincode as keys and
its corresponding district as values
eg: {'pincode': 'district'}

then I created one more helper funciton to short my large data
cause we only need to work for the year 2015. I just iterated
over my list of dictionary and created a dictionary for counting
and looked for the year=2015 and the address pincode and counted
the matching district.
eg: {'district_for_year_2015': count}

then I used one more function to plot the barplot using the
"""
from transform import get, get_zip_district_dic

dataset = get()


def get_the_district_count(arr):
    zip_district = get_zip_district_dic()

    district_count = {}
    for data in arr:
        if int(data['DATE_OF_REGISTRATION'][0:4]) != 2015:
            continue

        address = data['Registered_Office_Address']
        zipcode = address[len(address)-6:]

        if zipcode in zip_district:
            if zip_district[zipcode] not in district_count:
                district_count[zip_district[zipcode]] = 1
            else:
                district_count[zip_district[zipcode]] += 1

    keys = list(district_count.keys())
    values = list(district_count.values())

    return keys, values
