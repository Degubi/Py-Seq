from unittest import TestCase, main
import tests.sources as sources

class AnyMatchesTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertTrue(sources.range().any_matches(lambda k: k < 1000))

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertTrue(sources.rangeClosed().any_matches(lambda k: k % 2 == 0))

    def test_create_sequence_from_array(self):
        self.assertTrue(sources.array().any_matches(lambda k: k > 0))

    def test_create_sequence_using_iterate(self):
        self.assertTrue(sources.iterate().any_matches(lambda k: k % 10 != 0))

    def test_create_sequence_using_of(self):
        self.assertTrue(sources.of().any_matches(lambda k: k - k == 0))

    def test_create_sequence_using_empty(self):
        self.assertFalse(sources.empty().any_matches(lambda k: k % 2 == 0))

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().any_matches(lambda k: k == k))

    def test_filter(self):
        self.assertTrue(sources.filter().any_matches(lambda k: k % 2 == 0))

    def test_map(self):
        self.assertTrue(sources.map().any_matches(lambda k: k % 4 == 0))

    def test_flatMap(self):
        self.assertTrue(sources.flatMap().any_matches(lambda k: k - 2 == 0))

    def test_take(self):
        self.assertTrue(sources.take().any_matches(lambda k: k * 0 == 0))

    def test_skip(self):
        self.assertTrue(sources.skip().any_matches(lambda k: k * -1 != k))

    def test_takeWhile(self):
        self.assertTrue(sources.takeWhile().any_matches(lambda k: k < 10))

    def test_skipWhile(self):
        self.assertTrue(sources.skipWhile().any_matches(lambda k: k % 5 != 0))

    def test_distinct_with_numbers(self):
        self.assertFalse(sources.distinctNumbers().any_matches(lambda k: k < 0))

    def test_distinct_with_objects(self):
        self.assertTrue(sources.distinctObjects().any_matches(lambda k: k != 'a'))

    def test_sort_with_numbers(self):
        self.assertTrue(sources.descendingNumbers().any_matches(lambda k: k == 3))

if __name__ == '__main__':
    main()