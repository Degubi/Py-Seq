from unittest import TestCase, main
import tests.sources as sources

class MinTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().min(), 0)

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().min(), 0)

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().min(), 1)

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().min(), 0)

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().min(), 0)

    def test_create_sequence_using_empty(self):
        self.assertIsNone(sources.empty().min())

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().min())

    def test_filter(self):
        self.assertEqual(sources.filter().min(), 0)

    def test_map(self):
        self.assertEqual(sources.map().min(), 0)

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().min(), 1)

    def test_take(self):
        self.assertEqual(sources.take().min(), 0)

    def test_skip(self):
        self.assertEqual(sources.skip().min(), 3)

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().min(), 1)

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().min(), 6)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().min(), 0)

    def test_distinct_with_objects(self):
        self.assertEqual(sources.distinctObjects().min(lambda k: len(k)), 'a')

    def test_sort_with_numbers(self):
        self.assertEqual(sources.descendingNumbers().min(), 0)

if __name__ == '__main__':
    main()