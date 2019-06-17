import unittest

def insertion_sort(unsorted_list):
    '''
    내가 가진 카드 패를 오름차순으로 정렬한다고 생각하자.
    이 때, 인덱스를 순차대로 돌아가며 뽑고, 들어갈 위치를 탐색한다.
    탐색 완료 후 들어 갈 위치를 찾으면, 그자리에 카드를 둔다.
    이후 이미 탐색이 끝난 카드들은 순서가 밀리게 된다.
    '''
    for index, value_to_swap in enumerate(unsorted_list):
        current_point = index
        while index > 0 and unsorted_list[index-1] > unsorted_list[index]:
            unsorted_list[index-1] , unsorted_list[index] = unsorted_list[index] , unsorted_list[index-1]
            index -=1

    return unsorted_list

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([6, 5, 4, 3, 2, 1]))

if __name__ == "__main__":
    unittest.main()
