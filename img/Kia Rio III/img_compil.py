from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import glob
import os

size = 128, 128



for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    img = Image.open(infile)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(file + "F.jpg", "JPEG")
#    width = 400
#    height = 250
#    im = im.resize((width, height), Image.ANTIALIAS)  # best down-sizing filter
#    im1 = im.filter(ImageFilter.GaussianBlur(radius=1))
#    im1 = im.filter(ImageFilter.MaxFilter(size=3))
#    out = im.convert("P", palette=Image.ADAPTIVE, colors=256)
#    im.ImageEnhance.Contrast(im)
    enhancer = ImageEnhance.Brightness(im)
    enhanced = enhancer.enhance(0.5)
    enhancer = ImageEnhance.Contrast(enhanced)
    enhanced = enhancer.enhance(1.1)
    enhancer = ImageEnhance.Sharpness(enhanced)
    enhanced = enhancer.enhance(1.5)
    enhanced.save(file + "B.jpg", "JPEG")

    enhancer = ImageEnhance.Brightness(img)
    enhanced = enhancer.enhance(0.5)
    enhancer = ImageEnhance.Contrast(enhanced)
    enhanced = enhancer.enhance(1.1)
    enhancer = ImageEnhance.Sharpness(enhanced)
    enhanced = enhancer.enhance(1.5)
    enhanced.save(file + "FB.jpg", "JPEG")

#    enhanced.show()
#    out.show()

    enhancer = ImageEnhance.Brightness(im)
    enhanced = enhancer.enhance(1.5)
    enhancer = ImageEnhance.Contrast(enhanced)
    enhanced = enhancer.enhance(1.1)
    enhancer = ImageEnhance.Sharpness(enhanced)
    enhanced = enhancer.enhance(1.5)
    enhanced.save(file + "W.jpg", "JPEG")

    enhancer = ImageEnhance.Brightness(img)
    enhanced = enhancer.enhance(1.5)
    enhancer = ImageEnhance.Contrast(enhanced)
    enhanced = enhancer.enhance(1.1)
    enhancer = ImageEnhance.Sharpness(enhanced)
    enhanced = enhancer.enhance(1.5)
    enhanced.save(file + "FW.jpg", "JPEG")
#    im.save(file + ".jpg", "JPEG")
