import copy


class SentenceError(Exception):

    INVALID_WORD_TYPE   = "invalid_word_type" # спроба записати не рядок як слово речення
    INVALID_ADD_OPERAND = "invalid_add_operand" # правий операнд + не є Sentence або str
    INVALID_SUB_OPERAND = "invalid_sub_operand" # правий операнд - не є Sentence або str

    def __init__(self, code: str, **kwargs):
        self.code = code

        if code == self.INVALID_WORD_TYPE:
            got  = kwargs.get("got_type", "?")
            idx  = kwargs.get("index", "?")
            msg  = (
                f"Слово речення має бути рядком (str), "
                f"але отримано '{got}' для індексу [{idx}]."
            )

        elif code == self.INVALID_ADD_OPERAND:
            got = kwargs.get("got_type", "?")
            msg = (
                f"Оператор '+' підтримує лише Sentence або str, "
                f"але правий операнд має тип '{got}'."
            )

        elif code == self.INVALID_SUB_OPERAND:
            got = kwargs.get("got_type", "?")
            msg = (
                f"Оператор '-' підтримує лише Sentence або str, "
                f"але правий операнд має тип '{got}'."
            )

        else:
            msg = f"Невідома помилка Sentence (код: {code})."

        super().__init__(msg)

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
        if not isinstance(value, str):
            raise SentenceError(
                SentenceError.INVALID_WORD_TYPE,
                got_type=type(value).__name__,
                index=index,
            )
        self._words[index] = value

    def __contains__(self, word):
        return word in self._words

    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(self._words + other._words)
        if isinstance(other, str):
            return Sentence(self._words + [other])
        raise SentenceError(
            SentenceError.INVALID_ADD_OPERAND,
            got_type=type(other).__name__,
        )

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
        raise SentenceError(
            SentenceError.INVALID_SUB_OPERAND,
            got_type=type(other).__name__,
        )

    def __str__(self):
        return f"Sentence(слів={len(self._words)}): {' '.join(self._words)}"

    def __repr__(self):
        return f"Sentence({self._words!r})"

    def words(self):
        return list(self._words)

    def as_text(self):
        return " ".join(self._words)