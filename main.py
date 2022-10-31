import PIL.Image
import os

#ascii_chars = '@#$%&/*;:-+=,."      ' 
ascii_chars = 'N@#W$9876543210?!abc:;+=-,._ '

def resize_image(image, new_width=300):
    width, height = image.size
    ratio = height / width / 2.3
    new_height = int(new_width * ratio)
    resized_image = image.resize(([new_width, new_height]))
    return (resized_image)


def graify(img):
    grayscale_image = img.convert('L')
    return (grayscale_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ascii_chars[pixel//25] for pixel in pixels])
    return (characters)


def main(new_width=300):
    for i in os.listdir(r'image/'):
        path = 'image/{}'.format(i)
        print(path)
        try: image = PIL.Image.open(path)
        except: raise Exception('Path does not exist')
        resized = resize_image(image, new_width)
        graifyed = graify(resized)
        new_image_data = pixels_to_ascii(graifyed)
        pixel_count = len(new_image_data)
        ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
        #print(ascii_image)
        with open('asciis/{filename}.txt'.format(filename=i), 'w') as f:
            f.write(ascii_image)

main(new_width=500)