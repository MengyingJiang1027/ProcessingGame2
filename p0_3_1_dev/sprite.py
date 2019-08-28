class Sprite(object):

    def __init__(self,x,y,w,h,pic):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # pdb.set_trace()
        self.sprite = loadImage(pic)
        self.sprite.resize(w,h)
        image(self.sprite,self.x,self.y)

        # self.sprite_open = loadI

    def show(self):
        image(self.sprite,self.x,self.y)

    #---specifically for chests---#
    def open(self):
        pass
