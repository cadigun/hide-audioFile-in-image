#======================================================================#

Christianah Adigun, Sagari Raju Vatchhavayi, Nisarg Thakur
Steganography: Hiding and subsequently Retrieving Audio Files in Image
#======================================================================#

Our algorithm is inspired by the DrapsTv tutorial on hiding text in an image using the Least Significant bit of each pixel. Ours is a little more complicated.

How it Works
-------------------
For each pixel in the image, it gets the RGB sum and gets its modulo division of 3. It uses this information to determine whether it needs to modify the green value.
The only limitation in our algorithm is that the embedded audio file size cannot exceed half the size of the image to be used. 

For Linux Users:
To encode, use the commands
python ./main.py -e IMAGE_FILE


To decode, use the commands
python ./main.py -d IMAGE_FILE