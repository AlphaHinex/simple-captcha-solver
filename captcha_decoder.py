from PIL import Image
import sys

def decoder(
        im,
        threshold=100,
        mask="vc.bmp",
        alphabet="0123456789"):

    img = Image.open(im)
    img = img.convert("RGB")
    # minimize verified code area in the input image
    box = (4, 3, 46, 12)
    img = img.crop(box)
    pixdata = img.load()

    # open the mask
    letters = Image.open(mask)
    ledata = letters.load()

    letterlist = []

    def test_letter(img, letter, alphabet):
        A = img.load()
        B = letter.load()
        mx = 1000000
        max_x = 0
        for x in range(img.size[0] - letter.size[0] + 1):
            _sum = 0
            for i in range(letter.size[0]):
                for j in range(letter.size[1]):
                    _sum = _sum + abs(A[x + i, j][0] - B[i, j][0])
            if _sum < mx:
                mx = _sum
                max_x = x
            if _sum == mx and max_x != x and  _sum < threshold * 10:
                # print("a: %d, %d; b: %d, %d" % (max_x, mx, x, _sum))
                letterlist.append((_sum, alphabet, x))
        letterlist.append((mx, alphabet, max_x))

    # Clean the background noise, if color != white, then set to black.
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if (pixdata[x, y][0] > threshold) \
                    and (pixdata[x, y][1] > threshold) \
                    and (pixdata[x, y][2] > threshold):
                # black
                pixdata[x, y] = (0, 0, 0, 255)
            else:
                # white
                pixdata[x, y] = (255, 255, 255, 255)
    # img.save("/Users/alphahinex/Desktop/BoW.jpg")

    counter = 0
    old_x = -1

    for x in range(letters.size[0]):
        black = True
        for y in range(letters.size[1]):
            if ledata[x, y][0] != 0:
                black = False
                break
        if black:
            # one digit box, (left, upper, right, lower)
            box = (old_x + 1, 0, x, 9)
            letter = letters.crop(box)
            # letter.save("/Users/alphahinex/Desktop/" + alphabet[counter] + ".jpg")
            test_letter(img, letter, alphabet[counter])
            old_x = x
            counter += 1

    box = (old_x + 1, 0, 65, 9)
    letter = letters.crop(box)
    test_letter(img, letter, alphabet[counter])
    # letter.save("/Users/alphahinex/Desktop/" + alphabet[counter] + ".jpg")

    t = sorted(letterlist)
    t = t[0:4]  # 4-letter captcha
    # use threshold to filter matched letters
    t = filter(lambda l: l[0] < threshold * 10, t)

    final = sorted(t, key=lambda e: e[2])

    answer = ''.join(map(lambda l: l[1], final))
    return answer

if __name__ == '__main__':
    print(decoder(sys.argv[1]))
