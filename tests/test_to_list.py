from unittest import TestCase, main
import tests.sources as sources

class ToListTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertListEqual(sources.range().to_list(), [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ])

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertListEqual(sources.rangeClosed().to_list(), [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])

    def test_create_sequence_from_array(self):
        self.assertListEqual(sources.array().to_list(), [ 1, 2, 3 ])

    def test_create_sequence_using_iterate(self):
        self.assertListEqual(sources.iterate().to_list(), [ 0, 1, 2, 3, 4 ])

    def test_create_sequence_using_of(self):
        self.assertListEqual(sources.of().to_list(), [ 0, 1, 2, 3 ])

    def test_create_sequence_using_empty(self):
        self.assertListEqual(sources.empty().to_list(), [  ])

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().to_list())

    def test_filter(self):
        self.assertListEqual(sources.filter().to_list(), [ 0, 2, 4 ])

    def test_map(self):
        self.assertListEqual(sources.map().to_list(), [ 0, 4, 8 ])

    def test_flatMap(self):
        self.assertListEqual(sources.flatMap().to_list(), [ 1, 2, 3, 4, 5, 6 ])

    def test_take(self):
        self.assertListEqual(sources.take().to_list(), [ 0, 2, 4, 6, 8, 10 ])

    def test_skip(self):
        self.assertListEqual(sources.skip().to_list(), [ 3, 4, 5 ])

    def test_takeWhile(self):
        self.assertListEqual(sources.takeWhile().to_list(), [ 1, 2, 4, 8, 16 ])

    def test_skipWhile(self):
        self.assertListEqual(sources.skipWhile().to_list(), [ 6, 7, 8, 9 ])

    def test_distinct_with_numbers(self):
        self.assertListEqual(sources.distinctNumbers().to_list(), [ 0, 2, 5, 10 ])

    def test_distinct_with_objects(self):
        self.assertListEqual(sources.distinctObjects().to_list(), [ 'asd', 'a', 'ba' ])

    def test_sort_with_numbers(self):
        self.assertListEqual(sources.descendingNumbers().to_list(), [ 4, 3, 2, 1, 0 ])

if __name__ == '__main__':
    main()