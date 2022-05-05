#!/usr/bin/env python3

import math
import os
import time
import random

from graphics import *


settings = {
    "frame_rate": 30,
    "bird_radius": 8,
    "fall_rate": 5,
    "fall_rate_default": 5,
    "rise_rate": 20,
    "rise_rate_default": 20,
    "forward_rate": 5,
    "forward_rate_default": 5,
    "forward_rate_max": 15,
    "column_spacing": 450,
    "column_spacing_min": 150,
    "column_spacing_max": 450,
    "column_gap": 800,
    "column_gap_min": 160,
    "column_gap_max": 800,
    "gap_center_min": 320,
    "gap_center_max": 660,
    "window_x": 1920,
    "window_y": 980,
    "bg_color": "black",
    "fg_color": "white",
    "button_height": 50,
    "button_width": 250,
    "button_spacing": 40,
    "text_spacing": 40,
    "demo_mode": False,
    "color_shift": 5,
    "debug_mode": True,
}

levels = [
    {"bg_color": "black", "fg_color": "white"},
    {"bg_color": "blue4", "fg_color": "white"},
    {"bg_color": "red4", "fg_color": "white"},
    {"bg_color": "green4", "fg_color": "white"},
    {"bg_color": "purple4", "fg_color": "white"},
    {"bg_color": "cyan4", "fg_color": "white"},
    {"bg_color": "firebrick4", "fg_color": "white"},
    {"bg_color": "cornsilk4", "fg_color": "white"},
    {"bg_color": "orange4", "fg_color": "white"},
    {"bg_color": "orchid4", "fg_color": "white"},
    {"bg_color": "sienna4", "fg_color": "white"},
]
    


def init():
    clear()
    print("Welcome!\n")
    
    
def clear():
    os.system("clear")
    
    
def main():
    ##
    win = GraphWin("Flappy",settings["window_x"],settings["window_y"],autoflush=False)
    win.setBackground(settings["bg_color"])
    ##
    ##    
    draw_title(win)
    draw_menu(win)
    ##
    ##
    win.close()
    
    
def view_settings(win):
    to_draw = []    
    to_draw,buttons = draw_settings(win,to_draw)
    
    ### 
    for item in to_draw:
        item.draw(win)
    #########
    ## Stuff what be done goes here yo ##    
    choice = "default"
    while choice != "":
        click = win.getMouse()
        clickX = click.getX()
        clickY = click.getY()
        choice = ""
        for button in buttons:
            if clickX >= button["x1"] and clickX <= button["x2"] and clickY >= button["y1"] and clickY <= button["y2"]:
                choice = button["name"]
                print("Clicked on {} button".format(choice))
                adjust_setting(win,choice,button)
                redraw(win,to_draw)
                #to_draw,buttons = draw_settings(win,to_draw)
                win.update()
        if choice == "":
            break

            
    #########
    for item in to_draw:
        item.undraw()
    ###
    
    
