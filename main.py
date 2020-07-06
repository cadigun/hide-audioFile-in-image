#!/usr/bin/env python2
from PIL import Image
import binascii, optparse

delimiter = '110101010101010101010101010101011'
ksize = len(delimiter)

def getAudio2Str(filename):
    message = ''
    audio = open(filename, 'rb')
    print('reading audio file...')
    for line in audio.readlines():
        message += str(line)
    audio.close()
    return message


def getStr2Audio(message):
    with open('extracted', 'wb') as file:
        file.write(message)
    file.close()


def str2bin(message):
    binary = bin(int(binascii.hexlify(message), 16))
    return binary[2:]+delimiter


def bin2str(binary):
    message = binascii.unhexlify('%x' % (int('0b' + binary, 2)))
    return message

def hide(filename, filepath):
    data = Image.open(filename).convert('RGBA')
    strAudio = getAudio2Str(filepath)
    binary = str2bin(strAudio)
    newData = []

    if data.mode in ('RGBA'):
        datas = data.getdata()

    i = 0
    print('writing binary to image...')
    for pixel in datas:
        if (i < len(binary)):
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            sumof = red + green + blue
            binsec = 0
            if(sumof % 3 == 0):
                binsec = 1
            bit = binary[i]
            if (bit == '0' and binsec == 1):
                if(green > 250):
                    green = green - 1
                else:
                    green = green + 1
            elif (bit == '1' and binsec == 0):
                if(green > 250):
                    green = green - (sumof % 3)
                else:
                    green = green + (3 - sumof % 3)
            i += 1
            pixel = (red, green, blue, 255)
            newData.append(pixel)
        else:
            newData.append(pixel)

    data.putdata(newData)
    data.save("newfile.png", "PNG")
    return "Completed!"


def retr(filename):
    data = Image.open(filename).convert('RGBA')
    binary = ''
    if data.mode in ('RGBA'):
        datas = data.getdata()
    print('extracting audio from image...')
    for item in datas:
        pixel = item
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        sumof = red + green + blue
        if (sumof % 3 == 0):
            bit = 1
        else:
            bit = 0
        binary += str(bit)
        if (binary[-ksize:] == delimiter):
            binary = binary[:-ksize]
            break
    getStr2Audio(bin2str(binary))
    return 'done'


def Main():
    parser = optparse.OptionParser('usage %prog ' +
                                   '-e/-d <target file>')
    parser.add_option('-e', dest='hide', type='string',
                      help='target picture path to hide audio')
    parser.add_option('-d', dest='retr', type='string',
                      help='target picture path to retrieve audio')
    (options, args) = parser.parse_args()
    if (options.hide != None):
        filepath = raw_input("Enter path of audio file to hide: ")
        print(hide(options.hide, filepath))
    elif (options.retr != None):
        print(retr(options.retr))
    else:
        print(parser.usage)
        exit(0)


if __name__ == '__main__':
    Main()
