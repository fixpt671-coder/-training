import re

class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self) -> dict:
        all_words = {}
        for file in self.file_names:
            with open(file, encoding = "utf-8") as f:
                text = f.read().lower()
                text = re.sub("[',' | '.' | '=' | '!' | '?' | ';' | ':' | ' - ' | '\n']", ' ' , text)
                text = text.split()
                all_words[f.name] = text

        return all_words

    def find(self, word: str):
        res = {}
        for i, j in self.get_all_words().items():
            if word.lower() in j:
                res[i] = j.index(word.lower())
        return res

    def count(self, word : str):
        res = {}
        for i, j in self.get_all_words().items():
            res[i] = j.count(word.lower())
        return res


with open('test_file.txt', 'w', encoding = "utf-8") as file:
    file.write("""
    It's a text for task. Найти везде,
    Используйте его для самопроверки.
    Успехов в решении задачи!
    text text text 
    """)

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
