from unittest import TestCase, main
import tests.sources as sources

class CountTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().count(), 10)

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().count(), 11)

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().count(), 3)

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().count(), 5)

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().count(), 4)

    def test_create_sequence_using_empty(self):
        self.assertEqual(sources.empty().count(), 0)

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().count())

    def test_filter(self):
        self.assertEqual(sources.filter().count(), 3)

    def test_map(self):
        self.assertEqual(sources.map().count(), 3)

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().count(), 6)

    def test_take(self):
        self.assertEqual(sources.take().count(), 6)

    def test_skip(self):
        self.assertEqual(sources.skip().count(), 3)

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().count(), 5)

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().count(), 4)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().count(), 4)

    def test_distinct_with_objects(self):
        self.assertEqual(sources.distinctObjects().count(), 3)

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.descendingNumbers().count(), 5)

if __name__ == '__main__':
    main()