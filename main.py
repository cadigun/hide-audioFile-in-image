#!/usr/bin/env python
from PIL import Image
import binascii, optparse

def getAudio2Str(filename):
    audioArray = []
    message = ''
    audio = open(filename, 'rb')
    with audio as f:
        for line in f.readlines():
            audioArray.append(str(line))
    for i in range(0, len(audioArray)):
        message += audioArray[i]
    return message


def getStr2Audio(message):
    with open('extracted.wav', 'wb') as file:
        file.write(message)

def str2bin(message):

    binary = ''.join(format(ord(x), 'b').zfill(8) for x in message)
    return binary+'111111001111111'

def bin2str(binary):
    message = ''
    for i in range(0, len(binary), 8):
        message += chr(int(binary[i:i+8],2))
    return message

def hide(filename, filepath):
    data = Image.open(filename).convert('RGBA')
    strAudio = getAudio2Str(filepath)
    binary = str2bin(strAudio)
    print len(binary)
    newData = []
    i = 0
    if data.mode in ('RGBA'):
        datas = data.getdata()

    for item in datas:
	pixel = item
        if (i < len(binary)):
		red   = pixel[0]
            	green = pixel[1]
            	blue  = pixel[2]
            	sumof = red + green + blue
            	if(sumof % 3 == 0):
                	isOne = 1
            	else:
                	isOne = 0
            	bit = binary[i]
            	if (bit == '0' and isOne == 1):
                	if(green > 250):
				green = green - 1
			else:
				green = green + 1
            	elif (bit == '1' and isOne == 0):
                	if(green > 250):
				green = green - (sumof%3)
			else:
				green = green + (3 - sumof%3)
            	else:
                	pass
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
    	for item in datas:
        	pixel = item
        	red   = pixel[0]
        	green = pixel[1]
        	blue  = pixel[2]
        	sumof = red + green + blue
        	if (sumof % 3 == 0):
                	bit = 1
        	else:
                	bit = 0
        	binary += str(bit)
        	if (binary[-17:] == '11111110011111111'):
                	binary = binary[:-17]
			print len(binary)
                	break
	return getStr2Audio(bin2str(binary))

def Main():
    parser = optparse.OptionParser('usage %prog '+\
    	'-e/-d <target file>')
    parser.add_option('-e', dest='hide', type='string', \
    	help='target picture path to hide audio')
    parser.add_option('-d', dest='retr', type='string', \
                      help='target picture path to retrieve audio')
    (options, args) = parser.parse_args()
    if (options.hide != None):
        filepath = raw_input("Enter path of audio file to hide: ")
        print hide(options.hide, filepath)
    elif (options.retr != None):
        print retr(options.retr)
    else:
        print parser.usage
        exit(0)

if __name__ == '__main__':
    Main()
