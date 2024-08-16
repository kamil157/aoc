with open('2019/inputs/day08.txt') as f:
    input = f.read()


def checksum(s, w, h):
    layers = [s[i:i + w * h] for i in range(0, len(s), w * h)]
    best_layer = min(layers, key=lambda layer: layer.count('0'))
    return best_layer.count('1') * best_layer.count('2')


assert checksum('123456789012', 3, 2) == 1

print(checksum(input, 25, 6))


def image(s, w, h):
    layers = [s[i:i + w * h] for i in range(0, len(s), w * h)]

    data = []
    for i in range(w * h):
        for l in layers:
            if l[i] == '1':
                data.append('#')
                break
            elif l[i] == '0':
                data.append(' ')
                break

    for y in range(h):
        print(' '.join(data[y * w:y * w + w]))


image(input, 25, 6)
