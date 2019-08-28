from spriteAnimated import AnimatedSprite
from sprite import Sprite
from Button import Button

def setup():
    global scr_w,scr_h,offset
    global bgimg,isOnPlayBtn,isBtnShown

    global user_ctrl_up_btn,user_ctrl_down_btn,user_ctrl_left_btn,user_ctrl_right_btn
    global user_ctrl_penup_btn,user_ctrl_pendown_btn

    global isShowAxis,x_axis,y_axis
    global kada,frameR
    global text_x,text_y
    global reset_btn,start_btn
    global attr_reset_btn,attr_start_btn,attr_kada
    
    size(750,620)
    frameR = 60
    frameRate(frameR)
    scr_w,scr_h = 650,650
    offset = 50
    stepSize = -3
    isBtnShown = True

    attr_kada = {"x":scr_w/2-50,"y":scr_h/2-60,"w":20,"h":35,
                 "speed":3+int((1.5*(60-frameR)/10))}
    attr_reset_btn = {"x": 645, "y": 200, "w_s": 60, "h_s": 60,"w_l":80,"h_l":80}
    attr_start_btn = {"x": 645, "y": 300, "w_s": 80, "h_s": 80,"w_l":100,"h_l":100}
    attr_user_ctrl_up_btn = {"x": scr_w-10, "y": scr_h-210, "w_s": 60, "h_s": 50,"w_l":80,"h_l":70}
    attr_user_ctrl_down_btn = {"x": scr_w-8, "y": scr_h-90, "w_s": 60, "h_s": 50,"w_l":80,"h_l":70}
    attr_user_ctrl_left_btn = {"x": scr_w-70, "y": scr_h-150, "w_s": 60, "h_s": 50,"w_l":80,"h_l":70}
    attr_user_ctrl_right_btn = {"x": scr_w+50, "y": scr_h-150,"w_s": 60, "h_s": 50,"w_l":80,"h_l":70}
    attr_user_ctrl_penup_btn = {"x": 580, "y": 380, "w_s": 60, "h_s": 50,"w_l":80,"h_l":70}
    attr_user_ctrl_pendown_btn = {"x": 700, "y": 380, "w_s": 60, "h_s": 50,"w_l":80,"h_l":70}

    imageMode(CENTER)
    #four ctrl buttons
    user_ctrl_up_btn = Button(attr=attr_user_ctrl_up_btn,
                            imgs={"large":"./resources/user_ctrl_up.png",
                                  "small":"./resources/user_ctrl_up.png"})
    user_ctrl_down_btn = Button(attr=attr_user_ctrl_down_btn,
                            imgs={"large":"./resources/user_ctrl_down.png",
                                  "small":"./resources/user_ctrl_down.png"})
    user_ctrl_left_btn = Button(attr=attr_user_ctrl_left_btn,
                            imgs={"large":"./resources/user_ctrl_left.png",
                                  "small":"./resources/user_ctrl_left.png"})
    user_ctrl_right_btn = Button(attr=attr_user_ctrl_right_btn,
                            imgs={"large":"./resources/user_ctrl_right.png",
                                  "small":"./resources/user_ctrl_right.png"})
    user_ctrl_penup_btn = Button(attr=attr_user_ctrl_penup_btn,
                            imgs={"large":"./resources/penup_btn.png",
                                  "small":"./resources/penup_btn.png"})
    user_ctrl_pendown_btn = Button(attr=attr_user_ctrl_pendown_btn,
                            imgs={"large":"./resources/pendown_btn.png",
                                  "small":"./resources/pendown_btn.png"})
    #start and reset btn
    reset_btn = Button(attr=attr_reset_btn,
                       imgs={"large": "./resources/reset_btn.png",
                             "small": "./resources/reset_btn.png"})
    start_btn = Button(attr=attr_start_btn,
                       imgs={"large": "./resources/start_btn.png",
                             "small": "./resources/start_btn.png"})
    #coord's axis
    x_axis = loadImage("./resources/x_axis.png")
    x_axis.resize(540,15)
    y_axis = loadImage('./resources/y_axis.png')
    y_axis.resize(15,530)

    #load sprite
    kada = AnimatedSprite(x=attr_kada["x"], y=attr_kada["y"],
                          w=attr_kada["w"], h=attr_kada["h"],
                          pics_folder="./resources/kada_walks/", stepSize=stepSize,
                          scr_w=scr_w, scr_h=scr_h, speed=attr_kada["speed"])

    #$start0
    kada.forward(50)
    kada.backward(50)
    #$end0
    
