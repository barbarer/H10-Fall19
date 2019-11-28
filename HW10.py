import matplotlib.pyplot as plt
import sqlite3
import unittest

# Your name:
# The name(s) of anyone you worked with:


##############################################################################
# [Part 1]
##############################################################################
# Complete the get_category_dict(..) function that accepts the filename of the
# database as a parameter, and returns a dictionary with the number of
# restaurants that are in each category. The keys should be the category names
# and the values should be the number of restaurants in that category.
# The dictionary should look like:
#
# {'American (New)': 1, 'American (Traditional)': 1,'Bakeries': 2...}
#
# (HINT: If you did the extra credit for HW9, you can modify and re-use
# that code.)
#
# Your function must pass all the unit tests to get full credit.
###############################################################################

def get_category_dict(db_filename):
    pass

###############################################################################
# [Part 2]
###############################################################################
# Complete the function barchart_retaurants_by_cat(..), which takes in a
# dictionary created by the function in Part 1, and uses matplotlib functions
# to draw a bar chart with restaurant categories on the x axis, and the
# number of restaurants in that category on the y axis. The chart must
# have appropriate axis labels and a title.
#
# Sort the X axis alphabetically from left-to-right. See the directions for an
# example of what your chart should look like.
#
# Finally, this function should sort the dictionary items alphabetically and
# return the resulting list of tuples. Your list should look like:
#
# [('American (New)', 1), ('American (Traditional)', 1), ('Bakeries', 2)…]
#
#
# Submit an image file of your bar chart to Canvas, along with your
# repository link.
###############################################################################


def barchart_restaurants_by_cat(cat_dict):
    pass

    # Use these to make sure that your x axis labels fit on the page
    # plt.xticks(rotation=90)
    # plt.tight_layout()


##############################################################################
# [Extra Credit]
##############################################################################
# Complete function mean_rating_by_category(..) to plot a barchart of the mean
# rating for each restaurant category. Put the restaurant on the x axis and
# the average rating on the y axis. Sort the x axis in descending order from
# left-to-right The chart must have appropriate axis labels and a title.
# See the directions for a sample chart.
#
# Finally, this function should return a dictionary where the keys are
# restaurant categories and the values are the mean ratings for the
# corresponding category. Your dictionary should look like this:
#
# {'American (New)': 4.0, 'American (Traditional)': 3.5, 'Bakeries': 4.5…}
#
# Submit an image file of your chart to Canvas.
##############################################################################


def mean_rating_by_category(db_filename):
    pass

# #############################################################################
#                        DO NOT MODIFY THE TEST CASES                         #
#                                                                             #
# Don't forget to uncomment the one for the extra credit if you are           #
# attempting it.                                                              #
# #############################################################################


class TestHW10(unittest.TestCase):

    def test_get_category_dict(self):
        category_dict = get_category_dict('restaurants.db')
        answer_dict = {
            'American (New)': 1,
            'American (Traditional)': 1,
            'Bakeries': 2,
            'Beer Bar': 1,
            'Beer, Wine & Spirits': 2,
            'Breweries': 4,
            'Chicken Wings': 1,
            'Delis': 2,
            'Farmers Market': 1,
            'Italian': 5,
            'Pizza': 20,
            'Pubs': 3,
            'Salad': 2,
            'Sandwiches': 1,
            'Smokehouse': 1,
            'Sports Bars': 1,
            'Tapas Bars': 1,
            'Vegan': 1
        }
        self.assertEqual(type(category_dict), dict)
        self.assertEqual(len(category_dict), 18)
        self.assertDictEqual(category_dict, answer_dict)

    def test_barchart_restaurants_by_cat(self):
        print(
            """
            Passing this test case does NOT guarentee you full points.
            You MUST check your image against the expected output.
            """
        )
        sorted_data = barchart_restaurants_by_cat(get_category_dict(
            'restaurants.db')
        )
        answer_data = [
            ('American (New)', 1),
            ('American (Traditional)', 1),
            ('Bakeries', 2),
            ('Beer Bar', 1),
            ('Beer, Wine & Spirits', 2),
            ('Breweries', 4),
            ('Chicken Wings', 1),
            ('Delis', 2),
            ('Farmers Market', 1),
            ('Italian', 5),
            ('Pizza', 20),
            ('Pubs', 3),
            ('Salad', 2),
            ('Sandwiches', 1),
            ('Smokehouse', 1),
            ('Sports Bars', 1),
            ('Tapas Bars', 1),
            ('Vegan', 1)
        ]

        self.assertEqual(type(sorted_data), list)
        self.assertEqual(type(sorted_data[0]), tuple)
        self.assertEqual(len(sorted_data), 18)
        self.assertEqual(sorted_data, answer_data)

    # UNCOMMENT THIS IF YOU ARE ATTEMPTING THE EXTRA CREDIT
    # ######################################################
    # def test_mean_rating_by_category(self):
    #     print(
    #         """
    #         Passing this test case does NOT guarentee you full points.
    #         You MUST check your image against the expected output.
    #         """
    #     )
    #     mean_dict = mean_rating_by_category('restaurants.db')
    #     answer_dict = {
    #         'American (New)': 4.0,
    #         'American (Traditional)': 3.5,
    #         'Bakeries': 4.5,
    #         'Beer Bar': 3.5,
    #         'Beer, Wine & Spirits': 4.5,
    #         'Breweries': 3.75,
    #         'Chicken Wings': 4.5,
    #         'Delis': 4.25,
    #         'Farmers Market': 5.0,
    #         'Italian': 3.5,
    #         'Pizza': 3.825,
    #         'Pubs': 4.0,
    #         'Salad': 4.0,
    #         'Sandwiches': 4.0,
    #         'Smokehouse': 4.5,
    #         'Sports Bars': 4.0,
    #         'Tapas Bars': 4.0,
    #         'Vegan': 4.0
    #     }
    #     self.assertEqual(type(mean_dict), dict)
    #     self.assertEqual(len(mean_dict), 18)
    #     self.assertDictEqual(mean_dict, answer_dict)


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
