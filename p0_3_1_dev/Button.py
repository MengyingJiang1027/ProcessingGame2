class Button(object):

    def __init__(self,attr,imgs=[],):
        self.imageMode = CENTER
        self.x = attr["x"]
        self.y = attr["y"]
        self.w_s,self.h_s = attr["w_s"],attr["h_s"]
        self.w_l,self.h_l = attr["w_l"],attr["h_l"]
        self.large_btn,self.isLarge = loadImage(imgs["large"]),False
        # self.w_l,self.h_l = self.large_btn.width,self.large_btn.height

        self.small_btn,self.isSmall = loadImage(imgs["small"]),True
        # self.w_s,self.h_s = self.small_btn.width,self.small_btn.height
        self.isReleased = False

    def show(self):
        # print(self.isSmall)
        if (mouseX in range(self.x-self.w_s/2,self.x+self.w_s/2)) and \
                (mouseY in range(self.y-self.w_s/2,self.y+self.w_s/2)):
            self.small_btn.resize(self.w_l,self.h_l)
            image(self.small_btn,self.x,self.y)
            self.isLarge = True
            self.isSmall = False

        else:
            self.large_btn.resize(self.w_s, self.h_s)
            image(self.large_btn,self.x,self.y)
            self.isLarge = False
            self.isSmall = True
