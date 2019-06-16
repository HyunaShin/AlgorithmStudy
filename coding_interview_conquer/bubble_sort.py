import unittest

def bubblesort(unsorted_list):
    '''
    버블소트는 인접한 두 자료를 차순에 맞게 교환하는 알고리즘이다.
    리스트의 길이 - 1만큼 loop을 돌아야하며
    O(N^2)의 퍼포먼스, O(1)의 공간복잡도를 가진다
    '''
    for i in range(len(unsorted_list)-1):
        for j in range(len(unsorted_list) -1):
            if unsorted_list[j] > unsorted_list[j+1]:
                tmp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = tmp
    return unsorted_list


class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([6, 5, 4, 3, 2, 1]))

if __name__ == "__main__":
    unittest.main()
