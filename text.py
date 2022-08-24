# pip install easyocr
# pip install pytesseract
# pip install Pillow

import os.path

import easyocr
import pytesseract
from PIL import Image

# путь к исполняемому файлу tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# распозавание с помощью pytesseract, открытие картинки PIL.Image
def teseract_recognition(path_img):
    return pytesseract.image_to_string(Image.open(path_img), lang='rus+eng', config=r'--oem 3 --psm 6')


# распознавание с помощью easyocr, параметры: отключена детализация вывода,
# включены параграфы и установлена точность текста
def easyocr_recognition(path_img):
    return easyocr.Reader(["ru"]).readtext(path_img, detail=0, paragraph=True, text_threshold=0.8)


# сохранение текста в текстовый файл
def save_text(text, name):
    with open(f'{name}.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    print(f'[+] Распознанный текст сохранен в файл: "{name}.txt"')
    main()
    return


# ввод данных и выбор библиотеки для распознавания
def main():
    path_img = input('\n[+] Введите путь к картинке\n - Для выхода введите x\n   >>> ')
    if path_img == "x":
        exit(0)
    if not os.path.exists(path_img):
        print('[+] Картинки не существует')
        main()

    user_change = input('\n[+] Выберите библиотеку для распознавания текста:\n   [1] Tesseract OCR\n   '
                        '[2] EasyOCR\n   [3] Выход\n   >>> ')
    if user_change == "1":
        save_text(teseract_recognition(path_img), os.path.split(path_img)[1].split(".")[0])
    elif user_change == '2':
        save_text(easyocr_recognition(path_img), os.path.split(path_img)[1].split(".")[0])
    elif user_change == "3":
        exit(0)
    else:
        print('[+] Неопознанный ввод. Повторите все сначала')
        main()


if __name__ == "__main__":
    main()