import os
from PIL import Image
from pdf2image import convert_from_path

path = r"files"
poppler = r"poppler\Library\bin"

files = os.scandir(path)
files = [file for file in files]

dpi = int(input("Insert DPI: "))
print("\n--------------------------------------------------\n")

for pdf in range(len(files)):
    image = convert_from_path(files[pdf].path, poppler_path=poppler, dpi=dpi)[0]
    image.save(f"images/{pdf + 1}.png", "PNG")

row = input("Enter rows (press Enter to leave empty): ")
column = input("Enter columns (press Enter to leave empty): ")
print("\n--------------------------------------------------\n")

while True:
    if (len(row) == 0 and len(column) == 0) or (len(row) != 0 and len(column) != 0):
        print("Invalid Inputs\n")

        row = input("Enter rows (press Enter to leave empty): ")
        column = input("Enter columns (press Enter to leave empty): ")
        print("\n--------------------------------------------------\n")
        
    elif len(row) == 0:
        column = int(column)
        row = round(len(files) / column)

        break
    elif len(column) == 0:
        row = int(row)
        column = round(len(files) / row)

        break

x = input("Enter width (press Enter to leave empty): ")
y = input("Enter height (press Enter to leave empty): ")
print("\n--------------------------------------------------\n")

while True:
    if (len(x) == 0 and len(y) == 0) or (len(x) != 0 and len(y) != 0):
        print("Invalid Inputs\n")

        x = input("Enter width (press Enter to leave empty): ")
        y = input("Enter height (press Enter to leave empty): ")
        print("\n--------------------------------------------------\n")

    elif len(x) == 0:
        y = int(y)
        x = round(y * 0.7)

        break
    elif len(y) == 0:
        x = int(x)
        y = round(x * 1.5)

        break

width = column * x
height = row * y

collage = Image.new("RGBA", (width, height))

digit = 0
for i in range(0, height, 100):
    for j in range(0, width, 70):
        if digit > (len(files) - 1):
            break
        else:
            img = Image.open(fr"images/{digit + 1}.png")
            img = img.resize((70, 100))

            collage.paste(img, (j, i))

        digit += 1

collage.save(fr"result/result.png", dpi=(300, 300))

