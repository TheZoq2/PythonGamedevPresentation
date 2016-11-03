#Slide 1:

Introduction

#Components of a game

What components do you need to make a game?

Graphics, Something to look at. text based, 2d, 3d

Input Need to interract

Sound, often forgotten

Other?


#Library choise:

In order to draw graphics using python (or any other language), you need to use an external library. 
Unfortunley, when it comes to python, there is a lack of good graphics libraries. 

Pygame is widely suggested. I will show it today

PySFML is unmaintained :(

PySDL2, I will show alternative code for sdl2

Others like cocos2d and panda3d


#Getting started with SDL

Install using pip. Package manager on linux, woodoo on windows

`pip3 install pygame`

`import pygame`

Show that it runs


#The downside of SDL



#The game loop
Most games have a loop that looks something like this. Some libraries, like cocos2d that I mentioned earlier
hide this loop. But in SDL, we have to write it ourselves so let's do that. Since we have no gameplay
and nothing to draw yet, we will just write the `present_to_window` and `handle_user_input` functions.


Let's start out by creating a variable `running` which is set to true, and add a while loop that runs
while the `running` variable is true. This allows us to exit the game when it's done. Let's run the game
again. The window is there, but it's transparent and if I use the key combination I have set up for closing
windows, nothing happens. I need to go to the terminal that started the program and press ctrl-c.

The first issue is easy to fix, we need to tell our renderer to present what it has drawn so far to the 
screen. This is done using `renderer.present()`.

The second issue is a bit more tricky to fix. Most game engines use something called events. Each time 
something from the outside happens, like keyboard input or the game getting a close window signal, that
'event' is added to a list of things that have happned. When we are ready to deal with those events in
our game, we will write the following code.

As you can see, when we run the program this time, we can use my keyboard shortcut for closing windows and 
the program exits. We will get back to this event loop later on


#Drawing something on the screen
Now that we have a window set up, we will want to draw something on it. Most of the time you will want to
draw an image. Images when drawn by game engines are usually known as `sprites`. Some engines separate the
actual image from the sprite, but that's not the case in sdl. 

The renderer object contains a function called `load_sprite` that takes an image from a folder called
`resources`, loads it into memory and prepares it for drawing. The function returns an image 'variable' 
which you need to keep track of. 

In the `resources` folder, I have an ugly image called `ghost.png` which we want to draw. To do that,
we first call `sprite = renderer.load("ghost.png")`. Then in our main loop, before we run `renderer.present()`,
we call `renderer.draw_sprite(sprite)`.  When we run the program, we get a small ghost in the upper left of
the image. 

We can make the image bigger by using `sprite.scale` and we can change the location of it using 
`sprite.position`. 

THere, with those changes it's much better.


We can also rotate sprites using sprite.angle


#A quick look at classes
Those of you who are on the first year of the D and U programmes will not come across propper object orientation
until this spring but OOP contains one really usefull concept, classes.

In its simplest form, a class is simply a collection of data and functions to perform on that data. We will
ignore the functions for now and just focus on the data. 

In order to create a class, we use the class keyword

