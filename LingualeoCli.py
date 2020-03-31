# coding: utf-8

import appex
from html2text import html2text
import console
import re
import leoapi
import View


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
    first_translate = row_translates[0]["value"]
    answer = console.alert('Добавить слово в словарь?', 
    '%s - %s' % (text, first_translate), 'Yes', 'No', hide_cancel_button=True)
    if (answer == 1):
        leoapi.add_word(s, text, first_translate)

if __name__ == '__main__':
    main()
