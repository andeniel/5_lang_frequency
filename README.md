# Анализ частоты слов

Скрипт позволяет подсчитать количество слов в тексте и выводит в консоль десять самых популярных слов в порядке убывания частоты. 

Для этого вам нужен текстовый файл. Для примера можете скачать книгу [Moby Dick с сайта samolit.com](http://samolit.com/downloads/download.php?book_id=4862&format=txt)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash
# Программа принимает 1 параметр
# python3 lang_frequency.py -f [путь к файлу]
# -f [указываем путь к текстовому файлу]

$ python3 lang_frequency.py -f ru_sample.txt
# пример ответа скрипта
Часто используемые слова в тексте:
что     3646
как     1913
его     1876
она     1195
сказал  1145
было    1137
это     1030
так     952
ему     882
всё     839

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
