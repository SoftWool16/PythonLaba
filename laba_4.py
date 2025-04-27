from PIL import Image

with Image.open('C:/Users/Bill/Repos_From_SoftWool16/PythonLaba/image/Снимок_3-1.PNG') as image:


    print('Задание 3.1:')
    width, height = image.size
    print(f'Ширина: {width} пикселей')
    print(f'Высота: {height} пикселей')
    print('-------------')


    print('Задание 3.2:')
    image_3_2 = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_3_2.save("C:/Users/Bill/Repos_From_SoftWool16/PythonLaba/image/Снимок_3-2.PNG")
    print('-------------')


    print('Задание 3.3:')
    r, g, b, a = image.split()
    r = Image.eval(r, lambda x: 250 - x)
    g = Image.eval(g, lambda x: 250 - x)
    b = Image.eval(b, lambda x: 250 - x)
    a = Image.eval(b, lambda x: 250 - x)
    image_3_3 = Image.merge('RGB', (r, g, b))
    image_3_3.save("C:/Users/Bill/Repos_From_SoftWool16/PythonLaba/image/Снимок_3-3.PNG")

print('Задание 3.3:')
import numpy as np

random_array = np.random.rand(100)

reshaped_array = random_array.reshape(10, 10)

print(reshaped_array)
