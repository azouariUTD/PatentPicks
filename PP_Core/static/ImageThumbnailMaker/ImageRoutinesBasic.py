import os, sys
from PIL import Image

sizeForThumbnail =( 250,250 )
for imgFile in sys.argv[1:]:
	
	outFile = os.path.splitext(imgFile)[0] + ".thumbnail" + ".jpg"
	if imgFile != outFile:
		try:
			im = Image.open(imgFile)
			im.thumbnail(sizeForThumbnail)
			im.save(outFile,"JPEG")
		except IOError:
			print('cannot create thumbnail for', imgFile)














