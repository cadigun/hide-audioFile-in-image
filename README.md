Submitted to CS 8821 by Christianah Adigun, Sagari Raju Vatchhavayi & Nisarg Thakur.

### Steganography: Hiding and subsequently Retrieving Audio Files in Image
Our algorithm is inspired by the DrapsTv tutorial on hiding text in an image using the Least Significant bit of each pixel. Ours is a little more complex.

## Getting Started
Please install python2, pip & pillow to avoid errors. Does not work with python3.

## How it Works
Our idea is that the RGB value of a pixel translates to yes or no to a simple question. Is the pixel RGB value divisible by 3? If the answer is yes, the bit of information that pixel represents is 1, and if no, it's 0. Until the expected padding/delimiter is found in the image, each pixel must provide a binary value. When this "encoded" binary is converted to hex, it's an audio file!

Some limitations: For best results, use an image file size that's at least 6x larger than audio file size. This tool works with any input audio file. However, the extracted file extension must be the same as input file extension. If your input file is '.mp3', ensure that you rename 'extracted' to 'extracted.mp3'. Happy information hiding!

## encoding
python ./main.py -e IMAGE_FILE

## decoding
python ./main.py -d IMAGE_FILE

## Example
```
python2 ./main.py -e sample-image.jpg
Enter path of audio file to hide: audio.mp3
```

```
python2 ./main.py -d newfile.png
```

Thanks to pixabay.com for the royalty free image!
