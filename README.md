# LinguaLeo Clipboard Translator for IOS (Pythonista)
![alt text](https://img.shields.io/badge/Pythonista-3.3-blue.svg "Pythonista 3.3")

Расширение для приложения Pythonista.

Переводите слова и фразы в любых приложениям на IOS. Пополняйте личный словарь на сайте LinguaLeo.

## Установка
Выполните в консоли приложения Pythonista следующий код:
```Python
import requests
open('LingualeoCli.py', 'wb').write(requests.get('https://raw.githubusercontent.com/r6i/LeoPy/master/LingualeoCli.py').content)
```
В настройках приложения в разделе *APP EXTENSIONS* выбираем пункт **Share Extension Shortcuts**. Нажимаем **"+"**. Выбираем скаченный файл **LingualeCli.py**. По желанию, вводим название в поле *Custom Title*, меняем иконку и цвет виджета. Нажимаем кнопку **Add**.

## Использование
1. Выделяем текст. Нажимаем "Поделиться":
<p align="center">
  <img src="https://i.ibb.co/yFHKXQy/1.jpg" alt="Select text. Click on \"Share\"" width="738">
</p>
2. Нажимаем "Run Pythonista Script":
<p align="center">
  <img src="https://i.ibb.co/XyTHxxh/2.jpg" alt="Click on \"Run Pythonista Script\"" width="738">
</p>
3. Выбираем созданный нами виджет.
<p align="center">
  <img src="https://i.ibb.co/TtGgPsQ/3.jpg" alt="Click widget"" width="738">
</p>
4. Добавляем слово в словарь
<p align="center">
  <img src="https://i.ibb.co/7RBr0Ld/4.jpg" alt="Add word"" width="738">
</p>

## История версий
### [1.0.0] - 2020-03-30
- **Реализован** вывод всех переводом в одно окно.
- **Реализовано** сохранение файлов Куки после первой авторизации.

[1.0.0]:https://github.com/r6i/LingualeoCli/tree/0888c7ebb99c77a837ec5ca390a3be3b964d381d
