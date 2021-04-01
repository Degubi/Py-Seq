from unittest import TestCase, main
import tests.sources as sources

class MaxTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().max(), 9)

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().max(), 10)

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().max(), 3)

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().max(), 4)

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().max(), 3)

    def test_create_sequence_using_empty(self):
        self.assertIsNone(sources.empty().max())

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().max())

    def test_filter(self):
        self.assertEqual(sources.filter().max(), 4)

    def test_map(self):
        self.assertEqual(sources.map().max(), 8)

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().max(), 6)

    def test_take(self):
        self.assertEqual(sources.take().max(), 10)

    def test_skip(self):
        self.assertEqual(sources.skip().max(), 5)

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().max(), 16)

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().max(), 9)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().max(), 10)

    def test_distinct_with_objects(self):
        self.assertEqual(sources.distinctObjects().max(lambda k: len(k)), 'asd')

    def test_sort_with_numbers(self):
        self.assertEqual(sources.descendingNumbers().max(), 4)

if __name__ == '__main__':
    main()