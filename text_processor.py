from sentence import Sentence

PUNCT = ".,!?;:\"'()-—…"


class TextProcessor:
    def __init__(self, source):
        """
        source: шлях до файлу або TextProcessor
        """
        if isinstance(source, TextProcessor):
            self._sentences = [Sentence(s) for s in source._sentences]
            self._endings   = list(source._endings)
        elif isinstance(source, str):
            self._sentences = []
            self._endings   = []
            self._load(source)
        else:
            raise TypeError(f"Непідтримуваний тип: {type(source)}")


    def _load(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                self._endings.append("\n" if line.endswith("\n") else "")
                self._sentences.append(Sentence(line.rstrip("\n")))


    @staticmethod
    def _strip_punct(word):
        return word.strip(PUNCT)

    @staticmethod
    def _transfer_punct(original, new_word):
        leading, trailing = "", ""
        i = 0
        while i < len(original) and original[i] in PUNCT:
            leading += original[i]; i += 1
        j = len(original) - 1
        while j >= 0 and original[j] in PUNCT:
            trailing = original[j] + trailing; j -= 1
        return leading + new_word + trailing

    def replace_words(self, replacements: dict):
        """Замінює слова згідно зі словником {старе: нове}. Повертає self."""
        new_sentences = []
        for sentence in self._sentences:
            new_words = []
            for w in sentence.words():
                key = self._strip_punct(w).lower()
                new = replacements.get(key)
                new_words.append(self._transfer_punct(w, new) if new else w)
            new_sentences.append(Sentence(new_words))
        self._sentences = new_sentences
        return self

    def delete_words(self, deletions: list):
        """Видаляє слова зі списку. Повертає self."""
        exclude = {w.lower() for w in deletions}
        self._sentences = [
            Sentence([w for w in s.words()
                      if self._strip_punct(w).lower() not in exclude])
            for s in self._sentences
        ]
        return self

    def word_count(self):
        return sum(len(s) for s in self._sentences)

    def __str__(self):
        lines = "\n".join(
            f"  [{i+1}] {s.as_text()}"
            for i, s in enumerate(self._sentences)
        )
        return (f"TextProcessor(рядків={len(self._sentences)}, "
                f"слів={self.word_count()}):\n{lines}")

    def __repr__(self):
        return f"TextProcessor(sentences={len(self._sentences)})"