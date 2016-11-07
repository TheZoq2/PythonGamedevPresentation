#Slide 1:

Welcome to my presentation on making games in python. My name is Frans, I study the third year in the
D programme and have been making games during my spare time for a couple of years. I have been
to most of the gamejams since I started here and I have used python for nearly all of them.

I am also a lab assistant in the introductory python course so some of you might recognise me. 

The goal for today is to show you how to make a game in python and give you enough knowledge to go 
to the gamejam on friday and be able to make a decent game. The idea is that I will give a ~1 hour 
presentation on the basics of python game dev followed by a "workshop" where you can try these
things out and ask questions if they come up. 

#Components of a game

What components go into making a game?

The most important thing is probably input, the players need to be able to interract with and affect
the game. If they can't, it will be more of a movie or a book.

Input could be anything from regular keyboard input to things like motion controls. Of course, standard
things like keyboard, mouse and joystick input is the easiest and what I will focus on today. 

Once you have a way of interracting with the game, the game needs to have a way to relay information back to
the player. Usually this is done with some sort of visual graphics but you could imagine a game that relies
only on sound. Sometimes this can be a 2 step process where two players play together. One player
sees part of the game while another controls it. This has resulted in some pretty interesting games during
previous gamejams. 

Of course, the most common way of providing feedback is using 2d or 3d graphics. While 3d graphics are
cool, they take more work and skill to develop so 2d graphics is usually the best option for gamejams unless
you use things like unity.


Then you might want things like networking and high scores that are nice to have, but are not neccesairy for
all games. Both networking and high scores can be done by regular python without any libraries but for 
non text based graphics you need to use some kind of external library. 

#Library choise:

There are a couple of libraries out there for making games in python that let you do graphics, sound
and input among other things. However, none of these are perfect.

The biggest and most used one is probably pygame. A lot of people, myself included have used a library
called pygame during previous gamejams. It works but has a couple of issues. One of those is that the
documentation looks pretty ugly and isn't the best. There are a couple of other techical issues that
I will get to later but pygame is still one of the most maintained and general purpose 2d game engines
for python which is why I will show you it today.

Another alternative library that you could have a look at is PySFML. It is a wrapper around a C++ library
called SFML and is really nice to work with. It doesn't do more than you want but stil provides you 
with the things you DO want. Unfortunley, it is unmaintained and it doesn't compile at the moment. If it
starts updating in the future, I would suggest looking into it

Then there is a really nice library called PySDL2 which is a wrapper around a pretty widely used C
library called SDL2. I intended to show you SDL at first but it is a bit too low level for this presentation
and requires you to write a bit of boilerplate code in order to get rendering working. If you are interested,
you can have a look at my github profile where you can find a game that me and a few friends made that has
that boilerplate code worked out. If you don't want to use pygame (which also is based on SDL), I would
suggest looking into SDL2

These 3 are interchangeable, if you know how to do something in one of them, it should be fairly easy to
do the same thing in the other two. Where there are big differences between pygame and the others, I will
try to point them out. 

Finally, there are 2 different engines that you might want to have a look at. Cocos2D and panda 3d.
Cocos 2d is a 2d engine that does thigns in a specific way which you may or may not like. It takes
a while to get used to but I managed to make a game in it during a gamejam without having used it 
before.

Finally, if you really want to do 3d graphics, you can have a look at panda3d. I havn't used it 
but I think it's decent.


#Getting started with SDL

Alright, lets get started with the actual game programming. Since pygame is an external library 
that is not included in python by default, we need to install it separatley. Python has a great
somewhat official tool called *pip* that lets you install and configure packages using one commmand.

On most linux distributions you can install pip using the regular package manager. On windows and mac,
I don't know how to do it it is doable.

Once pip is installed, you can install pygame by running `pip install pygame`. You may need to install
some system packages aswell, like SDL, look up the documentation if you can't get it to work.

With pygame installed, you should be able to import it into your project by simply typing 
import pygame.

With pygame imported, you can run `pygame.init()` in order to initialise pygame and then you
can run `pygame.display.set_mode(resolution)` to create a window. Store the window in a variable
because we will need it later.


