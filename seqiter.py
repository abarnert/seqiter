from collections.abc import Sequence, Iterator

class SeqIter(Sequence, Iterator):
    def __init__(self, elts, _pos=-1):
        self._elts = list(elts)
        self._pos = _pos
    def __next__(self):
        self._pos += 1
        try:
            return self._elts[self._pos]
        except IndexError:
            raise StopIteration
    def __iter__(self):
        return self
    def __getitem__(self, idx):
        return self._elts[idx]
    def __len__(self):
        return len(self._elts)
    def __repr__(self):
        return '{}({}, _pos={})'.format(
            type(self).__name__, self._elts, self._pos)

s = SeqIter([1, 2, 3, 4])
print(s[0], s)
print('nexting:', next(s))
print(s[0], s)
print('listing:', list(s))
print(s[0], s)
print('listing:', list(s))
print(s[0], s)

