reco-kasko-calc
===============

РЕСО Калькулятор КАСКО

#Настройка локальной машины для запуска скрипта
 
 1. Установить Google Chrome
 2. Скачать последнюю версию chromedriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) и положить в C:\Windows
 3. Установить последнюю версию Python (https://www.python.org/downloads/)
 4. Прописать в переменную окружения PATH к установленному каталогу с python.exe (по умолчанию это C:\Python\) и добавить путь к C:\Python\Scripts
 5. Установить git-клиента https://git-scm.com/downloads
 6. Запустить консоль git
 7. Клонировать репозиторий себе на локальную машину
```bash
git clone https://github.com/efpato/reco.git
```
 8. Перейти в склонированный каталог и выполнить:
```bash
cd reco
python -m pip install -r requirements.txt
```

УСПЕХ! Вы готовы к использованию скрипта локально на своей виндовой машине

#Использование

```bash
python kasko-calc sample.xls
```
На выходе получаем Excel-файл sample.out.xlsx
