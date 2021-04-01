from unittest import TestCase, main
import tests.sources as sources

class ToListChunkedTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertListEqual(sources.range().chunk(3).to_list(), [[ 0, 1, 2 ], [ 3, 4, 5 ], [ 6, 7, 8 ], [ 9 ]])

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertListEqual(sources.rangeClosed().chunk(6).to_list(), [[ 0, 1, 2, 3, 4, 5 ], [ 6, 7, 8, 9, 10 ]])

    def test_create_sequence_from_array(self):
        self.assertListEqual(sources.array().chunk(1).to_list(), [[ 1 ], [ 2 ], [ 3 ]])

    def test_create_sequence_using_iterate(self):
        self.assertListEqual(sources.iterate().chunk(2).to_list(), [[ 0, 1 ], [ 2, 3 ], [ 4 ]])

    def test_create_sequence_using_of(self):
        self.assertListEqual(sources.of().chunk(10).to_list(), [[ 0, 1, 2, 3 ]])

    def test_create_sequence_using_empty(self):
        self.assertListEqual(sources.empty().chunk(42).to_list(), [])

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().chunk(420).to_list())

    def test_filter(self):
        self.assertListEqual(sources.filter().chunk(2).to_list(), [[ 0, 2 ], [ 4 ]])

    def test_map(self):
        self.assertListEqual(sources.map().chunk(3).to_list(), [[ 0, 4, 8 ]])

    def test_flatMap(self):
        self.assertListEqual(sources.flatMap().chunk(4).to_list(), [[ 1, 2, 3, 4 ], [ 5, 6 ]] )

    def test_take(self):
        self.assertListEqual(sources.take().chunk(5).to_list(), [[ 0, 2, 4, 6, 8 ], [ 10 ]])

    def test_skip(self):
        self.assertListEqual(sources.skip().chunk(1).to_list(), [[ 3 ], [ 4 ], [ 5 ]])

    def test_takeWhile(self):
        self.assertListEqual(sources.takeWhile().chunk(2).to_list(), [[ 1, 2 ], [ 4, 8 ], [ 16 ]])

    def test_skipWhile(self):
        self.assertListEqual(sources.skipWhile().chunk(3).to_list(), [[ 6, 7, 8 ], [ 9 ]])

    def test_distinct_with_numbers(self):
        self.assertListEqual(sources.distinctNumbers().chunk(20).to_list(), [[ 0, 2, 5, 10 ]])

    def test_distinct_with_objects(self):
        self.assertListEqual(sources.distinctObjects().chunk(2).to_list(), [[ 'asd', 'a' ], [ 'ba' ]])

    def test_sort_with_numbers(self):
        self.assertListEqual(sources.descendingNumbers().chunk(3).to_list(), [[ 4, 3, 2 ], [ 1, 0 ]])

if __name__ == '__main__':
    main()