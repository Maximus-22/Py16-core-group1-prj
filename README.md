![](https://www.python.org/static/favicon.ico)

# Гаджет "Персональний помічник" з інтерфейсом командного рядка.

    Файл в пакеті, який запускає гаджет __[personal_assistant.py]__.
    Здійснення запуску гаджету з командної строки (за умови встановлення пакету у робоче оточення) виконується за командою __[assist]__.
    Гаджет надає доступ до наступних додатків:

**1. Адресна книга**\
**2. Нотатки**\
**3. Сортування файлів**\
**4. Калькулятор**\
**5. Гра Бандеро-Гусак**

## Адресна книга.

    Додаток дозволяє створювати структуровані записи контактних осіб наступного вигляду:

**Ім'я:** `[Name]`\
**Адреса:** `[Address]`\
**Телефон:** `[Phone]`\
**Е-пошта:** `[E-mail]`\
**День народження:** `[Birthday]`

    Скріпт дозволяє виконуваити:

- _зберігання контактів з іменами, адресами, номерами телефонів, e-mail та днями народження до книги контактів;_
- _виведення списку контактів, у яких день народження через задану кількість днів від поточної дати;_
- _перевірку валідності введеного номера телефону та e-mail під час створення або редагування запису та повідомлення користувача у разі некоректного введення;_
- _здійснення пошуку контактів серед записів адресної книги;_
- _редагування та видалення записів з книги контактів._\
   За замовчуванням збереження записів користувача відбувається у файл **[addressbook.json]**.
  Передбачена можливість додавання додаткових телефонів контактних осіб у поле **[Phone]**.

## Нотатки.

    Додаток дозволяє створювати невеличкі записи, які мають заголовок, основний текст та тегі.
    За замовчуванням збереження записів користувача відбувається у файл __[notes.json]__.
    Скріпт дозволяє виконуваити:

- _зберігання нотатків з текстовою інформацією;_
- _проведення пошуку за нотатками;_
- _редагування та видалення нотаток;_
- _додавання в нотатки "тегів", - це ключові слова, що описують тему та предмет запису;_
- _здійснення пошуку та сортування нотаток за ключовими словами (тегами)._

## Сортування файлів.

    Скрипт приймає один аргумент з командної строки — це ім'я папки, в якій він буде проводити сортування. Додаток проходить на будь-яку глибину вкладеності та сортирує всі файли по групам:

- _архіви `("GZTAR", "TAR", "ZIP")`;_
- _аудіо файли `("AMR", "MP3", "OGG", "WAV")`;_
- _відео файли `("AVI", "MKV", "MOV", "MP4")`;_
- _документи `("DOC", "DOCX", "PDF", "PPTX", "TXT", "XLS", "XLSX")`;_
- _зображення `("GIF", "JPEG", "JPG", "PNG", "SVG")`;_
- _невідомі розширення._\
   При переносі файлів додаток перекладає кириличні символи у транслітерацію відповідно до таблиці транслітерації. Якщо архив розпаковується без помилки, у гілці з архивами створюється тека з файламі з його назвою; в іншому випадку файл архиву тільки переміщюється у відповідну групу.

## Калькулятор.

    Програма, яка виконує найпростіші математичні операції з числами послідовно, приймаючи від користувача операнди (числа) та оператор. Вміє виконувати наступні математичні операції: додавання __[+]__, віднімання __[-]__, множення __[*]__, ділення __[/]__. Додаток виводить результат обчислень, коли отримує від користувача символ __[=]__.

## Гра Бандеро-Гусак.

    Візуалізований антістресовий код, який дозволяє допомогти Гусакові долетіти до московії та якісно зробити свою справу.

---

## Встановлення пакету "Персональний помічник" з [test.pypi.org](https://test.pypi.org).

### 1. Створення робочої текі:

```
    D:\Python area\Packages>mkdir Test
```

### 2. Перехід у робочу теку та створення віртуального оточення:

```
    D:\Python area\Packages>cd Test
    D:\Python area\Packages\Test>py -m venv venv_test
    D:\Python area\Test>cd venv_test\Scripts
    D:\Python area\Test\venv_test\Scripts>activate
    (venv_test) D:\Python area\Test\venv_test\Scripts>cd ../../
```

### 3. Встановлення пакету pygame:

```
    (venv_test) D:\Python area\Packages\Test>pip install pygame
```

### 4. Встановлення пакету "Персональний помічник":

```
    (venv_test) D:\Python area\Packages\Test>pip install -i https://test.pypi.org/simple/ assistant-mmv22
```

### 5. Запуск програми "Персональний помічник" за допомогою команди-аліаса:

```
    (venv_test) D:\Python area\Packages\Test>assist
```

> **Приємного користування. :)**
>
> **Команда [Python Patroll](https://drive.google.com/file/d/1bV_tYCc-zHcm1j-eM1a8RadpeWBChVDu/view?usp=sharing).**
