def single_root_words(root_word, words):
    # Создаем пустой список для однокоренных слов
    single_root = []
    # Перебираем каждое слово в списке words
    for word in words:
        # Если слово начинается с root_word и имеет одинаковую длину с root_word, добавляем его в список single_root
        if word.startswith(root_word) and len(word) == len(root_word):
            single_root.append(word)
    # Возвращаем список однокоренных слов
    return single_root

# Пример использования функции
root_word = 'rich'
words = ["richiest', 'orichalcum', 'cheers', 'richies"]
print(single_root_words(root_word, words))

