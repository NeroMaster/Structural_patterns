from translator.english_to_russian_translator import EnglishToRussianTranslator
from ambassador import Ambassador

def main():
    translator = EnglishToRussianTranslator()
    english_ambassador = Ambassador(translator)
    english_ambassador.greet("Vladimir")

if __name__ == "__main__":
    main()
