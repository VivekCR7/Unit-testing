# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring

import unittest
import data
from transform import get, get_zip_district_dic
from histogram_of_authorized_cap import get_the_grouped_data as h
from barplot import get_the_dictionary as b
from bar_chart_for_year_2015 import get_the_district_count as ba
from grouped_bar_plot import get_the_combined_dictionary as g

dataset = get()
zip_data = get_zip_district_dic()
grouped_data = h(dataset)
year, year_count = b(dataset)
district, district_count = ba(dataset)
dictionary = g(dataset)


class TestData(unittest.TestCase):

    def test_year_array(self):
        self.assertEqual(data.year_array(dataset, 7, 10),
                         [2005, 2005, 2000, 2014])
        self.assertEqual(data.year_array(dataset, 1, 5),
                         [2004, 2011, 2011, 2004, 2009])
        self.assertEqual(data.year_array(dataset, 5, 1),
                         "Impossible!!")

    def test_check_district(self):
        self.assertEqual(data.check_district(zip_data, '414001'), 'Ahmednagar')
        self.assertEqual(data.check_district(zip_data, '401107'), 'Thane')
        self.assertEqual(data.check_district(
            zip_data, '414142'), 'Invalid Pincode')

    def test_check_group_number(self):
        self.assertEqual(data.check_group_number(
            grouped_data, 1, 3), [2, 5, 5])
        self.assertEqual(data.check_group_number(
            grouped_data, 5, 10), [4, 5, 5, 4, 2, 4])
        self.assertEqual(data.check_group_number(
            grouped_data, 10, 3), "Impossible!!")

    def test_check_count_for_companies(self):
        self.assertEqual(data.check_count_for_companies(
            year, year_count, 2000), 8920)
        self.assertEqual(data.check_count_for_companies(
            year, year_count, 2021), 7668)
        self.assertEqual(data.check_count_for_companies(
            year, year_count, 1999), "Invalid Year")

    def test_check_count_for_district(self):
        self.assertEqual(data.check_count_for_district(
            district, district_count, "Aurangabad"), 198)
        self.assertEqual(data.check_count_for_district(
            district, district_count, "Thane"), 459)
        self.assertEqual(data.check_count_for_district(
            district, district_count, "New york"), "No such district")

    def test_check_properties_in_year(self):
        self.assertEqual(data.check_properties_in_year(dictionary, 2000), {
                         'Total': 8920, 'Other': 6982, 'Manufacture': 1556,
                         'Construction': 382})
        self.assertEqual(data.check_properties_in_year(dictionary, 2012), {
                         'Total': 17312, 'Other': 12541, 'Manufacture': 2911,
                         'Construction': 1860})
        self.assertEqual(data.check_properties_in_year(
            dictionary, 1927), "Invalid Year")


if __name__ == '__main__':
    unittest.main()
