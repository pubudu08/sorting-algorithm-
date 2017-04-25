import unittest

from sorting_algorithms import counting_sort, bubble_sort, radix_sort


class Test(unittest.TestCase):
    def test_counting_sort(self):

        counting_sort_list = [6, 4, 3, 2, 1, 4, 3, 6, 6, 2, 4, 3, 4]
        k = 6
        counting_sort(counting_sort_list, k)
        for i in range(1, len(counting_sort_list)):
            if counting_sort_list[i - 1] > counting_sort_list[i]:
                self.fail("counting sort method fails.")

    def test_bubble_sort(self):
        bubble_sort_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        bubble_sort(bubble_sort_list)
        for i in range(1, len(bubble_sort_list)):
            if bubble_sort_list[i - 1] > bubble_sort_list[i]:
                self.fail("bubble_sort method fails.")

    def test_radix_sort(self):
        radix_sort_list = [18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2]
        radix_sort(radix_sort_list)
        for i in range(1, len(radix_sort_list)):
            if radix_sort_list[i - 1] > radix_sort_list[i]:
                self.fail("radix_sort method fails.")
