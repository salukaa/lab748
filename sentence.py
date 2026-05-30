import copy


class Sentence:
    def __init__(self, source=None):
        if source is None:
            self._words = []
        elif isinstance(source, Sentence):
            self._words = copy.copy(source._words)
        elif isinstance(source, str):
            self._words = source.split()
        elif isinstance(source, list):
            self._words = list(source)
        else:
            raise TypeError(f"Непідтримуваний тип: {type(source)}")

    def __len__(self):
        return len(self._words)

    def __getitem__(self, index):
        return self._words[index]

    def __setitem__(self, index, value):
        self._words[index] = value

    def __contains__(self, word):
        return word in self._words

    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(self._words + other._words)
        if isinstance(other, str):
            return Sentence(self._words + [other])
        raise TypeError(f"Непідтримуваний тип: {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Sentence):
            exclude = set(other._words)
            return Sentence([w for w in self._words if w not in exclude])
        if isinstance(other, str):
            result = list(self._words)
            try:
                result.remove(other)
            except ValueError:
                pass
            return Sentence(result)
        raise TypeError(f"Непідтримуваний тип: {type(other)}")

    def __str__(self):
        return f"Sentence(слів={len(self._words)}): {' '.join(self._words)}"

    def __repr__(self):
        return f"Sentence({self._words!r})"

    def words(self):
        return list(self._words)

    def as_text(self):
        return " ".join(self._words)