def draw():
    global scr_w,scr_h,offset
    global bgimg,isOnPlayBtn,isBtnShown
    global isShowAxis,x_axis,y_axis
    global kada,frameR
    global text_x,text_y
    global reset_btn,start_btn
    global attr_reset_btn,attr_start_btn
    global user_ctrl_up_btn,user_ctrl_down_btn,user_ctrl_left_btn,user_ctrl_right_btn
    global user_ctrl_penup_btn, user_ctrl_pendown_btn

    # run multiple lines
    if kada.isMoving == False and start_btn.isReleased:
        if len(kada.commands) > 0:
            command,arg = kada.commands.pop(0),kada.args.pop(0)
            if command == "F":
                kada.forwardT(arg)
            if command == "B":
                kada.backwardT(arg)
            if command == "U":
                kada.penupT()
            if command == "D":
                kada.pendownT()
            if command == "L":
                kada.left(arg)
            if command == "R":
                kada.right(arg)


    #--elements to show---
    background(200)
    draw_grid(scr_w-100,scr_h-100,offset=offset,num_lines=10)
    #user_ctrls
    user_ctrl_up_btn.show()
    user_ctrl_down_btn.show()
    user_ctrl_left_btn.show()
    user_ctrl_right_btn.show()
    user_ctrl_penup_btn.show()
    user_ctrl_pendown_btn.show()
    #start & reset btns
    reset_btn.show()
    start_btn.show()
    showMouseXY(scr_w-100,scr_h-100,coord_type=0) # 0 for traditional coord; 1 for processing coord
    image(x_axis,scr_w/2-30,scr_h/2-50)
    image(y_axis,scr_w/2-50,scr_h/2-65)
    move_kada(kada=kada,frameR=frameR)
    show_components(isResetBtn=True,isStartBtn=True,
                    isCoordRegion=True,
                    kada=kada,scr_w=scr_w,scr_h=scr_h)
    pass

def showMouseXY(scr_w,scr_h,coord_type=0):# display the current cord of X and Y
    fill(0)
    rectMode(CENTER)
    rect(mouseX,mouseY,5,5)
    point(mouseX,mouseY)
    if coord_type == 0: #origin at the center of the screen
        fill(0)
        textSize(15)
        text("x:"+str(mouseX-scr_w/2),mouseX+15,mouseY)
        text("y:"+str(scr_h/2-mouseY),mouseX+60,mouseY)
    else: # processing's default coord-sys
        fill(0)
        textSize(15)
        text("x:" + str(mouseX), mouseX+15, mouseY)
        text("y:" + str(mouseY), mouseX+60, mouseY)

