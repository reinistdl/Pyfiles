import urllib2
from PIL import Image
for x in range(1, 5100):
	y = 0
	try:
		html = Image.open(urllib2.urlopen('http://gign.lv/upload/pictures/large/image_'+ str(x) +'.jpg'))
		html.save('/Users/reinis/Desktop/pictures/test'+ str(x) +'.jpg')
	except urllib2.HTTPError:
		print 'File image_' + str(x) + '.jpg does not EXIST on Server.'
		y=1
	if y==0:
		print '/Users/reinis/Desktop/pictures/test'+ str(x) +'.jpg' + ' SAVED'
