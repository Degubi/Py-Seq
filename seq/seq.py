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

    @staticmethod
    def to_list():
        return {
            '_accumulatorSupplier': lambda: [],
            '_accumulatorFunction': lambda accumulator, key, element: accumulator.get(key).append(element)
        }

    @staticmethod
    def counting():
        return {
            '_accumulatorSupplier': lambda: 0,
            '_accumulatorFunction': _counting_accumulator_fun
        }

    @staticmethod
    def summing(keySelector):
        return {
            '_accumulatorSupplier': lambda: 0,
            '_accumulatorFunction': lambda accumulator, key, element: _summing_accumulator_fun(accumulator, key, element, keySelector)
        }

    @staticmethod
    def averaging(keySelector):
        return {
            '_accumulatorSupplier': lambda: _SumCount(),
            '_accumulatorFunction': lambda accumulator, key, element: _averaging_accumulator_fun(accumulator, key, element, keySelector),
            '_finisherFunction': _averaging_finisher_fun
        }

    @staticmethod
    def statisticizing(keySelector):
        return {
            '_accumulatorSupplier': lambda: _SumCountMinMax(),
            '_accumulatorFunction': lambda accumulator, key, element: _statisticizing_accumulator_fun(accumulator, key, element, keySelector),
            '_finisherFunction': _statisticizing_finisher_fun
        }

class Sequence:

    def __init__(self, generator):
        self._generator = generator()
        self._terminated = False

    @staticmethod
    def range(begin, end, step = 1):
        return Sequence(lambda: _generate_range(begin, end, step))

    @staticmethod
    def range_closed(begin, end, step = 1):
        return Sequence.range(begin, end + 1, step)

    @staticmethod
    def iterate(seed, generatorFunction, limiterPredicateFunction = lambda _: True):
        return Sequence(lambda: _generate_iterate(seed, generatorFunction, limiterPredicateFunction))

    @staticmethod
    def generate(generatorFunction):
        return Sequence(lambda: _generate_generate(generatorFunction))

    @staticmethod
    def empty():
        return Sequence(lambda: _generate_empty())

    @staticmethod
    def of(*elements):
        return Sequence(lambda: _generate_of(elements[0])) if len(elements) == 1 and isinstance(elements[0], list) \
        else   Sequence(lambda: _generate_of(elements))



    def filter(self, predicateFunction):
        _checkTerminated(self)
        return Sequence(lambda: _generate_filter(predicateFunction, self._generator))

    def map(self, mapperFunction):
        _checkTerminated(self)
        return Sequence(lambda: _generate_map(mapperFunction, self._generator))

    def flat_map(self, nestMapperFunction):
        _checkTerminated(self)
        return Sequence(lambda: _generate_flatMap(nestMapperFunction, self._generator))

    def take(self, count):
        _checkTerminated(self)
        return Sequence(lambda: _generate_take(count, self._generator))

    def skip(self, count):
        _checkTerminated(self)
        return Sequence(lambda: _generate_skip(count, self._generator))

    def take_while(self, predicateFunction):
        _checkTerminated(self)
        return Sequence(lambda: _generate_takeWhile(predicateFunction, self._generator))

    def skip_while(self, predicateFunction):
        _checkTerminated(self)
        return Sequence(lambda: _generate_skipWhile(predicateFunction, self._generator))

    def distinct(self, keySelectorFunction = lambda k: k):
        _checkTerminated(self)
        return Sequence(lambda: _generate_distinct(keySelectorFunction, self._generator))

    def sort(self, comparerFunction):
        allElements = self.to_list()

        allElements.sort(key = cmp_to_key(comparerFunction))

        return Sequence(lambda: _generate_of(allElements))

    def sort_ascending(self, keySelectorFunction = lambda k: k):
        return self.sort(lambda k, s: _ascending_sort(k, s, keySelectorFunction))

    def sort_descending(self, keySelectorFunction = lambda k: k):
        return self.sort(lambda k, s: _descending_sort(k, s, keySelectorFunction))

    def chunk(self, chunkSizes):
        _checkTerminated(self)
        return Sequence(lambda: _generate_chunk(chunkSizes, self._generator))


    def for_each(self, consumerFunction):
        _checkTerminated(self)

        for e in self._generator:
            consumerFunction(e)

    def reduce(self, seed, accumulatorFunction):
        _checkTerminated(self)

        returnVal = seed
        for e in self._generator:
            returnVal = accumulatorFunction(returnVal, e)

        return returnVal

    def sum(self):
        return self.reduce(0, lambda accumulator, nextElement: accumulator + nextElement)

    def count(self):
        return self.reduce(0, lambda accumulator, _: accumulator + 1)

    def average(self):
        result = _collect(_SumCount(), self, _avg_fun)

        return None if result.count == 0 else result.sum / result.count


    def statistics(self):
        result = _collect(_SumCountMinMax(), self, _statistics_fun)

        return None if result.count == 0 else NumberStatistics(result.sum, result.count, result.min, result.max, result.sum / result.count)

    def join(self, separator = ''):
        return separator.join(self.map(lambda k: str(k)).to_list())

    def min(self, keySelector = lambda k: k):
        firstElement = next(self._generator, None)

        return self.reduce(None if firstElement == None else firstElement, lambda accumulator, nextElement: accumulator if keySelector(accumulator) < keySelector(nextElement) else nextElement)

    def max(self, keySelector = lambda k: k):
        firstElement = next(self._generator, None)

        return self.reduce(None if firstElement == None else firstElement, lambda accumulator, nextElement: accumulator if keySelector(accumulator) > keySelector(nextElement) else nextElement)

    def to_list(self):
        return _collect([], self, lambda result, element: result.append(element))

    def to_dictionary(self, keySelectorFunction, valueSelectorFunction, duplicateResolverFunction = _throw_on_duplicate):
        return _collect({}, self, lambda result, element: _to_map_fun(result, element, keySelectorFunction, valueSelectorFunction, duplicateResolverFunction))

    def partition_by(self, predicateFunction):
        return _collect([[], []], self, lambda result, element: result[0 if predicateFunction(element) == True else 1].append(element))

    def group_by(self, keySelectorFunction, grouperFunction = Grouper.to_list()):
        result = _collect({}, self, lambda result, element: _groupBy_fun(result, element, keySelectorFunction, grouperFunction))

        finisherFunction = grouperFunction.get('_finisherFunction')
        if finisherFunction != None:
            for key, value in result.items():
                finisherFunction(result, key, value)

        return result

    def first(self):
        _checkTerminated(self)

        firstElement = next(self._generator, None)

        return None if firstElement == None else firstElement

    def last(self):
        firstElement = next(self._generator, None)

        return self.reduce(None if firstElement == None else firstElement, lambda _, nextElement: nextElement)

    def all_matches(self, predicateFunction):
        _checkTerminated(self)

        for e in self._generator:
            if predicateFunction(e) == False:
                return False

        return True

    def any_matches(self, predicateFunction):
        _checkTerminated(self)

        for e in self._generator:
            if predicateFunction(e) == True:
                return True

        return False