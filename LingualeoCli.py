# coding: utf-8

import appex
import console
import leoapi


def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    text = appex.get_text().strip('* \n')
    if not text:
        print('No text input found.')
        return
    s = leoapi.get_session()
    row_translates = leoapi.get_row_translates(s, text)
    all_t = ""
    for t in row_translates:
        all_t += "- " + t["value"] + "\n"
    first_translate = row_translates[0]["value"]
    
    answer = console.alert(text, 
    '%s' % (all_t), 'Добавить в словарь', 'Отменить', hide_cancel_button=True)
    if (answer == 1):
        leoapi.add_word(s, text, first_translate)
    
    console.alert("Слово добавлено", "", 'OK', hide_cancel_button=True)

if __name__ == '__main__':
    main()
