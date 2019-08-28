from processing import *


class AnimatedSprite(object):

    def __init__(self, x, y, w, h, pics_folder, stepSize, scr_w, scr_h, speed=3):
        self.scr_w, self.scr_h = scr_w, scr_h
        self.x, self.y, self.w, self.h = x, y, w, h
        self.speed, self.rot_angle = speed, 0
        # sprite's states
        self.isMovingRight, self.isMovingLeft, self.isMovingUp, self.isMovingDown = False, False, False, False
        self.isFlying = True
        self.isFacingRight, self.isFacingLeft,self.isFacingUp,self.isFacingDown = True, False, False,False
        self.isMoving = False
        self.isUp, self.isDown, self.isFall, self.isHit = False, True, False, False
        self.isEval = False

        self.start_x, self.start_y = x, y
        self.speed = speed
        self.commands = []
        self.args = []


        # Final outcomes
        self.isWin, self.isLose = False, False
        
        # animation pics init
        # imageMode(CORNERS)
        # kadaR1 = loadImage(pics_folder + "green_flag.png")
        # kadaR2 = loadImage(pics_folder + "green_flag.png")
        # kadaR3 = loadImage(pics_folder + "green_flag.png")
        # kadaR4 = loadImage(pics_folder + "green_flag.png")

        # kadaL1 = loadImage(pics_folder + "green_flag.png")
        # kadaL2 = loadImage(pics_folder + "green_flag.png")
        # kadaL3 = loadImage(pics_folder + "green_flag.png")
        # kadaL4 = loadImage(pics_folder + "green_flag.png")

        # kadaU1 = loadImage(pics_folder + "green_flag.png")
        # kadaU2 = loadImage(pics_folder + "green_flag.png")
        # kadaU3 = loadImage(pics_folder + "green_flag.png")
        # kadaU4 = loadImage(pics_folder + "green_flag.png")

        # kadaD1 = loadImage(pics_folder + "green_flag.png")
        # kadaD2 = loadImage(pics_folder + "green_flag.png")
        # kadaD3 = loadImage(pics_folder + "green_flag.png")
        # kadaD4 = loadImage(pics_folder + "green_flag.png")

        # kada_air_L1 = loadImage(pics_folder + "green_flag.png")
        # kada_air_L2 = loadImage(pics_folder + "green_flag.png")

        # kada_air_R1 = loadImage(pics_folder + "green_flag.png")
        # kada_air_R2 = loadImage(pics_folder + "green_flag.png")
        
        imageMode(CENTER)
        kadaR1 = loadImage(pics_folder + "kadaR1.png")
        kadaR2 = loadImage(pics_folder + "kadaR2.png")
        kadaR3 = loadImage(pics_folder + "kadaR3.png")
        kadaR4 = loadImage(pics_folder + "kadaR4.png")

        kadaL1 = loadImage(pics_folder + "kadaL1.png")
        kadaL2 = loadImage(pics_folder + "kadaL2.png")
        kadaL3 = loadImage(pics_folder + "kadaL3.png")
        kadaL4 = loadImage(pics_folder + "kadaL4.png")

        kadaU1 = loadImage(pics_folder + "kadaU1.png")
        kadaU2 = loadImage(pics_folder + "kadaU2.png")
        kadaU3 = loadImage(pics_folder + "kadaU3.png")
        kadaU4 = loadImage(pics_folder + "kadaU4.png")

        kadaD1 = loadImage(pics_folder + "kadaD1.png")
        kadaD2 = loadImage(pics_folder + "kadaD2.png")
        kadaD3 = loadImage(pics_folder + "kadaD3.png")
        kadaD4 = loadImage(pics_folder + "kadaD4.png")

        # kada_air_L1 = loadImage(pics_folder + "kada_air_L1.png")
        # kada_air_L2 = loadImage(pics_folder + "kada_air_L2.png")
        #
        # kada_air_R1 = loadImage(pics_folder + "kada_air_R1.png")
        # kada_air_R2 = loadImage(pics_folder + "kada_air_R2.png")

        self.spritesR = [kadaR1, kadaR2, kadaR3, kadaR4]
        self.spritesL = [kadaL1, kadaL2, kadaL3, kadaL4]
        self.spritesU = [kadaU1, kadaU2, kadaU3, kadaU4]
        self.spritesD = [kadaD1, kadaD2, kadaD3, kadaD4]

        # self.kada_air_L = [kada_air_L1, kada_air_L2, kada_air_L1, kada_air_L2]
        # self.kada_air_R = [kada_air_R1, kada_air_R2, kada_air_R1, kada_air_R2]

        self.count = 0
        self.stepSize = stepSize
        image(self.spritesR[0], self.x, self.y, self.w, self.h)

    def forward(self, stepSize):
        self.commands.append("F")
        self.args.append(stepSize)

    def backward(self, stepSize):
        self.commands.append("B")
        self.args.append(stepSize)

    def penup(self):
        self.commands.append("U")
        self.args.append("")

    def pendown(self):
        self.commands.append("D")
        self.args.append("")

    def left(self,deg):
        self.commands.append("L")
        self.args.append(deg)

    def right(self,deg):
        self.commands.append("R")
        self.args.append(deg)

    def forwardT(self, stepSize):
        if self.isMoving == False:
            self.stepSize = stepSize
            self.isMoving = True
            self.start_x = self.x
        pass

    def backwardT(self, stepSize):
        if self.isMoving == False:
            self.stepSize = stepSize
            self.isMoving = True
            self.isMovingRight = False
            self.isFacingRight = False
            self.isMovingLeft = True
            self.isFacingLeft = True
            self.start_x = self.x

    def penupT(self):
        if self.isUp == False:
            self.isFlying = True
            self.isUp = True

    def pendownT(self):
        if self.isUp == True:
            self.isFlying = False
            self.isUp = False

    def leftT(self,deg):
        if self.isMoving == False:
            self.isMoving == True
            pass

    def rightT(self,deg):
        kada.turnRight(deg)

    def moveUp(self,stepSize):
        self.stepSize = stepSize
        if self.isMoving == False:
            self.isMoving = True
            self.isMovingLeft,self.isMovingRight = False,False
            self.isMovingUp,isMovingDown = True,False
            self.isFacingLeft, self.isFacingRight = False, False
            self.isFacingUp, self.isFacingDown = True, False
            self.start_y = self.y

    def moveDown(self,stepSize):
        self.stepSize = stepSize
        if self.isMoving == False:
            self.isMoving  = True
            self.isMovingLeft, self.isMovingRight = False, False
            self.isMovingUp, self.isMovingDown = False, True
            self.isFacingLeft, self.isFacingRight = False, False
            self.isFacingUp, self.isFacingDown = False, True
            self.start_y = self.y
        pass

    def moveLeft(self,stepSize):
        self.stepSize = stepSize
        if self.isMoving == False:
            self.isMoving = True
            self.isMovingLeft, self.isMovingRight = True, False
            self.isMovingUp, self.isMovingDown = False, False
            self.isFacingLeft, self.isFacingRight = True, False
            self.isFacingUp, self.isFacingDown = False, False
            self.start_x = self.x

    def moveRight(self,stepSize):
        self.stepSize = stepSize
        if self.isMoving == False:
            self.isMoving = True
            self.isMovingLeft, self.isMovingRight = False, True
            self.isMovingUp, self.isMovingDown = False, False
            self.isFacingLeft, self.isFacingRight = False, True
            self.isFacingUp, self.isFacingDown = False, False
            self.start_x = self.x


    def show(self, pics):
        image(pics[self.count], self.x, self.y, self.w, self.h)

    def show_init(self):
        image(self.spritesR[0], self.x, self.y, self.w, self.h)

    def game_cond(self, pics):
        if self.isLose:
            self.isMoving = False
            if self.y < self.scr_h:
                pushMatrix()
                translate(self.x, self.y)
                if self.isHit:
                    self.rot_angle += 1
                    self.y += 5
                    rotate(radians(self.rot_angle))
                    image(pics[self.count], 0, 0, self.w, self.h)
                if self.isFall:
                    self.x += 3
                    self.y += 5
                    self.rot_angle += 1
                    rotate(radians(self.rot_angle))
                    image(pics[self.count], 0, 0, self.w, self.h)
                popMatrix()
            else:
                fill(0)
                textSize(30)
                text("Please try again!", 350, 330)
                self.show(pics)
        elif self.isWin:
            self.isMoving = False
            self.speed = 0
            fill(255)
            textSize(30)
            text("You've got the Treasure!", 400, 330)
            self.show(pics)
        else:
            self.show(pics)

    def animationUpdate(self):
        self.count += 1
        if self.count >= len(self.spritesR):
            self.count = 0

    def locationUpdate(self):
        if self.isFacingLeft or self.isMovingLeft:
            self.game_cond(pics=self.spritesL)
        elif self.isFacingRight or self.isMovingRight:
            self.game_cond(pics=self.spritesR)
        elif self.isFacingUp or self.isMovingUp:
            self.game_cond(pics=self.spritesU)
        elif self.isFacingDown or self.isMovingDown:
            self.game_cond(pics=self.spritesD)
        # if self.isMovingUp:
        #     if self.isFlying:
        #         if self.isFacingLeft:
        #             self.game_cond(pics=self.kada_air_L)
        #         elif self.isFacingRight:
        #             self.game_cond(pics=self.kada_air_R)
        #     else:
        #         if self.isFacingLeft:
        #             self.game_cond(pics=self.spritesL)
        #         elif self.isFacingRight:
        #             self.game_cond(pics=self.spritesR)
        #         elif self.isFacingUp:
        #             self.game_cond(pics=self.spritesU)
        #         elif self.isFacingDown:
        #             self.game_cond(pics=self.spritesD)
        # if self.isMovingDown:
        #     if self.isFlying:
        #         if self.isFacingLeft:
        #             self.game_cond(pics=self.kada_air_L)
        #         elif self.isFacingRight:
        #             self.game_cond(pics=self.kada_air_R)
        #     else:
        #         if self.isFacingLeft:
        #             self.game_cond(pics=self.spritesL)
        #         elif self.isFacingRight:
        #             self.game_cond(pics=self.spritesR)
        # if self.isMovingLeft or self.isFacingLeft:
        #     if self.isFlying:
        #         self.game_cond(pics=self.kada_air_L)
        #         self.isFacingLeft, self.isFacingRight = True, False
        #     else:
        #         self.game_cond(pics=self.spritesL)
        #         self.isFacingLeft, self.isFacingRight = True, False
        # if self.isMovingRight or self.isFacingRight:
        #     if self.isFlying:
        #         self.game_cond(pics=self.kada_air_R)
        #         self.isFacingLeft, self.isFacingRight = False, True
        #     else:
        #         self.game_cond(pics=self.spritesR)
        #         self.isFacingLeft, self.isFacingRight = False, True
