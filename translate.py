# -*- coding: utf-8 -*-
import leoapi
import View

def main():
    s = leoapi.get_session()
    print("Введите слово ('q' - для выхода):")
    word = input()
    while (word != "q"):
        row_translates = leoapi.get_row_translates(s, word)
        print("word - выберите перевод:")
        View.show_translate_variant(row_translates)
        try:
            num_translate = int(input())
        except ValueError:
            num_translate = 0
        if num_translate in range (1, len (row_translates)):
            leoapi.add_word(s, word, row_translates[num_translate-1]["value"])
            print("Слово добавлено. Введите новое слово.")
        else:
            print("Перевод не выбран. Введите новое слово.")
        word = input()
if __name__ == '__main__':
    main()
