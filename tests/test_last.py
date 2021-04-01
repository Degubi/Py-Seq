from unittest import TestCase, main
import tests.sources as sources

class LastTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().last(), 9)

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().last(), 10)

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().last(), 3)

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().last(), 4)

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().last(), 3)

    def test_create_sequence_using_empty(self):
        self.assertIsNone(sources.empty().last())

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().last())

    def test_filter(self):
        self.assertEqual(sources.filter().last(), 4)

    def test_map(self):
        self.assertEqual(sources.map().last(), 8)

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().last(), 6)

    def test_take(self):
        self.assertEqual(sources.take().last(), 10)

    def test_skip(self):
        self.assertEqual(sources.skip().last(), 5)

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().last(), 16)

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().last(), 9)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().last(), 10)

    def test_distinct_with_objects(self):
        self.assertEqual(sources.distinctObjects().last(), 'ba')

    def test_sort_with_numbers(self):
        self.assertEqual(sources.descendingNumbers().last(), 0)

if __name__ == '__main__':
    main()