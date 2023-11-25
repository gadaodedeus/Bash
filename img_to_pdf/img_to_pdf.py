from PIL import Image
from pypdf import PdfMerger
import sys

def convert(img):
    '''Convert an RGBA image to an RGB image
    If the passed image has:
        img.mode == 'RGBA'
    then it will be converted to RGB.
    Else, the image itself will be returned.
        
    :PARAM: img - an object of type PIL.Image
    :RETURNS: img as RGBA
    '''
    if img.mode == 'RGBA':
        rgb = Image.new('RGB', img.size, (255,255,255)) 
        rgb.paste(img, mask=img.split()[3])
        return(rgb)
    else:
        return(img)
                           

inputArgs = sys.argv[1:]
def remove_duplicates(l):
    return list(set(l))
arguments=remove_duplicates(inputArgs)


inp = arguments
pdf = 0
for i in range(len(arguments)):
	if '.pdf' in arguments[i]:
		pdf=i
		break
out = arguments.pop(i)
print(inp)
print(out)

        
images = [Image.open(i) for i in inp]
images = [convert(i) for i in images]

images[0].save(out, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])




