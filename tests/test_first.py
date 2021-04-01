from unittest import TestCase, main
import tests.sources as sources

class FirstTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().first(), 0)

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().first(), 0)

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().first(), 1)

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().first(), 0)

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().first(), 0)

    def test_create_sequence_using_empty(self):
        self.assertIsNone(sources.empty().first())

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().first())

    def test_filter(self):
        self.assertEqual(sources.filter().first(), 0)

    def test_map(self):
        self.assertEqual(sources.map().first(), 0)

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().first(), 1)

    def test_take(self):
        self.assertEqual(sources.take().first(), 0)

    def test_skip(self):
        self.assertEqual(sources.skip().first(), 3)

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().first(), 1)

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().first(), 6)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().first(), 0)

    def test_distinct_with_objects(self):
        self.assertEqual(sources.distinctObjects().first(), 'asd')

    def test_sort_with_numbers(self):
        self.assertEqual(sources.descendingNumbers().first(), 4)

if __name__ == '__main__':
    main()