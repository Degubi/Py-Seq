from unittest import TestCase, main
import tests.sources as sources

def forEachOpHelper(sequence):
    result = []

    sequence.for_each(lambda k: result.append(k))

    return result


class ForEachTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertListEqual(forEachOpHelper(sources.range()), [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ])

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertListEqual(forEachOpHelper(sources.rangeClosed()), [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])

    def test_create_sequence_from_array(self):
        self.assertListEqual(forEachOpHelper(sources.array()), [ 1, 2, 3 ])

    def test_create_sequence_using_iterate(self):
        self.assertListEqual(forEachOpHelper(sources.iterate()), [ 0, 1, 2, 3, 4 ])

    def test_create_sequence_using_of(self):
        self.assertListEqual(forEachOpHelper(sources.of()), [ 0, 1, 2, 3 ])

    def test_create_sequence_using_empty(self):
        self.assertListEqual(forEachOpHelper(sources.empty()), [  ])

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: forEachOpHelper(sources.terminated()))

    def test_filter(self):
        self.assertListEqual(forEachOpHelper(sources.filter()), [ 0, 2, 4 ])

    def test_map(self):
        self.assertListEqual(forEachOpHelper(sources.map()), [ 0, 4, 8 ])

    def test_flatMap(self):
        self.assertListEqual(forEachOpHelper(sources.flatMap()), [ 1, 2, 3, 4, 5, 6 ])

    def test_take(self):
        self.assertListEqual(forEachOpHelper(sources.take()), [ 0, 2, 4, 6, 8, 10 ])

    def test_skip(self):
        self.assertListEqual(forEachOpHelper(sources.skip()), [ 3, 4, 5 ])

    def test_takeWhile(self):
        self.assertListEqual(forEachOpHelper(sources.takeWhile()), [ 1, 2, 4, 8, 16 ])

    def test_skipWhile(self):
        self.assertListEqual(forEachOpHelper(sources.skipWhile()), [ 6, 7, 8, 9 ])

    def test_distinct_with_numbers(self):
        self.assertListEqual(forEachOpHelper(sources.distinctNumbers()), [ 0, 2, 5, 10 ])

    def test_distinct_with_objects(self):
        self.assertListEqual(forEachOpHelper(sources.distinctObjects()), [ 'asd', 'a', 'ba' ])

    def test_sort_with_numbers(self):
        self.assertListEqual(forEachOpHelper(sources.descendingNumbers()), [ 4, 3, 2, 1, 0 ])

if __name__ == '__main__':
    main()