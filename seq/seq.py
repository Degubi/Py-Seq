from functools import cmp_to_key
from sys import maxsize
from collections import namedtuple

NumberStatistics = namedtuple('NumberStatistics', [ 'sum', 'count', 'min', 'max', 'average' ])

class _SumCount:

    def __init__(self):
        self.sum = 0
        self.count = 0

class _SumCountMinMax:

    def __init__(self):
        self.sum = 0
        self.count = 0
        self.min = maxsize
        self.max = -(maxsize - 1)


def _collect(result, sequenceInstance, accumulatorFunction):
    _checkTerminated(sequenceInstance)

    for e in sequenceInstance._generator:
        accumulatorFunction(result, e)

    return result

def _checkTerminated(sequenceInstance):
    if sequenceInstance._terminated:
        raise Exception('Sequence was already terminated!')

    sequenceInstance._terminated = True

def _ascending_sort(f, s, keySelectorFunction):
    firstKey = keySelectorFunction(f)
    secondKey = keySelectorFunction(s)

    return -1 if firstKey < secondKey else 1 if firstKey > secondKey else 0

def _descending_sort(f, s, keySelectorFunction):
    firstKey = keySelectorFunction(f)
    secondKey = keySelectorFunction(s)

    return 1 if firstKey < secondKey else -1 if firstKey > secondKey else 0

def _avg_fun(accumulator, nextElement):
    accumulator.count += 1
    accumulator.sum += nextElement

def _statistics_fun(accumulator, nextElement):
    accumulator.count += 1
    accumulator.sum += nextElement
    accumulator.min = min(accumulator.min, nextElement)
    accumulator.max = max(accumulator.max, nextElement)

def _throw_on_duplicate(key, oldE, newE):
    raise f"Duplicate value found for key: '{key}', previous value: '{oldE}', current value: '{newE}'"

def _to_map_fun(result, element, keySelectorFunction, valueSelectorFunction, duplicateResolverFunction):
    key = keySelectorFunction(element)
    value = valueSelectorFunction(element)
    existingValue = result.get(key)

    result[key] = value if existingValue == None else duplicateResolverFunction(key, existingValue, value)

def _groupBy_fun(result, element, keySelectorFunction, grouperFunction):
    mappedKey = keySelectorFunction(element)

    if not mappedKey in result:
        result[mappedKey] = grouperFunction['_accumulatorSupplier']()

    grouperFunction['_accumulatorFunction'](result, mappedKey, element)

def _averaging_accumulator_fun(accumulator, key, element, keySelector):
    acc = accumulator.get(key)
    acc.sum += keySelector(element)
    acc.count += 1

def _statisticizing_accumulator_fun(accumulator, key, element, keySelector):
    acc = accumulator.get(key)
    keySelected = keySelector(element)

    acc.count += 1
    acc.sum += keySelected
    acc.min = min(acc.min, keySelected)
    acc.max = max(acc.max, keySelected)

def _counting_accumulator_fun(accumulator, key, _):
    accumulator[key] = accumulator.get(key) + 1

def _summing_accumulator_fun(accumulator, key, element, keySelector):
    accumulator[key] = accumulator.get(key) + keySelector(element)

def _averaging_finisher_fun(result, key, value):
    result[key] = value.sum / value.count

def _statisticizing_finisher_fun(result, key, value):
    result[key] = NumberStatistics(value.sum, value.count, value.min, value.max, value.sum / value.count)




def _generate_range(begin, end, step):
    for i in range(begin, end, step):
        yield i

def _generate_iterate(seed, generatorFunction, limiter):
    i = seed
    yield i

    i = generatorFunction(i)

    while limiter(i):
        yield i
        i = generatorFunction(i)

def _generate_of(iterableObject):
    for e in iterableObject:
        yield e

def _generate_empty():
    return
    yield

def _generate_generate(supplierFunction):
    while(True):
        yield supplierFunction()

def _generate_filter(predicate, generatorInstance):
    for element in generatorInstance:
        if predicate(element):
            yield element

def _generate_map(mapper, generatorInstance):
    for element in generatorInstance:
        yield mapper(element)

def _generate_flatMap(mapper, generatorInstance):
    for element in generatorInstance:
        nested = mapper(element)

        for n in nested:
            yield n

