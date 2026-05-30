from sentence       import Sentence
from text_processor import TextProcessor

SEP = "-" * 50

class Main:
    def __init__(self, filepath, replacements, deletions):
        self.filepath     = filepath
        self.replacements = replacements
        self.deletions    = deletions

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

    def run(self):
        print(f"\n{SEP}")
        print("Обробка текстового файлу")
        print(SEP)

        processor = TextProcessor(self.filepath)
        print(f"До редагування: {processor}\n")

        processor.replace_words(self.replacements).delete_words(self.deletions)

        print(f"Після редагування:\n{processor.as_text()}")
        print(f"Загальна кількість слів: {processor.word_count()}")

        print(f"\nДокладно:\n{processor}")


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
    app.run()