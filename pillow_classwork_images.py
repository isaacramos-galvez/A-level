from PIL import Image as i
image = i.open("landscape.png")
image.show()
#print(f"Format : {image.format}, Size : {image.size}, Mode: {image.mode}")


new_image = i.new('R', (255, 255))
pixels = new_image.load()
for y in range(255):
    for x in range(255):
        pixels[x, y] = (x, y, 255)
        #print(f'x:{x}, y:{y}, RGB:{pixels[x, y]}')

new_image.show()