def _generate_distinct(keySelectorFunction, generatorInstance):
    uniqueElements = []

    for element in generatorInstance:
        elementKeySelected = keySelectorFunction(element)

        try:
            for uniq in uniqueElements:
                if elementKeySelected == keySelectorFunction(uniq):
                    raise 'fml'
        except:
            continue

        uniqueElements.append(element)
        yield element

def _generate_take(count, generatorInstance):
    yieldedCount = 0

    while True:
        nextElement = next(generatorInstance, None)

        if nextElement == None or yieldedCount == count:
            break

        yieldedCount += 1
        yield nextElement

def _generate_skip(count, generatorInstance):
    skippedCount = 0

    while True:
        nextElement = next(generatorInstance, None)

        if nextElement == None:
            break

        if skippedCount >= count:
            yield nextElement

        skippedCount += 1

def _generate_takeWhile(predicate, generatorInstance):
    while True:
        nextElement = next(generatorInstance, None)

        if nextElement == None or not predicate(nextElement):
            break

        yield nextElement

def _generate_skipWhile(predicate, generatorInstance):
    while True:
        nextElement = next(generatorInstance, None)

        if nextElement == None:
            return

        if not predicate(nextElement):
            yield nextElement
            break

    for remaining in generatorInstance:
        yield remaining

def _generate_chunk(chunkSizes, generatorInstance):
    while True:
        elements = []

        for i in range(0, chunkSizes):
            element = next(generatorInstance, None)

            if element == None:
                break

            elements.append(element)

        if len(elements) == 0:
            break

        yield elements

class Grouper:
    ''' Grouper utility class, contains static factories for creating Grouper functions used with groupBy '''

    @staticmethod
    def to_list():
        ''' Creates a grouper function that maps each key to a list of elements for that specific key

            Returns:
                A new grouper instance '''

        return {
            '_accumulatorSupplier': lambda: [],
            '_accumulatorFunction': lambda accumulator, key, element: accumulator.get(key).append(element)
        }

    @staticmethod
    def counting():
        ''' Creates a grouper function that maps each key to 1 and then sums it (a.k.a counts the occurence of it)

            Useful for creating frequency maps

            Returns:
                A new grouper instance '''

        return {
            '_accumulatorSupplier': lambda: 0,
            '_accumulatorFunction': _counting_accumulator_fun
        }

    @staticmethod
    def summing(keySelectorFunction):
        ''' Creates a grouper function that maps each key to the sum of the keySelector's key

            Args:
                keySelectorFunction: Function used for extracting the property to calculate the sum of
            Returns:
                A new grouper instance '''

        return {
            '_accumulatorSupplier': lambda: 0,
            '_accumulatorFunction': lambda accumulator, key, element: _summing_accumulator_fun(accumulator, key, element, keySelectorFunction)
        }

    @staticmethod
    def averaging(keySelectorFunction):
        ''' Creates a grouper function that maps each key to the average of the keySelector's key

            Args:
                keySelectorFunction: Function used for extracting the property to calculate the average of
            Returns:
                A new grouper instance '''

        return {
            '_accumulatorSupplier': lambda: _SumCount(),
            '_accumulatorFunction': lambda accumulator, key, element: _averaging_accumulator_fun(accumulator, key, element, keySelectorFunction),
            '_finisherFunction': _averaging_finisher_fun
        }

    @staticmethod
    def statisticizing(keySelectorFunction):
        ''' Creates a grouper function that maps each key to the statistics of the keySelector's key

            Args:
                keySelectorFunction: Function used for extracting the property to calculate the statistics of
            Returns:
                A new grouper instance '''

        return {
            '_accumulatorSupplier': lambda: _SumCountMinMax(),
            '_accumulatorFunction': lambda accumulator, key, element: _statisticizing_accumulator_fun(accumulator, key, element, keySelectorFunction),
            '_finisherFunction': _statisticizing_finisher_fun
        }

