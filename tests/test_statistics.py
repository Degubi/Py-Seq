from unittest import TestCase, main
import sources
from seq import NumberStatistics

class StatisticsTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertTupleEqual(sources.range().statistics(), NumberStatistics(45, 10, 0, 9, 4.5))

    def test_number_sequence_from_0_to_10_closed(self):
        self.assertTupleEqual(sources.rangeClosed().statistics(), NumberStatistics(55, 11, 0, 10, 5))

    def test_create_sequence_from_array(self):
        self.assertTupleEqual(sources.array().statistics(), NumberStatistics(6, 3, 1, 3, 2))

    def test_create_sequence_using_iterate(self):
        self.assertTupleEqual(sources.iterate().statistics(), NumberStatistics(10, 5, 0, 4, 2))

    def test_create_sequence_using_of(self):
        self.assertTupleEqual(sources.of().statistics(), NumberStatistics(6, 4, 0, 3, 1.5))

    def test_create_sequence_using_empty(self):
        self.assertIsNone(sources.empty().statistics())

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().statistics())

    def test_filter(self):
        self.assertTupleEqual(sources.filter().statistics(), NumberStatistics(6, 3, 0, 4, 2))

    def test_map(self):
        self.assertTupleEqual(sources.map().statistics(), NumberStatistics(12, 3, 0, 8, 4))

    def test_flatMap(self):
        self.assertTupleEqual(sources.flatMap().statistics(), NumberStatistics(21, 6, 1, 6, 3.5))

    def test_take(self):
        self.assertTupleEqual(sources.take().statistics(), NumberStatistics(30, 6, 0, 10, 5))

    def test_skip(self):
        self.assertTupleEqual(sources.skip().statistics(), NumberStatistics(12, 3, 3, 5, 4))

    def test_takeWhile(self):
        self.assertTupleEqual(sources.takeWhile().statistics(), NumberStatistics(31, 5, 1, 16, 6.2))

    def test_skipWhile(self):
        self.assertTupleEqual(sources.skipWhile().statistics(), NumberStatistics(30, 4, 6, 9, 7.5))

    def test_distinct_with_numbers(self):
        self.assertTupleEqual(sources.distinctNumbers().statistics(), NumberStatistics(17, 4, 0, 10, 4.25))

main()