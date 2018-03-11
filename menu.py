import os
import sys
from PIL import Image
def open_photo(menu):
	img=Image.open(menu)
	img.show()
open_photo(sys.argv[1]+".jpg")