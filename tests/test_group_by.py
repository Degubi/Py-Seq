from unittest import TestCase, main
import sources
from seq import Grouper, NumberStatistics

class GroupByTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertDictEqual(sources.range().group_by(lambda k: k % 2), { 0: [ 0, 2, 4, 6, 8 ], 1: [ 1, 3, 5, 7, 9 ] })

    def test_create_sequence_using_empty(self):
        self.assertDictEqual(sources.empty().group_by(lambda k: k), {})

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().group_by(lambda k: k))


    def test_to_list_with_objects(self):
        self.assertDictEqual(sources.ofObjects().group_by(lambda k: k['prop1'], Grouper.to_list()), { 'asd': [{ 'prop1': 'asd', 'prop2': 50 }, { 'prop1': 'asd', 'prop2': 20 }], 'kek': [{ 'prop1': 'kek', 'prop2': 10 }]})

    def test_to_list_with_empty_sequence(self):
        self.assertDictEqual(sources.empty().group_by(lambda k: k, Grouper.to_list()), {})

    def test_to_list_with_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().group_by(lambda k: k, Grouper.to_list()))


    def test_counting_with_objects(self):
        self.assertDictEqual(sources.ofObjects().group_by(lambda k: k['prop1'], Grouper.counting()), { 'asd': 2, 'kek': 1 })

    def test_counting_with_empty_sequence(self):
        self.assertDictEqual(sources.empty().group_by(lambda k: k, Grouper.counting()), {})

    def test_counting_with_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().group_by(lambda k: k, Grouper.counting()))


    def test_summing_with_objects(self):
        self.assertDictEqual(sources.ofObjects().group_by(lambda k: k['prop1'], Grouper.summing(lambda k: k['prop2'])), { 'asd': 70, 'kek': 10 })

    def test_summing_with_empty_sequence(self):
        self.assertDictEqual(sources.empty().group_by(lambda k: k, Grouper.summing(lambda k: k)), {})

    def test_summing_with_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().group_by(lambda k: k, Grouper.summing(lambda k: k)))


    def test_averaging_with_objects(self):
        self.assertDictEqual(sources.ofObjects().group_by(lambda k: k['prop1'], Grouper.averaging(lambda k: k['prop2'])), { 'asd': 35, 'kek': 10 })

    def test_averaging_with_empty_sequence(self):
        self.assertDictEqual(sources.empty().group_by(lambda k: k, Grouper.averaging(lambda k: k)), {})

    def test_averaging_with_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().group_by(lambda k: k, Grouper.averaging(lambda k: k)))


    def test_statisticizing_with_objects(self):
        self.assertDictEqual(sources.ofObjects().group_by(lambda k: k['prop1'], Grouper.statisticizing(lambda k: k['prop2'])), { 'asd': NumberStatistics(70, 2, 20, 50, 35), 'kek': NumberStatistics(10, 1, 10, 10, 10)})

    def test_statisticizing_with_empty_sequence(self):
        self.assertDictEqual(sources.empty().group_by(lambda k: k, Grouper.statisticizing(lambda k: k)), {})

    def test_statisticizing_with_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().group_by(lambda k: k, Grouper.statisticizing(lambda k: k)))

main()