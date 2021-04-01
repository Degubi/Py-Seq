# Python functional sequence processing library
[![Github issues](https://img.shields.io/github/issues/Degubi/Py-Seq?label=Issues&style=plastic&logo=github)](https://github.com/Degubi/Py-Seq/issues)
[![Linecount](https://img.shields.io/tokei/lines/github/degubi/Py-Seq?label=Total%20Lines&logo=Github&style=plastic)](https://github.com/Degubi/Py-Seq/tree/master/src)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/degubi/py-seq/Run%20tests?label=Build&style=plastic&logo=github-actions)](https://github.com/Degubi/Py-Seq/actions)
[![Dependencies](https://img.shields.io/badge/dependencies-none-green.svg?label=Dependencies&style=plastic)](https://github.com/Degubi/Py-Seq/blob/master/setup.py)

- The api is very similar to java8 streams
- Lazy by default
- Made because of boredom

# Versions for other languages
- Javascript: https://github.com/Degubi/Js-Seq

# Installation
## Using pip:

```pip install git+https://github.com/Degubi/Py-Seq.git```
<br>

## Without pip:
```seq.py is available in the seq directory```

# Usage
## Importing:

```python
from seq import Sequence
```
## Creating sequences:
```python
Sequence.range(0, 10)                                    # 1 to 10 excluding 10
Sequence.range_closed(0, 10)                             # 1 to 10 including 10
Sequence.range(0, 10, 2)                                 # 1 to 10 stepping 2, excluding 10
Sequence.iterate(1, lambda k: k * 2)                     # 1, 2, 4, 8.... this sequence is infinite
Sequence.iterate(1, lambda k: k * 2, lambda k: k < 50)   # Same as the last one but taking values less than 50 (same as doing a takeWhile)
Sequence.generate(input)                                 # Generate strings with reading from console
Sequence.of(1, 3, 3, 7, 4, 2, 0)                         # Sequence of elements
Sequence.of([ 1, 2, 3 ])                                 # Create sequence from array
```

## Transforming sequences (intermediate operations):
- These operations do nothing by themselves, they only start doing work when the terminal operation gets called
- Function list:

<br>
<table>
    <tr>
        <td>filter</td>
        <td>map</td>
        <td>flat_map</td>
        <td>distinct</td>
    </tr>
    <tr>
        <td>take</td>
        <td>skip</td>
        <td>take_while</td>
        <td>skip_while</td>
    </tr>
    <tr>
        <td>sort</td>
        <td>sort_ascending</td>
        <td>sort_descending</td>
        <td>chunk</td>
    </tr>
</table>
<br>

- Examples:

```python
Sequence.range(0, 100)                 \  # Need to create a new sequence with every new pipeline
        .filter(lambda k: k % 2 == 0)  \  # Keep only even values in the sequence
        .map(lambda k: k * 2)          \  # Multiply them by 2
        .skip(2)                       \  # Skip the first 2 elements
        .take(10)                      \  # Take the first 10 elements only
        .sort_ascending()                 # Sort them in ascending order

Sequence.of({ 'prop1': 5, 'prop2': 'hey' }, { 'prop1': 5, 'prop2': 'ho'}, { 'prop1': 20, 'prop2': 'hi' }) \
        .distinct(lambda k: k['prop1'])        \  # Many functions have key selecting overloads, default is always identity
        .sort_descending(lambda k: k['prop1'])    # Same happens here

Sequence.of({ data: [ 1, 2, 3, 4 ] }, { data: [ 5, 6, 7, 8 ] })  \
        .flat_map(lambda k: k.data)                              \
        .take_while(lambda k: k < 6)
```

## Finishing sequences (terminal operations):
- Function list:

<br>
<table>
    <tr>
        <td>for_ach</td>
        <td>reduce</td>
        <td>to_list</td>
        <td>to_dictionary</td>
        <td>partition_by</td>
    </tr>
    <tr>
        <td>sum</td>
        <td>count</td>
        <td>average</td>
        <td>min</td>
        <td>max</td>
    </tr>
    <tr>
        <td>group_by</td>
        <td>first</td>
        <td>last</td>
        <td>join</td>
        <td>statistics</td>
    </tr>
    <tr>
        <td>all_matches</td>
        <td>any_matches</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
<br>

- Examples

```python
seq = Sequence.range(0, 100)        # Let's assume we recreate this sequence every time

seq.for_each(print)                 # Print every value to the console
seq.reduce(0, lambda k, l: k + l)   # Sum all values
seq.sum()                           # Shorthand for summing
seq.count()                         # Count number of elements in sequence
seq.min()                           # Find the smallest value in the sequence, has key selector overload
seq.max()                           # Find the largest value in the sequence, has key selector overload
seq.average()                       # Average of the values in the sequence
seq.to_list()                       # Collect all elements into an array
seq.first()                         # Find the first element in the sequence, this returns the element or null
seq.last()                          # Find the last element in the sequence, this returns the element or null
seq.join(',')                       # Join elements with a comma
seq.statistics()                    # Returns an object with sum, count, min, max, average properties

seq = Sequence.of({ 'prop1': 5, 'prop2': 'hey' }, { 'prop1': 20, 'prop2': 'hi' }, { 'prop1': 20, 'prop2': 'hey' })

# Creates an object where the keys are from 'prop1' and the corresponding values are from 'prop2'
# Note: This call throws an error because of the duplicate 'prop1: 20' key
seq.to_dictionary(lambda k: k['prop1'], lambda k: k['prop2'])

# This is the same as the last example, but this version handles the duplicate key problem by keeping the first value
seq.to_dictionary(lambda k: k['prop1'], lambda k: k['prop2'], lambda key, previousValue, currentValue: previousValue)

# Returns true if the given predicate is true for all elements of the sequence
seq.all_matches(lambda k: k['prop1'] > 0)

# Returns true if the given predicate is true for any of the elements of the sequence
seq.any_matches(lambda k: k['prop2'] == 'nope')

# Groups elements by 'prop1' where the values are the objects that had the same key
seq.group_by(lambda k: k['prop1'])

# This does the same as the last example
seq.group_by(lambda k: k['prop1'], Grouper.to_list())

# Groups elements prop1' where the value is the frequency of the key
seq.group_by(lambda k: k['prop1'], Grouper.counting())

# Groups elements by 'prop2' where the value is the sum of 'prop1'
seq.group_by(lambda k: k['prop2'], Grouper.summing(lambda k: k['prop1']))

# First array contains the elements where the predicate was true
matching, notMatching = seq.partition_by(lambda k: k['prop1'] % 2 == 0)
```