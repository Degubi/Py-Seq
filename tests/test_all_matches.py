from unittest import TestCase, main
import sources

class AllMatchesTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertTrue(sources.range().all_matches(lambda k: k < 1000))

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertFalse(sources.rangeClosed().all_matches(lambda k: k % 2 == 0))

    def test_create_sequence_from_array(self):
        self.assertTrue(sources.array().all_matches(lambda k: k > 0))

    def test_create_sequence_using_iterate(self):
        self.assertFalse(sources.iterate().all_matches(lambda k: k % 10 != 0))

    def test_create_sequence_using_of(self):
        self.assertTrue(sources.of().all_matches(lambda k: k - k == 0))

    def test_create_sequence_using_empty(self):
        self.assertTrue(sources.empty().all_matches(lambda k: k % 2 == 0))

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().all_matches(lambda k: k == k))

    def test_filter(self):
        self.assertTrue(sources.filter().all_matches(lambda k: k % 2 == 0))

    def test_map(self):
        self.assertTrue(sources.map().all_matches(lambda k: k % 4 == 0))

    def test_flatMap(self):
        self.assertFalse(sources.flatMap().all_matches(lambda k: k - 2 == 0))

    def test_take(self):
        self.assertTrue(sources.take().all_matches(lambda k: k * 0 == 0))

    def test_skip(self):
        self.assertTrue(sources.skip().all_matches(lambda k: k * -1 != k))

    def test_takeWhile(self):
        self.assertFalse(sources.takeWhile().all_matches(lambda k: k < 10))

    def test_skipWhile(self):
        self.assertTrue(sources.skipWhile().all_matches(lambda k: k % 5 != 0))

    def test_distinct_with_numbers(self):
        self.assertFalse(sources.distinctNumbers().all_matches(lambda k: k < 0))

    def test_distinct_with_objects(self):
        self.assertFalse(sources.distinctObjects().all_matches(lambda k: k != 'a'))

    def test_sort_with_numbers(self):
        self.assertFalse(sources.descendingNumbers().all_matches(lambda k: k == 3))

main()