def draw_settings(win,to_draw):
    for item in to_draw:
        item.undraw()
    
    to_draw = []
    buttons = []
    
    centerX = int(settings["window_x"]/2)
    centerY = int(settings["window_y"]/2)
    
    leftcol_centerX = int(centerX / 2)
    rightcol_centerX = centerX + leftcol_centerX
    
    header_height = settings["button_height"] + settings["button_spacing"]*2
    total_button_height = settings["button_height"] + settings["button_spacing"]

    ### Max buttons per column is limited by window Y ###
    ### Total height of button is (button + button_spacing)*number_of_buttons + header_height ###
    max_buttons_per_column = int((settings["window_y"]-header_height)/total_button_height)
    
    print("{} settings: {} buttons per column".format(
        str(len(settings)),str(max_buttons_per_column)))
    
    if max_buttons_per_column < len(settings):
        columns = 2
        print("Two columns needed")
    else:
        columns = 1
        print("One column needed")
        
    title = Text(Point(centerX, settings["button_spacing"]), "SETTINGS")
    title.setTextColor(settings["fg_color"])
    title.setSize(24)
    title.setStyle("bold")
    to_draw.append(title)
    
    #### COUNT TITLE AS A BUTTON FOR SPACING PURPOSES ####
    buttons_made = 2
    column = 1
    
    for item in settings:
        button_name = item
        button_value = settings[item]
        button_string = ("{}: {}".format(button_name, button_value))
        
        if columns == 1:
            box_P1X = centerX - settings["button_width"]/2
            box_P1Y = (settings["button_height"]*buttons_made) + settings["button_spacing"]*buttons_made
            box_P2X = box_P1X + settings["button_width"]
            box_P2Y = box_P1Y + settings["button_height"]
        elif columns == 2:
            if buttons_made-2 >= max_buttons_per_column:
                column = 2
                if settings["debug_mode"]:
                    print("Column 2")
            else:
                column = 1
                if settings["debug_mode"]:
                    print("Column 1")
            if column == 1:
                box_P1X = (centerX - settings["button_width"]/2) - settings["button_width"]*2
                box_P1Y = (settings["button_height"]*buttons_made) + settings["button_spacing"]*buttons_made
                box_P2X = box_P1X + settings["button_width"]
                box_P2Y = box_P1Y + settings["button_height"]
            elif column == 2:
                box_P1X = (centerX - settings["button_width"]/2) + settings["button_width"]*2
                box_P1Y = (settings["button_height"]*(buttons_made - max_buttons_per_column)) + (settings["button_spacing"]*(buttons_made - max_buttons_per_column))
                box_P2X = box_P1X + settings["button_width"] 
                box_P2Y = box_P1Y + settings["button_height"]
                #print("{},{}  x  {},{}".format(
                #    str(box_P1X),str(box_P1Y),str(box_P2X),str(box_P2Y)))
        
        
        box_centerX = (box_P1X + box_P2X)/2
        box_centerY = (box_P1Y + box_P2Y)/2
        
        box = Rectangle(Point(box_P1X,box_P1Y),Point(box_P2X,box_P2Y))
        box.setFill(settings["bg_color"])
        box.setOutline(settings["fg_color"])
        box.setWidth(2)
        
        box_text = Text(Point(box_centerX,box_centerY),button_string)
        box_text.setTextColor(settings["fg_color"])
        
        buttons_made += 1
        if settings["debug_mode"]:
            print("Buttons made: "+str(buttons_made))
        
        buttons.append(
            {"name": button_name,
             "value": button_value,
             "x1": box_P1X,
             "y1": box_P1Y,
             "x2": box_P2X,
             "y2": box_P2Y,
             "box": box,
             "text": box_text,
            })
        
        to_draw.append(box)
        to_draw.append(box_text)
        
    return(to_draw,buttons)

    
def redraw(win,to_draw):
    for item in to_draw:
        item.undraw()
    win.update()
    for item in to_draw:
        try:
            item.setColor(settings["fg_color"])
        except:
            pass
        try:
            item.setTextColor(settings["fg_color"])
        except:
            pass
        item.setOutline(settings["fg_color"])
        item.draw(win)
    win.setBackground(settings["bg_color"])
    win.update()
    
    
def adjust_setting(win,setting_name,button):
    ### Draw a box with text, entry, and two buttons ("Accept", "Cancel") ###
    to_draw = []
    
    for setting in settings:
        if setting_name == setting:
            setting_value = settings[setting]
            if settings["debug_mode"]:
                print("Setting: "+str(setting))
                print("Setting value: "+str(setting_value))
    
    centerX = settings["window_x"]/2
    centerY = settings["window_y"]/2
    
    box_P1X = centerX - settings["button_width"]
    box_P2X = centerX + settings["button_width"]
    box_P1Y = centerY - settings["button_height"]*4
    box_P2Y = centerY + settings["button_height"]*4
    box_centerX = (box_P1X + box_P2X)/2
    box_centerY = (box_P1Y + box_P2Y)/2
    box_topY = box_P1Y
    
    box = Rectangle(Point(box_P1X,box_P1Y),Point(box_P2X,box_P2Y))
    box.setFill(settings["bg_color"])
    box.setOutline(settings["fg_color"])
    box.setWidth(3)
    to_draw.append(box)
    
    title = Text(
        Point(box_centerX,box_topY + settings["button_spacing"]),setting_name)
    title.setTextColor(settings["fg_color"])
    title.setSize(24)
    title.setStyle("bold")
    to_draw.append(title)
    
    value = Text(
        Point(box_centerX,box_topY + settings["button_spacing"]*2),str(setting_value))
    value.setTextColor(settings["fg_color"])
    value.setSize(18)
    to_draw.append(value)
    
    entry = Entry(Point(box_centerX,box_topY + settings["button_spacing"]*4),16)
    entry.setText(str(setting_value))
    entry.setTextColor("black")
    entry.setFill("white")
    to_draw.append(entry)
    
    
    for item in to_draw:
        item.draw(win)
        
    #####
    win.getMouse()
    new_value = entry.getText()
    
    entry.undraw()
    for setting in settings:
        if setting == setting_name:
            if new_value.isdigit():
                new_value = int(new_value)
            settings[setting] = new_value
            button["text"].setText(setting+": "+str(new_value))
            show_info_box(win,"New value set!\nRe-open settings for some values to take effect.")
    entry.draw(win)
    
    for item in to_draw:
        item.undraw()
    
    
