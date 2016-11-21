reco-kasko-calc
============

РЕСО Калькулятор КАСКО

#Настройка локальной машины для запуска скрипта
 
 1. Установить Firefox
 2. Установить Python (https://www.python.org/downloads/release/python-342/)
 3. Прописать в переменную окружения PATH к установленному каталогу с python.exe (по умолчанию это C:\Python34\) и добавить путь к C:\Python34\Scripts
 4. Установить tesseract https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download
 5. Установить git-клиента https://git-scm.com/downloads
 6. Запустить консоль git
 7. Клонировать репозиторий себе на локальную машину
```bash
git clone https://github.com/efpato/reco.git
```
 7. Перейти в склонированный каталог и выполнить:
```bash
cd reco
pip install -r requirements.txt
```

УСПЕХ! Вы готовы к использованию скрипта локально на своей виндовой машине

#Использование

```bash
python kasko-calc sample.xlsx
```
На выходе получаем Excel-файл sample.out.xlsx
