# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

from transform import get, get_zip_district_dic

dataset = get()
zip_data = get_zip_district_dic()


# function to check if the dataset has only years from 2000 to 2021
def year_array(arr, left, right):
    year_arr = []
    if right < left:
        return "Impossible!!"

    for i in range(left, right+1):
        date = int('20' + arr[i]["DATE_OF_REGISTRATION"][6:])
        year_arr.append(date)

    return year_arr


# function to check if the district is getting printed respective to there pincode
def check_district(arr, pincode):
    if pincode not in arr:
        return "Invalid Pincode"

    return arr[pincode]


# function to check if group is creating properly
def check_group_number(arr, left, right):
    if right < left:
        return "Impossible!!"

    return arr[left:right+1]


# function to check the number of companies respective to the year
def check_count_for_companies(keys, values, registered_year):
    if registered_year not in keys:
        return "Invalid Year"

    return values[keys.index(registered_year)]


# function to check the number of companies respective to there district
def check_count_for_district(keys, values, district_name):
    if district_name not in keys:
        return "No such district"

    return values[keys.index(district_name)]


# function to check the total and  principal activity for a particular year
def check_properties_in_year(arr, year_num):
    if year_num not in arr:
        return "Invalid Year"

    return arr[year_num]