def draw_grid(scr_w,scr_h,num_lines=20,colors=["yellow","grey"],offset=50):
    offset /= 2
    #draw lines
    for i in range(num_lines+1):
        fill(0)
        stroke(0,100) 
        line(offset+i*(scr_w-offset*2)//num_lines , offset,
             offset+i*(scr_w-offset*2)//num_lines, scr_h-offset)
        line(offset, offset+i*(scr_w-offset*2)//num_lines,
             scr_w-offset, offset+i*(scr_w-offset*2)//num_lines)

    #TODO:color regions
    # fill(0,0,0,100)

def show_components(isResetBtn,isStartBtn,isCoordRegion, kada,scr_w,scr_h):
    text_left_x = 540
    if isResetBtn:
        pass
    if isStartBtn:
        pass

    if isCoordRegion:
        #label-坐标
        ref_y = 100
        fill(0)
        Chinese = createFont("LiSu", 20)
        textFont(Chinese)
        text(u"位置",text_left_x,ref_y-40)
        text(u"坐标",text_left_x,ref_y)
        #data
        show_data_xy(kada,scr_w,scr_h,ref_y)


    pass

def move_kada(kada,frameR):
    # kada animation
    kada.locationUpdate()
    if frameCount % (frameR//7) == 0:
        kada.animationUpdate()
    if kada.isMoving:
        if kada.isMovingLeft:
            kada.x -= kada.speed
            if abs(kada.x - kada.start_x) >= kada.stepSize:
                kada.isMovingLeft = False
                kada.isMoving = False
                kada.x = kada.start_x - kada.stepSize
                kada.start_x = kada.x
        elif kada.isMovingRight:
            kada.x += kada.speed
            if abs(kada.x - kada.start_x) >= kada.stepSize:
                kada.isMovingRight = False
                kada.isMoving = False
                kada.x = kada.start_x + kada.stepSize
                kada.start_x = kada.x
        if kada.isMovingUp:
            kada.y -= kada.speed
            if abs(kada.y - kada.start_y) >= kada.stepSize:
                kada.isMovingUp = False
                kada.isMoving = False
                kada.y = kada.start_y - kada.stepSize
                kada.start_y = kada.y
        elif kada.isMovingDown:
            kada.y += kada.speed
            if abs(kada.y - kada.start_y) >= kada.stepSize:
                kada.isMovingDown = False
                kada.isMoving = False
                kada.y = kada.start_y + kada.stepSize
                kada.start_y = kada.y

def show_data_xy(kada,scr_w,scr_h,ref_y):
    kada_x,kada_y = show_kada_xy(kada,scr_w,scr_h,ref_y)
    text_x,text_y = "",""
    if kada_x < 0:
        text_x = u"左"
    if kada_x > 0:
        text_x = u"右"
    if kada_y > 0:
        text_y = u"上"
    if kada_y < 0:
        text_y = u"下"
    text( "(" + text_x + str(abs(kada_x)) + ","
          + text_y + str(abs(kada_y))+ ")" , scr_w-65,ref_y-40)

def show_kada_xy(kada,scr_w,scr_h,ref_y):
    kada_x = kada.x-(scr_w/2-50)
    kada_y = (scr_h/2-60)-kada.y
    fill(0)
    textSize(20)
    text("(" + str(kada_x) + ","+str(kada_y)+")",scr_w-65,ref_y)
    return kada_x,kada_y

# **inner event func of processing***
# when the mouse is clicked on the "Play"、"Reset" and 4 directional btns
def mouseReleased():
    global user_ctrl_up_btn,user_ctrl_down_btn,user_ctrl_left_btn,user_ctrl_right_btn
    global user_ctrl_penup_btn,user_ctrl_pendown_btn
    global reset_btn,start_btn
    if mouseButton == LEFT:
        if user_ctrl_up_btn.isLarge:
            kada.moveUp(50)
        if user_ctrl_down_btn.isLarge:
            kada.moveDown(50)
        if user_ctrl_left_btn.isLarge:
            kada.moveLeft(50)
        if user_ctrl_right_btn.isLarge:
            kada.moveRight(50)
        if user_ctrl_penup_btn.isLarge:
            kada.isFlying = True
        if user_ctrl_pendown_btn.isLarge:
            kada.isFlying = False
        if reset_btn.isLarge:
            kada.x,kada.y = scr_w/2-50,scr_h/2-60
            pass

        if start_btn.isLarge:
            start_btn.isReleased = True
        else:
            start_btn.isReleased = False
