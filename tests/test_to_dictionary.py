from unittest import TestCase, main
import tests.sources as sources

class ToDictionaryTest(TestCase):

    def test_number_sequence_from_0_to_10(self):
        self.assertDictEqual(sources.range().to_dictionary(lambda k: k, lambda k: k % 2 == 0), { 0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False })

    def test_number_sequence_from_0_to_10_closed_with_not_handling_duplicates(self):
        self.assertRaises(Exception, lambda: sources.rangeClosed().to_dictionary(lambda k: k % 2, lambda k: k))

    def test_create_sequence_from_array_handling_duplicates(self):
        self.assertDictEqual(sources.array().to_dictionary(lambda _: 1, lambda k: k, lambda k, _, currentVal: currentVal), { 1: 3 })

    def test_create_sequence_using_iterate(self):
        self.assertDictEqual(sources.iterate().to_dictionary(lambda k: k + 1, lambda k: k - 1), { 1: -1, 2: 0, 3: 1, 4: 2, 5: 3 })

    def test_create_sequence_using_of(self):
        self.assertDictEqual(sources.of().to_dictionary(lambda k: k, lambda k: k * 2), { 0: 0, 1: 2, 2: 4, 3: 6 })

    def test_create_sequence_using_empty(self):
        self.assertDictEqual(sources.empty().to_dictionary(lambda k: k, lambda k: k / 2), {})

    def test_use_already_terminated_sequence(self):
        self.assertRaises(Exception, lambda: sources.terminated().to_dictionary(lambda k: k, lambda k: k / 2))

    def test_filter(self):
        self.assertDictEqual(sources.filter().to_dictionary(lambda k: k, lambda k: k), { 0: 0, 2: 2, 4: 4 })

    def test_map(self):
        self.assertDictEqual(sources.map().to_dictionary(lambda k: k, lambda k: k % 4), { 0: 0, 4: 0, 8: 0 })

    def test_flatMap_handling_duplicates(self):
        self.assertDictEqual(sources.flatMap().to_dictionary(lambda _: 0, lambda k: k, lambda k, oldValue, _: oldValue), { 0: 1 })

    def test_take(self):
        self.assertRaises(Exception, lambda: sources.take().to_dictionary(lambda _: 1, lambda _: 2))

    def test_skip(self):
        self.assertDictEqual(sources.skip().to_dictionary(lambda k: k, lambda k: min(k, 4)), { 3: 3, 4: 4, 5: 4 })

    def test_takeWhile(self):
        self.assertDictEqual(sources.takeWhile().to_dictionary(lambda k: k % 2, lambda k: k, lambda k, _, newValue: newValue), { 1: 1, 0: 16 })

    def test_skipWhile_not_handling_duplicates(self):
        self.assertRaises(Exception, lambda: sources.skipWhile().to_dictionary(lambda _: 0, lambda k: k))

    def test_distinct_with_numbers(self):
        self.assertDictEqual(sources.distinctNumbers().to_dictionary(lambda k: k, lambda k: k), { 0: 0, 2: 2, 5: 5, 10: 10 })

    def test_distinct_with_objects(self):
        self.assertDictEqual(sources.distinctObjects().to_dictionary(lambda k: k, lambda k: len(k)), { 'asd': 3, 'a': 1, 'ba': 2 })

if __name__ == '__main__':
    main()