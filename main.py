from turtle import width
import pyautogui as gui;
WIDTH, HEIGHT = gui.size(); #X Y
print(WIDTH, HEIGHT);
while True:
    width, height = gui.position();
    if(width == WIDTH-1):
        gui.moveTo(0, height);
    if(width == 0):
        gui.moveTo(WIDTH, height);
    if(height == HEIGHT-1):
        gui.moveTo(width, 0);

    if(height == 0):
        gui.moveTo(width, HEIGHT);


    
