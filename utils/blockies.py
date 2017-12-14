# This is based on https://github.com/ethereum/blockies , 
# and is a python library for generating blocky identicons from 
# Etherem addresses
# Requires Python3

import math, io, random, colorsys

def wrap(n):
    # Behave like javascript integers
    n = n & 0xffffffff

    if n > 0x7fffffff:
        n = n & 0x7fffffff
        n -= 0x80000000

    return n

class Blocky():
    def __init__(self):
        self.randseed = [0,0,0,0]

    def seedrand(self,seed):
        rs  = [0,0,0,0]     
        
        for i in range(0,len(seed)):
            rs[ i % 4 ] = wrap(wrap( rs [ i % 4 ] << 5) - rs[i % 4] + ord(seed[i]))

        self.randseed = rs

    def rand(self): 
        rs = self.randseed

        t = rs[0] ^ (wrap(rs[0] << 11))
        rs[0] = rs[1]
        rs[1] = rs[2]
        rs[2] = rs[3]
        rs[3] = (rs[3] ^ (rs[3] >> 19) ^ t ^ (t >> 8))        
        self.randseed = rs
        return rs[3] / 0x80000000 


    def createColor(self):
        # hue (whole spectrum)
        h = self.rand()
        # saturation [40,100], avoids greyish colors
        s = self.rand() * 0.6  + 0.4
        # lightness
        # can be anything from 0 to 100, but probabilities are a bell curve around 50%
        l = (self.rand()+self.rand()+self.rand()+self.rand()) / 4

        (r,g,b) = colorsys.hls_to_rgb(h,l,s)

        return (int(r*0xFF),int(g*0xFF),int(b*0xFF))

    def createImageData(self,width):

        dataW = math.ceil( width / 2 )
        mirrorW = width - dataW

        data = []
        for y in range(0,width): 
            row = [math.floor( self.rand() * 2.3) for x in range(0, dataW)]
            data.extend(row)
            r = row[0:mirrorW]
            r.reverse()
            data.extend(r)

        return data

    def buildOpts(self,opts = {}):

        if 'seed' in opts:
            s = opts['seed']
        else :
            s = "{:x}".format(random.randint(0,10e16))

        self.seedrand(s)

        def get(key, default):
            if key in opts:
                return opts[key]
            return default()

        return {
            'size' : get('size', lambda: 8),
            'scale' : get('scale', lambda: 16),
            'color' : get('color', lambda: self.createColor()),
            'bgcolor' : get('bgcolor', lambda: self.createColor()),
            'spotcolor' : get('spotcolor', lambda: self.createColor())
        }

    def renderIcon(self, opts):
        import PIL.Image, PIL.ImageDraw

        imgdata = self.createImageData(opts['size'])        
        w = math.sqrt(len(imgdata))
        scale = opts['scale']
        cWidth = opts['size'] * scale
        
        img = PIL.Image.new("RGB", (cWidth, cWidth),opts['bgcolor'])
        canvas = PIL.ImageDraw.Draw(img)

        for  i in range (0, len(imgdata)):
            row = math.floor( i / w )
            col = i % w
            if imgdata[i] == 0:
                continue

            fillstyle = opts['color']
            if imgdata[i] == 2:
                fillstyle = opts['spotcolor']

            (x0,y0) = (col*scale , row * scale)
            canvas.rectangle((x0,y0,x0+scale,y0+scale), fillstyle)

        return img

        # python imaging special

    def createIcon(self, opts = {}):
        opts = self.buildOpts(opts)
        return self.renderIcon(opts)
        
def getIconPNG(seed, size=8, scale=8):
    data = io.BytesIO()
    img = Blocky().createIcon({'seed':seed, 'size':size, 'scale':scale})
    img.save(data,"png")
    return data.getvalue() 


def main():

    generator = Blocky()
#    generator.seedrand("1cb7fef7c4e55")
    img = generator.createIcon({
        'seed': "0xAB6916095ca1df60bb79ce92ce3ea74c37c5d359",
        'size': 8, 
        'scale': 16,
        })
    img.show()
    
    data = io.BytesIO()
    img.save(data,"png")
    print("data", data.getvalue())

if __name__ == '__main__':
    main()