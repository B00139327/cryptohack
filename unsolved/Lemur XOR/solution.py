from PIL import Image
def loadImage(filename):
    img = Image.open(filename)
    width, height = img.size
    img = img.convert("RGB")
    pixel = img.load()
    return width, height, pixel
def combineImage(file1, file2):
    w1, h1, p1 = loadImage(flag_7ae18c704272532658c10b5faad06d74.png)
    w2, h2, p2 = loadImage(lemur_ed66878c338e662d3473f0d98eedbd0d.png)
    width = min(w1, w2)
    height = min(h1, h2)
    img = Image.new("RGB", (width, height))
    pix = img.load()
    for y in xrange(0, height):
        for x in xrange(0, width):
            r1, g1, b1 = p1[x, y]
            r2, g2, b2 = p2[x, y]
            pix[x, y] = r1^r2, g1^g2, b1^b2

img.save(file3)
if __name__ == "__main__" :
    combineImage("pic1.jpg", "pic2.jpg")
