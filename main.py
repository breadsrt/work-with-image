from PIL import Image, ImageFilter, ImageEnhance

image = Image.open("трава.jpg")

while True:
    print("1.Показати зображення")
    print("2.Зберегти зображення")
    print("3.Зробити ч/б")
    print("4.")
    print("5.")
    operation = input("Введіть операцію")
    if operation == "1":
        image.show()
    elif operation == "2":
        name = input("введіть назву файлу")
        image.save(name)
    elif operation == "3":
        image = image.convert("L")
    elif operation == "4":
        image = image.filter(ImageFilter.BLUR)
    elif operation == "5":
        image = ImageEnhance.Brightness(image).enhance(0.3)