class Sequence:
    ''' Sequence class, used for creating, manipulating & finishing sequences

        Sequences are created using static factories'''

    def __init__(self, generator):
        self._generator = generator()
        self._terminated = False

    @staticmethod
    def range(begin, end, step = 1):
        ''' Function for creating a sequence of numbers using a non inclusive number range generator

            Args:
                begin: The first value of the range
                end: The last value of the range
                step: Default is 1
            Returns:
                Sequence from begin-to stepping with increment'''

        return Sequence(lambda: _generate_range(begin, end, step))

    @staticmethod
    def range_closed(begin, end, step = 1):
        ''' Function for creating a sequence of numbers using an inclusive number range generator

            Args:
                begin: The first value of the range
                end: The last value of the range
                step: Default is 1
            Returns:
                Sequence from begin-to stepping with step '''

        return Sequence.range(begin, end + 1, step)

    @staticmethod
    def iterate(seed, generatorFunction, limiterPredicateFunction = lambda _: True):
        ''' Function for creating a sequence of elements using the seed as a base value and then applying the generator function to it,
            until the limiterPredicateFunction returns false

            Note:
                This generates an infinite sequence if the last parameter is ommited
            Args:
                seed: The initial value of the sequence
                generatorFunction: Function to generate the next element of the sequence
                limiterPredicateFunction: Optional parameter, defaults to always returning to true (meaning that it's infinite)
            Returns:
                Sequence with elements being populated lazily '''

        return Sequence(lambda: _generate_iterate(seed, generatorFunction, limiterPredicateFunction))

    @staticmethod
    def generate(generatorFunction):
        ''' Function for creating a sequence of elements using the input generator

            Note:
                This generates an infinite sequence
            Args:
                generatorFunction: A function that when called returns an element
            Returns:
                Sequence with elements being populated lazily from the input generatorFunction '''

        return Sequence(lambda: _generate_generate(generatorFunction))

    @staticmethod
    def empty():
        ''' Function for creating an empty sequence

            Returns:
                Sequence with 0 elements'''

        return Sequence(lambda: _generate_empty())

    @staticmethod
    def of(*elements):
        ''' Function for creating a sequence of elements using the passed in array source

            Args:
                elements: Input elements
            Returns:
                Sequence populated from the input array'''

        return Sequence(lambda: _generate_of(elements[0])) if len(elements) == 1 and isinstance(elements[0], list) \
        else   Sequence(lambda: _generate_of(elements))



    def filter(self, predicateFunction):
        ''' Method for creating a new sequence containing only the elements that match the given predicate

            Args:
                predicateFunction: The predicate to test against the elements, if it returns true the element is kept in the sequence
            Returns:
                New sequence containing only the elements that match the given predicate '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_filter(predicateFunction, self._generator))

    def map(self, mapperFunction):
        ''' Method for creating a new sequence with elements after applying the given function

            Args:
                mapperFunction: The function to apply to each element
            Returns:
                New sequence with elements after applying the given function '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_map(mapperFunction, self._generator))

    def flat_map(self, flatMapperFunction):
        ''' Method for creating a new sequence with elements after applying the given flatMapper function

            Args:
                flatMapperFunction: The function to apply to each element
            Returns:
                New sequence with elements after applying the given function '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_flatMap(flatMapperFunction, self._generator))

    def take(self, count):
        ''' Method for creating a new sequence with a specific amount of elements

            Args:
                count: Number of elements to keep in the sequence
            Returns:
                New sequence containing the first 'n' number of elements '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_take(count, self._generator))

    def skip(self, count):
        ''' Method for creating a new sequence while skipping 'n' number of elements

            Args:
                count: Number of elements to skip
            Returns:
                New sequence with the first 'n' elements skipped '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_skip(count, self._generator))

    def take_while(self, predicateFunction):
        ''' Method for creating a new sequence that takes elements until the given predicate returns false

            Args:
                predicateFunction: The function to test against
            Returns:
                New sequence that takes elements until the given predicate returns false '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_takeWhile(predicateFunction, self._generator))

    def skip_while(self, predicateFunction):
        ''' Method for creating a new sequence that skips elements until the given predicate returns true

            Args:
                predicateFunction: The function to test against
            Returns:
                New sequence that skips elements until the given predicate returns true '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_skipWhile(predicateFunction, self._generator))

    def distinct(self, keySelectorFunction = lambda k: k):
        ''' Method for creating a new sequence containing only unique values

            Args:
                keySelectorFunction: The Function for selecting a key for uniqueness, defaults to identity
            Returns:
                New sequence containing distinct elements according to the input function '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_distinct(keySelectorFunction, self._generator))

    def sort(self, comparerFunction):
        ''' Method for creating a new sequence where the elements are sorted based on the given comparer

            Args:
                comparerFunction: This function has the same properties as the comparer function given to .sort
            Returns:
                New sequence with elements are sorted based on the given comparer '''

        allElements = self.to_list()

        allElements.sort(key = cmp_to_key(comparerFunction))

        return Sequence(lambda: _generate_of(allElements))

    def sort_ascending(self, keySelectorFunction = lambda k: k):
        ''' Method for creating a new sequence where the elements are sorted in ascending order based on the given keySelector

            Args:
                keySelectorFunction: Function for selecting a key property to be used for sorting, defaults to identity
            Returns:
                New sequence with elements sorted in ascending order based on the given keySelector '''

        return self.sort(lambda k, s: _ascending_sort(k, s, keySelectorFunction))

    def sort_descending(self, keySelectorFunction = lambda k: k):
        ''' Method for creating a new sequence where the elements are sorted in descending order based on the given keySelector

            Args:
                keySelectorFunction: Function for selecting a key property to be used for sorting, defaults to identity
            Returns:
                New sequence with elements sorted in descending order based on the given keySelector '''

        return self.sort(lambda k, s: _descending_sort(k, s, keySelectorFunction))

    def chunk(self, chunkSizes):
        ''' Method for creating a new sequence where the elements are chunked into arrays with each array containing max of 'chunkSizes' elements

            Args:
                chunkSizes: Max size of each chunk
            Returns:
                New sequence with arrays containing the sequence's elements, with their maximum lengths restricted to the given chunk size '''

        _checkTerminated(self)
        return Sequence(lambda: _generate_chunk(chunkSizes, self._generator))


    def for_each(self, consumerFunction):
        ''' Method for terminating the sequence and applying a function to each of the elements

            Args:
                consumerFunction: Function to apply to each of the elements
            Returns:
                Nothing '''

        _checkTerminated(self)

        for e in self._generator:
            consumerFunction(e)

    def reduce(self, seed, accumulatorFunction):
        ''' Method for terminating the sequence and peforming a reduction on the elements of the sequence

            Args:
                seed: Used as an 'initial' or 'base' value
                accumulatorFunction: Function used for combining the accumulator and the current element
            Returns:
                Result of the reduction '''

        _checkTerminated(self)

        returnVal = seed
        for e in self._generator:
            returnVal = accumulatorFunction(returnVal, e)

        return returnVal

    def sum(self):
        ''' Method for terminating the sequence while calculating the sum of the elements

            Returns:
                Sum of the elements in the sequence '''

        return self.reduce(0, lambda accumulator, nextElement: accumulator + nextElement)

    def count(self):
        ''' Method for terminating the sequence while counting the number of elements

            Returns:
                Count of the elements in the sequence '''

        return self.reduce(0, lambda accumulator, _: accumulator + 1)

    def average(self):
        ''' Method for terminating the sequence while calculating the average of the elements

            Note: This function returns None if the sequence is empty
            Returns:
                Average of the elements in the sequence or None if the sequence was empty '''

        result = _collect(_SumCount(), self, _avg_fun)

        return None if result.count == 0 else result.sum / result.count

    def statistics(self):
        ''' Method for terminating the sequence and calculating the statistics of the elements of the sequence

            Returns:
                Object that contains the sum, count, min, max and average of the sequence '''

        result = _collect(_SumCountMinMax(), self, _statistics_fun)

        return None if result.count == 0 else NumberStatistics(result.sum, result.count, result.min, result.max, result.sum / result.count)

    def join(self, separator = ''):
        ''' Method for terminating the sequence while joining the elements together using the given separator

            Args:
                separator: The separator used for joining the elements, defaults to empty string
            Returns:
                The final joined string '''

        return separator.join(self.map(lambda k: str(k)).to_list())

    def min(self, keySelectorFunction = lambda k: k):
        ''' Method for retrieving the smallest element from the sequence

            Note:
                This function returns None if the sequence is empty
            Args:
                keySelectorFunction: Function used for extracting the key from the object to compare against, defaults to identity
            Returns:
                The smallest element in the sequence according to the keySelector or None if the sequence was empty '''

        firstElement = next(self._generator, None)

        return self.reduce(None if firstElement == None else firstElement, lambda accumulator, nextElement: accumulator if keySelectorFunction(accumulator) < keySelectorFunction(nextElement) else nextElement)

    def max(self, keySelectorFunction = lambda k: k):
        ''' Method for retrieving the largest element from the sequence

            Note:
                This function returns None if the sequence is empty
            Args:
                keySelectorFunction: Function used for extracting the key from the object to compare against, defaults to identity
            Returns:
                The largest element in the sequence according to the keySelector or None if the sequence was empty '''

        firstElement = next(self._generator, None)

        return self.reduce(None if firstElement == None else firstElement, lambda accumulator, nextElement: accumulator if keySelectorFunction(accumulator) > keySelectorFunction(nextElement) else nextElement)

    def to_list(self):
        ''' Method for terminating the sequence and collecting the elements of the sequence into a list

            Returns:
                A list containing the elements of the sequence '''

        return _collect([], self, lambda result, element: result.append(element))

    def to_dictionary(self, keySelectorFunction, valueSelectorFunction, duplicateResolverFunction = _throw_on_duplicate):
        ''' Method for terminating the sequence and collecting the elements into a dictionary using the key & value selector functions

            Args:
                keySelectorFunction: Function used for extracting the key from the object
                valueSelectorFunction: Function used for extracting the value from the object
                duplicateResolverFunction: Takes 3 arguments: the key, the old value and the value we're trying to insert at the moment. Defaults to throwing an error.
                    Return value is the value that gets inserted as the value of the duplicate key. Default is to throw an error
            Returns:
                A dictionary where the keys are populated using the keySelector and the corresponding values are the values returned by the valueSelector '''

        return _collect({}, self, lambda result, element: _to_map_fun(result, element, keySelectorFunction, valueSelectorFunction, duplicateResolverFunction))

    def partition_by(self, predicateFunction):
        ''' Method for terminating the sequence and partitioning the elements into 2 arrays according to the given predicate

            Args:
                predicateFunction: The predicate to test against
            Returns:
                2 arrays where the first one contains the elements that matched the predicate and the second one that didn't '''

        return _collect([[], []], self, lambda result, element: result[0 if predicateFunction(element) == True else 1].append(element))

    def group_by(self, keySelectorFunction, grouperFunction = Grouper.to_list()):
        ''' Method for terminating the sequence and performing a grouping by operation on the elements of the sequence

            Args:
                keySelectorFunction: Function used for extracting the keys of the result
                grouperFunction: An instance of a Grouper object, defaults to Grouper.to_list()
            Returns:
                The result of the grouping '''

        result = _collect({}, self, lambda result, element: _groupBy_fun(result, element, keySelectorFunction, grouperFunction))

        finisherFunction = grouperFunction.get('_finisherFunction')
        if finisherFunction != None:
            for key, value in result.items():
                finisherFunction(result, key, value)

        return result

    def first(self):
        ''' Method for terminating the sequence and getting the first element from it

            Note:
                This function returns None if the sequence is empty
            Returns:
                The first element of the sequence or None if the sequence was empty '''

        _checkTerminated(self)

        firstElement = next(self._generator, None)

        return None if firstElement == None else firstElement

    def last(self):
        ''' Method for terminating the sequence and getting the last element from it

            Note:
                This function returns None if the sequence is empty
            Returns:
                The last element of the sequence or None if the sequence was empty '''

        firstElement = next(self._generator, None)

        return self.reduce(None if firstElement == None else firstElement, lambda _, nextElement: nextElement)

    def all_matches(self, predicateFunction):
        ''' Method for terminating the sequence which returns true only if the given predicate matches all of the elements in the sequence

            Args:
                predicateFunction: The function to test against
            Returns:
                True if the given predicate matches all of the elements in the sequence '''

        _checkTerminated(self)

        for e in self._generator:
            if predicateFunction(e) == False:
                return False

        return True

    def any_matches(self, predicateFunction):
        ''' Method for terminating the sequence which returns true if the given predicate matches any of the elements in the sequence

            Args:
                predicateFunction: The function to test against
            Returns:
                True if the given predicate matches any of the elements in the sequence '''

        _checkTerminated(self)

        for e in self._generator:
            if predicateFunction(e) == True:
                return True

        return False