def draw_title(win):
    text_title = "FLAPPY"
    text_border = "----------"
    text_bottom = "SlamJones 2022"
    
    to_draw = []
    
    midX = settings["window_x"]/2
    midY = settings["window_y"]/2
    
    rows = 3
    rowsY = calc_rowsY(win,rows)
    
    title = Text(Point(midX,rowsY[0]),text_title)
    title.setSize(36)
    border = Text(Point(midX,rowsY[1]),text_border)
    border.setSize(36)
    bottom = Text(Point(midX,rowsY[2]),text_bottom)
    border.setSize(24)
    
    to_draw.append(title)
    to_draw.append(border)
    to_draw.append(bottom)
    
    for item in to_draw:
        item.setTextColor(settings["fg_color"])
        item.setStyle("bold")
        item.draw(win)
    update()
    ####
        
    win.getMouse()
    ####
    for item in to_draw:
        item.undraw()
    win.update()
        
        
def draw_menu(win):
    text_title = "FLAPPY"
    button_names = ["Start","Demo","Settings","Quit"]
    buttons = []
    
    to_draw = []
    
    midX = settings["window_x"]/2
    rows = len(button_names)+1
    rowsY = calc_rowsY(win,rows)
    
    title = Text(Point(midX,rowsY[0]),text_title)
    title.setSize(36)
    title.setTextColor(settings["fg_color"])
    to_draw.append(title)
    
    count = 1
    for b in button_names:
        button_center_X = midX
        button_center_Y = rowsY[count]
        button_text = button_names[count-1]
        button_P1x = (
            (button_center_X-settings["button_width"]/2))
        button_P1y = (
            (button_center_Y-settings["button_height"]/2))
        button_P2x = (
            (button_center_X+settings["button_width"]/2))
        button_P2y = (
            (button_center_Y+settings["button_height"]/2))
        
        button_rect = Rectangle(Point(button_P1x,button_P1y),Point(button_P2x,button_P2y))
        button_rect.setFill(settings["bg_color"])
        button_rect.setOutline(settings["fg_color"])
        button_rect.setWidth(3)
        to_draw.append(button_rect)
        
        button_text = Text(Point(button_center_X,button_center_Y),button_text)
        button_text.setTextColor(settings["fg_color"])
        to_draw.append(button_text)
        buttons.append([button_rect,button_text.getText()])
        
        count += 1
    
    for item in to_draw:
        item.draw(win)
    win.update()
    ####
    choice = ""
    
    while choice != "Quit":
        choice = ""
        click = win.getMouse()
        click_x = click.getX()
        click_y = click.getY()

        for button in buttons:
            button_P1 = button[0].getP1()
            button_P2 = button[0].getP2()
            if click_x >= button_P1.getX() and click_x <= button_P2.getX() and click_y >= button_P1.getY() and click_y <= button_P2.getY():
                if settings["debug_mode"]:
                    print("Clicked on {}".format(button[1]))
                choice = button[1]
        if choice == "Start":
            for item in to_draw:
                item.undraw()
            win.update()
            ####
            draw_game(win)
            ####
            for item in to_draw:
                item.draw(win)
            win.update()
        elif choice == "Quit":
            break
        elif choice == "Demo":
            #settings["demo_mode"] = True
            #for item in to_draw:
            #    item.undraw()
            #win.update()
            show_info_box(win,"Demo not hooked up yet!")
            #draw_game(win)
            #for item in to_draw:
            #    item.draw(win)
            #win.update()
            #settings["demo_mode"] = False
        elif choice == "Settings":
            for item in to_draw:
                item.undraw()
            win.update()
            ####
            view_settings(win)
            ####
            for item in to_draw:
                item.draw(win)
            win.update()
        else:
            choice = ""
    
    
