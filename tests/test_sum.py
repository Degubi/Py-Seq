from unittest import TestCase, main
import tests.sources as sources

class SumTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().sum(), 45)

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().sum(), 55)

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().sum(), 6)

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().sum(), 10)

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().sum(), 6)

    def test_create_sequence_using_empty(self):
        self.assertEqual(sources.empty().sum(), 0)

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().sum())

    def test_filter(self):
        self.assertEqual(sources.filter().sum(), 6)

    def test_map(self):
        self.assertEqual(sources.map().sum(), 12)

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().sum(), 21)

    def test_take(self):
        self.assertEqual(sources.take().sum(), 30)

    def test_skip(self):
        self.assertEqual(sources.skip().sum(), 12)

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().sum(), 31)

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().sum(), 30)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().sum(), 17)

if __name__ == '__main__':
    main()