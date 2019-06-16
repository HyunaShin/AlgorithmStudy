import unittest

def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        minim_idx = i
        for j in range(i,len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[minim_idx]:
                minim_idx = j
            else:
                pass

        tmp_val = unsorted_list[minim_idx]
        unsorted_list[minim_idx] = unsorted_list[i]
        unsorted_list[i] = tmp_val

    return unsorted_list

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([6, 5, 4, 3, 2, 1]))

if __name__ == "__main__":
    unittest.main()
