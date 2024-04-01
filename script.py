import copy

import pyperclip
from PIL import Image


def refine_pixels(pixels):

    # takes raw pixel data and returns a list of all pixels in order
    # each element of the returned list will be an integer

    spam = str(pixels)[2 : len(str(pixels)) - 2]
    new_pixels = ""
    for character in spam:
        if character != "(" and character != ")":
            new_pixels += character
        else:
            continue
    temp = new_pixels.split(", ")
    refined = []
    for i in temp:
        refined.append(int(i))

    if EASY:
        return refined
    else:
        t = []
        a = 1
        for i in refined:
            if a % 4 != 0:
                t.append(i)
            a += 1
        return t


def get_binary(message):

    ## An example of how it works (this is dumb, I know):
    
    ## basically, each word is separated by a `@`, which is then dealt with accordingly in the
    ## `mutate` function. The end of this so-called binary string is signified by the `!` at the end
    ## which signals the program to stop reading the thing further.

    # >>> message
    # 'ab'
    # >>> binary = []
    # >>> for i in message: binary += list(bin(ord(i))[2:].rjust(8, "0") + "@")
    # ... 
    # >>> binary
    # ['0', '1', '1', '0', '0', '0', '0', '1', '@', '0', '1', '1', '0', '0', '0', '1', '0', '@']
    # >>> binary = binary[: len(binary) - 1] + list("!")
    # >>> binary
    # ['0', '1', '1', '0', '0', '0', '0', '1', '@', '0', '1', '1', '0', '0', '0', '1', '0', '!']

    binary = []
    for i in message:
        binary += list(bin(ord(i))[2:].rjust(8, "0") + "@")
    binary = binary[: len(binary) - 1] + list("!")
    return binary


def mutate(pixels):
    pixels = refine_pixels(pixels)
    binary = get_binary(message)
    new_pixels = []
    done_reading = False
    for i in range(0, len(pixels), 3):
        for j in range(i, i + 3):

            # here, we're going over each channel in this loop
            # we're also reading the bits in our so-called binary string
            # now, depending on the value of each bit, sy 1 or 0, (or even @), we
            # change the vlaues of the channels slightly... this operation comes to a stop when
            # the bit reads `!`

            # the function decoding the image simply does the opposite of this
            # this makes this program really non-standard and personally, kinda dumb lol

            if binary[j] == "1":
                if pixels[j] % 2 == 0:
                    new_pixels.append(pixels[j] + 1)
                else:
                    new_pixels.append(pixels[j])
            if binary[j] == "0":
                if pixels[j] % 2 == 0:
                    new_pixels.append(pixels[j])
                else:
                    new_pixels.append(pixels[j] - 1)
            if binary[j] == "@":
                if pixels[j] % 2 == 0:
                    new_pixels.append(pixels[j])
                else:
                    new_pixels.append(pixels[j] - 1)
            if binary[j] == "!":
                if pixels[j] % 2 == 0:
                    new_pixels.append(pixels[j] + 1)
                else:
                    new_pixels.append(pixels[j])
                done_reading = True
                break
        if done_reading:
            break
    # at this point, all the required pixls have been modified
    # it is time to append the remaining original ones
    temp = copy.copy(new_pixels)
    temp += pixels[len(temp) :]
    return temp


def cluster(pixels):
    pixels = mutate(pixels)
    temp_pixels = []
    for i in range(0, len(pixels), 3):
        temp_pixel = []
        for j in range(i, i + 3):
            temp_pixel.append(pixels[j])
        temp_pixels.append(tuple(temp_pixel))
    return temp_pixels


def encode(pixels):
    pixels = cluster(pixels)
    im2 = Image.new(im.mode, im.size)
    im2.putdata(pixels)
    im2.save("new.png")


def get_message_in_binary(pixels):
    pixels = refine_pixels(pixels)
    binary = []
    a = 1
    for i in pixels:
        if a % 9 == 0:
            if i % 2 != 0:
                break

        else:
            if i % 2 != 0:
                binary.append(1)
            else:
                binary.append(0)
        a += 1

    return binary


def get_message(pixels):
    pixels = get_message_in_binary(pixels)
    string = ""
    for i in range(0, len(pixels), 8):
        temp = ""
        for j in range(i, i + 8):
            temp += str(pixels[j])
        string += chr(int(temp, 2))
    return string


EASY = True
print("STEGANOGRAPHY".center(80, "-"))
print("Enter 1 to encode and 2 to decode: ", end="")
answer = int(input())
if answer == 1:
    print("Enter image path: ", end="")
    path = input().strip()
    im = Image.open(path)
    pixels = list(im.getdata())
    if len(pixels[0]) > 3:
        EASY = False
    print(
        "Do you want to use your clipboard contents as your message to be encoded? [Y/N]: ",
        end="",
    )
    choice = input().upper()
    if choice == "Y":
        message = pyperclip.paste()
    else:
        print("Enter the message to be encoded: ", end="")
        message = input().strip()
    encode(pixels)
    print("...".center(80))
    print("The encoded image has been saved as 'new.png' in this working directory")
    print("...".center(80))
    print("DONE".center(80, "-"))
else:
    print("Enter image path: ", end="")
    path = input().strip()
    im = Image.open(path)
    pixels = list(im.getdata())
    if len(pixels[0]) > 3:
        EASY = False
    print("The message is:")
    print(get_message(pixels))
    print("DONE".center(80, "-"))
