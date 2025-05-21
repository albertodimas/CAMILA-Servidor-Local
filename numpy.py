class ndarray(list):
    """Minimal ndarray supporting sum() and shape for tests."""
    def __init__(self, data):
        if isinstance(data, ndarray):
            data = list(data)
        super().__init__(data)
        self._data = data

    def sum(self):
        if self._data and isinstance(self._data[0], (list, tuple, ndarray)):
            return sum(float(x) for row in self._data for x in row)
        return sum(float(x) for x in self._data)

    @property
    def shape(self):
        if self._data and isinstance(self._data[0], (list, tuple, ndarray)):
            return (len(self._data), len(self._data[0]))
        return (len(self._data),)

def array(data):
    return ndarray(data)

def argmax(seq):
    """Return the index of the maximum value in a sequence."""
    if isinstance(seq, ndarray):
        seq = list(seq)
    return max(range(len(seq)), key=lambda i: seq[i])