def draw_game(win):
    to_draw = []
    
    centerX = settings["window_x"]/2
    centerY = settings["window_y"]/2
    
    score = Text(Point(settings["window_x"]-100,100), "0")
    
    score.setTextColor("white")
    score.setSize(36)
    to_draw.append(score)
    
    for item in to_draw:
        item.draw(win)
    win.update()
    ####
    
    show_info_box(win,"Hit any key to continue")
    play_game(win,score)
    
    ####
    for item in to_draw:
        item.undraw()
    win.update()
    
    
def show_info_box(win,text):
    to_draw = []
    
    box_width = len(text) * 20
    
    if len(text) > 30:
        height = 2
    else:
        height = 1
    
    centerX = int(settings["window_x"]/2)
    centerY = int(settings["window_y"]/2)
    rect_P1X = centerX - box_width/2
    rect_P2X = centerX + box_width/2
    rect_P1Y = centerY - (settings["button_height"]/2)*height
    rect_P2Y = centerY + (settings["button_height"]/2)*height
    
    rect = Rectangle(Point(rect_P1X,rect_P1Y),Point(rect_P2X,rect_P2Y))
    rect.setFill(settings["bg_color"])
    rect.setOutline(settings["fg_color"])
    rect.setWidth(3)
    to_draw.append(rect)
    
    info_text = Text(Point(centerX,centerY),text)
    info_text.setTextColor(settings["fg_color"])
    info_text.setStyle("bold")
    info_text.setSize(20)
    to_draw.append(info_text)
    
    for item in to_draw:
        item.draw(win)
        
    key = ""
    click = None
    while key == "" and click == None:
        key = win.checkKey()
        click = win.checkMouse()
    time.sleep(1)
    
    for item in to_draw:
        item.undraw()
    
    
def play_game(win,score):
    play = True
    reset = False
    passing_column = False
    to_draw = []
    columns = []
    player_score = 0
    
    birdX = settings["window_x"]/2
    birdY = settings["window_y"]/2
    bird_move = [0,0]
    bird = Circle(Point(birdX,birdY),settings["bird_radius"])
    bird.setFill(settings["fg_color"])
    bird.setOutline(settings["fg_color"])
    to_draw.append(bird)
    
    for item in to_draw:
        item.draw(win)
    
    traveled = 0
    traveled_since_column = 0
    
    distance_to_next = settings["column_spacing"]
    
    points_since_color_shift = 0
    
    #####
    ##### START PLAY LOOP #####
    while play:
        traveled += settings["forward_rate"]
        traveled_since_column += settings["forward_rate"]
        
        if traveled_since_column >= distance_to_next:
            traveled_since_column = 0
            column = new_column(win,traveled)
            columns.append(column)
        
        for column in columns:
            column["x"] -= settings["forward_rate"]
            column["all"].move(-settings["forward_rate"],0)
            column["mid"].move(-settings["forward_rate"],0)
            if column["x"] <= 0:
                columns.remove(column)
                column["all"].undraw()
                column["mid"].undraw()
        
        key = win.checkKey()
        if key == "space":
            bird_move = [0,-settings["rise_rate"]]
        elif key == "Escape":
            play = False
            break
        else:
            bird_move = [0,settings["fall_rate"]]
        
        bird.move(bird_move[0],bird_move[1])
        update(settings["frame_rate"])
        
        ##### Check for collision #####
        if bird.getCenter().getY() >= settings["window_y"] or bird.getCenter().getY() <= 0:
            play = False
            show_info_box(win,"You crashed! Try again.")
            
        #### Step 1: Determine if bird is crossing a column ####
        #### #### Bird_left and bird_right? Check if column Y is between them?
        #### Step 2: Calculate whether bird is passing through gap or not ####
        #### #### Bird_top and bird_botton?  Check if both are within gap_top and gap_bottom
        bird_left = bird.getCenter().getX() - settings["bird_radius"]
        bird_right = bird.getCenter().getX() + settings["bird_radius"]
        bird_top = bird.getCenter().getY() - settings["bird_radius"]
        bird_bottom = bird.getCenter().getY() + settings["bird_radius"]
        print("bird_left: {}, bird_right: {}, bird_top: {}, bird_bottom: {}".format(
            str(bird_left),str(bird_right),str(bird_top),str(bird_bottom)))
        for column in columns:
            columnX = column["all"].getP1().getX()
            columnY = column["all"].getP1().getY()
            gap_top = column["mid"].getP1().getY()
            gap_bottom = column["mid"].getP2().getY()
            if columnX >= bird_left and columnX <= bird_right:
                if not column["passed"]:
                    column["passed"] = True
                    player_score += 1
                    points_since_color_shift += 1
                    if points_since_color_shift >= 5:
                        next_color(win)
                        points_since_color_shift = 0
                    score.setText(str(player_score))
                if settings["debug_mode"]:
                    print("Passing column: "+
                        "columnX: {},   columnY: {},    bird_left: {},   bird_right: {}".format(
                            str(columnX),str(columnY),str(bird_left),str(bird_right)))
                if gap_top > bird_top or gap_bottom < bird_bottom:
                    play = False
                    show_info_box(win,"You crashed! Try again.")
                    reset_settings()
    ##### END PLAY LOOP #####
    #####
            
    for item in columns:
        item["all"].undraw()
        item["mid"].undraw()

    for item in to_draw:
        item.undraw()
    win.update()    
        

