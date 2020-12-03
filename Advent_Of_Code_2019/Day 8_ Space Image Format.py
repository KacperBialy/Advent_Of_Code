# PART 1
with open('./input_data/day8.txt', mode='r') as file:
    encoded_image = file.read().strip()
encoded_image_length = len(encoded_image)
layer_size = 25 * 6
layers_count = int(encoded_image_length / layer_size)
image = []
start = -layer_size
for i in range(layers_count):
    start += layer_size
    layer = encoded_image[start:start + layer_size]
    image.append(layer)
fewest_zeros = min(image, key=lambda var: var.count('0'))
print(fewest_zeros.count('1') * fewest_zeros.count('2'))

# PART 2

end_image = []
for i in range(layer_size):
    for j in range(layers_count):
        pixel = image[j][i]
        if pixel != '2':
            end_image.append(pixel)
            break
for i in range(layer_size):
    if end_image[i] == '1':
        print('#', end='')
    else:
        print(' ', end='')
    if i % 25 == 24:
        print()