If we run this code, we can see that it doesn't crash and we get a window for a split second. However,
the window closes immeadietly. This is because the python script exits as soon as it is done running and
when the script closes, so does the window. 

To prevent the window from closing, you need to add a loop to keep the game running. We can do
that by adding `while True: pass`. The pass keyword, for those of you who havn't seen it simply does
nothing, it is there to allow you to add empty blocks like this.

If we run the code again, we can see that the window stays and we can move it around. However, you can't
close it. On my computer, the close window function doesn't work and I need to go to the script
and close it using Ctrl+C. 

This is because pygame doesn't know what to do when the window is closed. Perhaps some files need
to be saved which would be corrupted if the script closed immeadietly when the close action is performed,
or perhaps you want to ask the user if they really want to quit. 

In order to fix this, we need to tell pygame what to do when the user presses close.

#Events
This brings us to something called events

The point of events is to give us programmers a way to know when something has happened in the outside
world that might affect us. In pygame it is used for things like window closing, keyboard and mouse input,
gamepad input and window changes. Whenever an event happens, it is put on a list of things that have happened
since the last time we checked. 

When we are ready to, we can go through each event that has happened using a for-loop and the 
`pygame.event.get()` function. Each event has a type, and the type we are looking for is pygame.QUIT
which gets sent to us whenever the window close action is performed.

Now we need a way to allow us to exit the game loop whenver the event happens, so we change the loop
from `while True: #things` to `while running: #things`. If we set running to false when the user
closes the window, the program will exit. 

Let's run the code and see if it works


#Graphics

Now that we have a nice big window, we probably want to draw something on it. Pygame supports a wide
variety of drawing features. You can draw things like geometric shapes like lines and circles, text and 
images that you load from disk. Today I will focus on showing you image drawing but you should be able
to look in the documentation if you want to know how to draw other things.


Let's get started drawing an image then. Image drawing is done in two steps: First, you need to load the 
image from the disk. This should not be done too often as it is a pretty slow process so unless you can't 
avoid it, try to load all images at the start of the program. 

Once the images are loaded, you probably want to draw them somewhere on the screen. In pygame, this is done
using a function called `blit` which is run on the screen object we got earlier from the `display.set_mode()` 
function that we used earlier.

Blit takes 2 *required* arguments, an image to draw and a second argument that tells you where on the
screen to draw it. The image is the result of the `pygame.image.load("path")` function while the position
is a tuple that contains the target x and y pixels.

In my folder, I have a resources subfolder that contains a ghost.png. We can load it using 
`pygame.image.load("resources/ghost.png")` and display it using the image.blit function.



If we run this code, we notice that it doesn't do anything, our window is still black. This is because
of the way drawing is done in most game engines. Instead of drawing to the screen immeadietly, you actually
do the drawing to a buffer that contains a 'virtual' screen. When you are done drawing to the buffer,
you tell the program to send what you drew to the window. 

In pygame, this is done using the `pygame.display.flip()` function. In other engines this can be
called `sync` or `present`. When we add it to the code, we see our image in the top left corner.






<!--TODO: Add a note on other engines-->




#Some tips for the game jam
That was all the technical things I had to show today but I have some tips to give you for the gamejam which
I hope you will participate in. 

My first tip would be not to worry about trying to write great code. Your code will only be seen by you, and 
those you work with and only for 48 hours, you might think that you want to continue working on the game but
that doesn't happen. The most important thing is to get some sort of game working even if it isn't perfect.

The one exception to this is that you should avoid code reuse. If you see yourself doing the same calculation
more than once, do break it out into a function. Hardcoded calculations are difficult to change without
side effects.


Finally, I want to give you a piece of completely no-technical advice: Work with people you don't know which
I say as a pretty unsocial person. 
You will end up making some good friends that you wouldn't meet otherwise if you didn't. I would not
be part of lithe-kod if I didn't work with some people I didn't know during my first gamejam. That
doesn't mean don't work with people you know, you can create a group with some new and some old people
and during the gamejam, you will have a lot of time for brainstorming and creating teams. 

Finally, have fun while making the games. They will probably end up being pretty bad, almost all
gamejam games are so the focus should be on you having fun while making them. 