def new_column(win,traveled):
    column_gap = random.randrange(settings["column_gap_min"],settings["column_gap_max"])/2
    gap_center = random.randrange(settings["gap_center_min"],settings["gap_center_max"])
    
    columnX = settings["window_x"]
    #gap_center = settings["window_y"]/2
    gap_P1Y = gap_center - int(column_gap/2)
    gap_P2Y = gap_center + int(column_gap/2)
    
    column_all = Line(Point(columnX,0),Point(columnX,settings["window_y"]))
    column_all.setFill(settings["fg_color"])
    column_all.setOutline(settings["fg_color"])
    column_all.setWidth(2)
    
    column_mid = Line(Point(columnX,gap_P1Y),Point(columnX,gap_P2Y))
    column_mid.setFill(settings["bg_color"])
    column_mid.setOutline(settings["bg_color"])
    column_mid.setWidth(2)
    
    column = {"x": columnX, "all": column_all, "mid": column_mid,}
    if settings["debug_mode"]:
        print("Spawned column: "+str(column))
    column["passed"] = False
    column["all"].draw(win)
    column["mid"].draw(win)
    
    return(column)


def reset_settings():
    settings["column_spacing"] = settings["column_spacing_max"]
    settings["forward_rate"] = settings["forward_rate_default"]
    settings["fall_rate"] = settings["fall_rate_default"]
    settings["rise_rate"] = settings["rise_rate_default"]

        
def next_color(win):
    new_settings = random.choice(levels)
    #settings["bg_color"] = new_settings["bg_color"]
    #settings["fg_color"] = new_settings["fg_color"]
    #win.setBackground(settings["bg_color"])
    if settings["forward_rate"] < settings["forward_rate_max"]:
        settings["forward_rate"] += 1
        settings["rise_rate"] += 1
        settings["fall_rate"] += 1
    if settings["column_spacing"] > settings["column_spacing_min"]:
        settings["column_spacing"] -= 2
    if settings["column_gap_max"] > settings["column_gap_min"]:
        settings["column_gap_max"] -= 2
        
    
def calc_rowsY(win,rows):
    rowsY = []
    for i in range(1,rows+1):
        new_y = i/(rows+1)
        #print("{} = int({}/({}+1))".format(
        #    str(new_y),str(i),str(rows)))
        rowsY.append(new_y*settings["window_y"])
    return(rowsY)
    
    
def farewell():
    print("\nFarewell!\n")
    if not settings["debug_mode"]:
        clear()


init()
main()
farewell()
