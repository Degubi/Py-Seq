from unittest import TestCase, main
import tests.sources as sources

class AverageTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().average(), 4.5)

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().average(), 5)

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().average(), 2)

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().average(), 2)

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().average(), 1.5)

    def test_create_sequence_using_empty(self):
        self.assertIsNone(sources.empty().average())

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().average())

    def test_filter(self):
        self.assertEqual(sources.filter().average(), 2)

    def test_map(self):
        self.assertEqual(sources.map().average(), 4)

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().average(), 3.5)

    def test_take(self):
        self.assertEqual(sources.take().average(), 5)

    def test_skip(self):
        self.assertEqual(sources.skip().average(), 4)

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().average(), 6.2)

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().average(), 7.5)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().average(), 4.25)

    def test_sort_with_numbers(self):
        self.assertEqual(sources.descendingNumbers().average(), 2)

if __name__ == '__main__':
    main()