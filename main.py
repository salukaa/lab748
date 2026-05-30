from sentence       import Sentence, SentenceError
from text_processor import TextProcessor

SEP = "-" * 50


class Main:
    def __init__(self, filepath, replacements, deletions):
        self.filepath     = filepath
        self.replacements = replacements
        self.deletions    = deletions

    # демонстрація звичайної роботи Sentence
    def demo_sentence(self):

        print(SEP)
        print("Демонстрація класу Sentence")
        print(SEP)

        s1 = Sentence("Сьогодні чудова погода і сонце світить")
        s2 = Sentence("Діти грають у дворі та сміються")
        print(s1)
        print(s2)

        # copy-constructor
        s_copy = Sentence(s1)
        print(f"\nКопія s1: {s_copy}")

        # len, []
        print(f"\nlen(s1)={len(s1)}, s1[0]='{s1[0]}', s1[2]='{s1[2]}'")

        # запис через []
        s1[0] = "Завтра"
        print(f"Після s1[0]='Завтра': {s1}")

        # +
        print(f"\ns1 + s2:      {s1 + s2}")
        print(f"s1 + 'завжди': {s1 + 'завжди'}")

        # -
        print(f"\n(s1+s2) - s2: {(s1 + s2) - s2}")
        print(f"s1 - 'Завтра': {s1 - 'Завтра'}")

        # in
        print(f"\n'сонце' in s1: {'сонце' in s1}")
        print(f"'дощ'   in s1: {'дощ'   in s1}")

    # демонстрація виключень SentenceError
    def demo_errors(self):
        print(f"\n{SEP}")
        print("Демонстрація виключень SentenceError")
        print(SEP)

        s = Sentence("Сьогодні чудова погода")

        # 1) __setitem__ — не рядковий тип
        for wrong_value in (42, 3.14, ["слово"], None):
            try:
                s[0] = wrong_value
            except SentenceError as e:
                print(f"[{e.code}]  s[0] = {wrong_value!r:<12} -> {e}")

        print()

        # 2) __add__ — неприпустимий тип правого операнда
        for wrong_value in (100, ["слово"], {"ключ": "значення"}):
            try:
                _ = s + wrong_value
            except SentenceError as e:
                print(f"[{e.code}]  s + {wrong_value!r:<20} -> {e}")

        print()

        # 3) __sub__ — неприпустимий тип правого операнда
        for wrong_value in (True, (1, 2), 0.5):
            try:
                _ = s - wrong_value
            except SentenceError as e:
                print(f"[{e.code}]  s - {wrong_value!r:<20}  ->  {e}")

    # ── обробка файлу ─────────────────────────────────────────────

    def run(self):
        print(f"\n{SEP}")
        print("Обробка текстового файлу")
        print(SEP)

        processor = TextProcessor(self.filepath)
        print(f"До редагування: {processor}\n")

        processor.replace_words(self.replacements).delete_words(self.deletions)

        print(f"Після редагування: {processor}")

if __name__ == "__main__":
    app = Main(
        filepath="input.txt",
        replacements={
            "чудова":  "прекрасна",
            "смачний": "чудовий",
            "цікаву":  "захопливу",
        },
        deletions=["голосно", "яскраво", "щодня"],
    )

    app.demo_sentence()
    app.demo_errors()
    app.run()