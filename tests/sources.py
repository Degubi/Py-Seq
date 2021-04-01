from seq import Sequence

def range(): return Sequence.range(0, 10)
def rangeClosed(): return Sequence.range_closed(0, 10)
def array(): return Sequence.of([ 1, 2, 3 ])
def iterate(): return Sequence.iterate(0, lambda k: k + 1, lambda k: k < 5)
def empty(): return Sequence.empty()

def terminated():
    seq = Sequence.range(0, 5)
    seq.for_each(lambda _: None)
    return seq

def of(): return Sequence.of(0, 1, 2, 3)
def ofObjects(): return Sequence.of({ 'prop1': 'asd', 'prop2': 50 }, { 'prop1': 'asd', 'prop2': 20 }, { 'prop1': 'kek', 'prop2': 10 })
def filter(): return Sequence.of(0, 1, 2, 3, 4, 5).filter(lambda k: k % 2 == 0)
def map(): return Sequence.of(0, 2, 4).map(lambda k: k * 2)
def flatMap(): return Sequence.of([{ 'data': [ 1, 2, 3 ] }, { 'data': [ 4, 5, 6 ] }]).flat_map(lambda k: k['data'])
def take(): return Sequence.iterate(0, lambda k: k + 2).take(6)
def skip(): return Sequence.range(0, 6).skip(3)
def takeWhile(): return Sequence.iterate(1, lambda k: k * 2).take_while(lambda k: k < 20)
def skipWhile(): return Sequence.range(0, 10).skip_while(lambda k: k < 6)
def distinctNumbers(): return Sequence.of(0, 2, 2, 0, 5, 10, 2, 5).distinct()
def distinctObjects(): return Sequence.of('asd', 'sad', 'lal', 'a', 'c', 'ba').distinct(lambda k: len(k))
def descendingNumbers(): return Sequence.range(0, 5).sort_descending()