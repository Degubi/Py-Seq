from unittest import TestCase, main
import sources

class JoinTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertEqual(sources.range().join(), '0123456789')

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertEqual(sources.rangeClosed().join(', '), '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10')

    def test_create_sequence_from_array(self):
        self.assertEqual(sources.array().join('-'), '1-2-3')

    def test_create_sequence_using_iterate(self):
        self.assertEqual(sources.iterate().join(','), '0,1,2,3,4')

    def test_create_sequence_using_of(self):
        self.assertEqual(sources.of().join(), '0123')

    def test_create_sequence_using_empty(self):
        self.assertEqual(sources.empty().join(', '), '')

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().join())

    def test_filter(self):
        self.assertEqual(sources.filter().join(', '), '0, 2, 4')

    def test_map(self):
        self.assertEqual(sources.map().join('x'), '0x4x8')

    def test_flatMap(self):
        self.assertEqual(sources.flatMap().join(', '), '1, 2, 3, 4, 5, 6')

    def test_take(self):
        self.assertEqual(sources.take().join(' '), '0 2 4 6 8 10')

    def test_skip(self):
        self.assertEqual(sources.skip().join('-'), '3-4-5')

    def test_takeWhile(self):
        self.assertEqual(sources.takeWhile().join(', '), '1, 2, 4, 8, 16')

    def test_skipWhile(self):
        self.assertEqual(sources.skipWhile().join(','), '6,7,8,9')

    def test_distinct_with_numbers(self):
        self.assertEqual(sources.distinctNumbers().join('x'), '0x2x5x10')

    def test_distinct_with_objects(self):
        self.assertEqual(sources.distinctObjects().join(', '), 'asd, a, ba')

    def test_sort_with_numbers(self):
        self.assertEqual(sources.descendingNumbers().join(', '), '4, 3, 2, 1, 0')

main()