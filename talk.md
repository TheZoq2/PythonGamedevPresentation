#Slide 1:

Introduction...


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



Cool, we can draw an image, but we probably don't want it to just stay in the top left corner. There
are 3 common thigns you want to manipulate when drawing images and those are position, scale and rotation.

I have briefly covered position already which is quite simple in pygame. All you need to do to change the
position where your image is drawn is to change the value of the second parameter for the blit function. 
The value passed to it is a tuple where the elements are the x and y coordinates where you want the
top left corner of the image to appear.


Rotation and scaling are not as simple but still very much doable. In pygame, they are done using
`pygame.transform` which contains a couple of functions that transform an image. One thing to note 
about them is that they return a new image and doesn't modify the original. 

Scaling is done by `pygame.transform.scale` which takes a source image and a tuple where the elements 
are the desired height
and width of the new image. This differs from most engines where scaling is done by percentage, you tell
the engine to create an image half the size, not 100x100 pixels.

Rotation is similar to scaling, instead if `.scale`, the function is called `.rotate` which takes an image
to rotate and an angle (in degrees) to rotate it by.


The code in `4game.py` demonstrates how these transforms work. First, the image is drawn normally at (0,0),
second the same image is drawn at (100, 100), third: the image is rotated by 45 degrees and drawn to the 
left and finally it is scaled to 400x400 pixels

Note that we can draw the same image twice in the same frame. Drawing using the `blit` or corresponding 
functions in pygame and a lot of other engines simply copies the pixels from an image to the screen 
without modifying the image itself.

##Continuous translation
So far, we have only drawn static things but in a game we probably want things to move. To do that, we 
add a variable called position that keeps track of where the image is currently. We update that variable
and draw the image in the current location in each iteration of the loop which should make it move across
the screen.


If we run `5game.py` we notice somethign weird however. The sprite moves along fine but it draws a trail as
it moves. This is because most game engines don't clear the buffers or windows once they have been drawn.
In most cases, we will probably draw over it anyway which means that clearing the screen is a waste
of performance.

Therefore, in order to get rid of the trail we will need to draw something to cover up the old frame and a
background image is a great way of doing that, atleast if we intend to have a background in the first place.

In our code, we add a background image that is loaded when the program starts, and then drawn first thing
in the loop. You have to make sure to not do any drawing between the `.flip` function and the background
being drawn as that will never be shown on the window.

As you can see from `6game.py` this works perfectly and we now have a ghost flying along in the desert.


##Rotation and the problem with pygame
The same thing should work for angles, right?. Of course not since I mention it :). Let's have a look at the
code in `7game.py`. It is the same as the previous example where the ghost moved across the screen except
position has been replaced by angle and the translation has been replaced by a rotation. If we run this code
you will notice that something is off. 


<!--Detailing the fix for this issue-->

##Other engines.
As you might imagine, doing rotation like this is quite tedious and beause of it, and a bunch of other
factors most engines don't have this issue. Instead, they separate image drawing from image storage by
using something called sprites. A sprite is an image with a scale, a position and a rotation and those
3 operations are done at once when drawing instead of trying to create imtermediate images. The reason
they can do that and pygame can't is partly because they use the GPU to do the heavy lifting while
pygame does it on the CPU. This also makes pygame fairly slow compared to hardware accelerated engines.

#Input

As I said earlier, input is a very important part of games as it is what sets games apart from things like 
movies. 

Dealing with input in pygame takes us back to events which I covered briefly for closing the window. As
I said then, events are a way for pygame to tell us about things that have happened in the outside
world. Whenever something interesting happens (keyboard/mouse input, window changes or gamepad input),
those things are put in a list of events. In order to separate them, the event.type variable
can be checked to find out what actually happened. As you can see from this table, the type of an
event can be things like `key pressed`, `mouse moved` or `joystick changed`. However, this information
isn't enough. Usually we want to know *What* key was pressed or *where* the mouse was moved which means
that the events also contain a bit of data. This data can be accessed by `event.<data>` where data
is things like .key keypresses or .pos for mouse events.

If we run this code that prints the event.key every time we get the KEYDOWN event, we notice that it
prints a different number for each keypress.

Let's use this information to make our ghost move using the arrow keys. We will reuse the position 
changing ghost that we had before but this time we dont' change position over time. Instead we update
the position when the left and right arrow keys are pressed. To find out what numbers corresponds to the
arrow keys, we could run the previous program and copy the numbers but that is both bad coding practice
and tedious. Instead we will use a set of constants defined by pygame which you can find on this link.

Left arrow is called `K_LEFT` and right arrow is called `K_RIGHT` so whenever we get a keydown event and
that the key corresponds to one of those constants we update the position. 

Let's run `a1game.py`. We notice that it sort of works but the ghost only moves when we press the keys,
not when we hold them. This is because we only get events when things change, not continuous updates
as they happen. If we want to make something happen while a key is held, we need to keep track
of wether or not the key is held ourselves by looking for both KEYDOWN and KEYUP events.

A neat way of doing this is using a datastructure called `set`. A set is a collection of unique items
where an item can either be part of the set or not. That is perfect for our usecase since it allows
us to add each key that gets pressed to the set and remove it once it gets released. In order to check
if the key is held, we simply check if that key exists in the set using the `in` operator.

If we run `a2game.py` we can move our sprite across the screen using the arrow keys.

Mouse and joystick input is quite similar. You either need to keep track of where the mouse was last
moved to or remember if a button is held or not, you should be able to figgure it out by looking at
the documentation and perhaps some examples.

#Game structure
Now that we know how to draw things and how to handle input I want to talk a bit about structuring our code.

Until now, I have put all the code in a single `main()` function but generally you want to split things
up in smaller chunks to make modifications and collaborations easier. A good general structure for a game
could be something like this. There are 3 main functions, one that handles what should happen in the game
each frame like moving enemies or updating score. The second function you want is a function
to draw the current state of the game and finally you want a function to handle all input. 

Most games contain a bit of data that needs to be passed around. This is things like player position,
player score, all the enemies and their data. The drawing and input functions need additional parameters
like a variable containing all the images to draw (remember that we don't want to load that each frame).

As you can see here, this just wouldn't be manageable long term. We need a better sollution.




##Avoid code reuse.
As you develop your game, you will realise that you want to change something, perhaps it is the size of
the enemeies or the speed of your character. Normally, you might write those values as numbers each time
you use them. For example, `if enemy_distance < 30 / 2: is_hit()` and `enemy_sprite.scale(30, 30)` ... As
This number, 30 might appear in 10 places around your code after a day of programming and once you realise
that the enemies should be 40 pixels wide instead, you need to change the 30 in to 40 in all those places.

This is a tedious process that is bound to introduce bugs. You should instead use a constant called 
`ENEMY_SIZE` that you set to 30. If you have used that constant everywhere, you can simply change the value
of it every time you want to change the size of an enemy which will be much more robust.

The same thing applies to calculations that you do in lots of places. If you notice yourself writing the same
calculation 3 or 4 times, break it out into a function. It will save you work when you use the same calculation
again and you have one place to change it if you notice it's wrong or want to update it.






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




#Installing on the IDA computers
Unfortunley, the pip version is severely outdated on the IDA computers which makes the process for installing
pygame a bit trickier. You need to use a tool called virtualenv which manages your python enviroments to install
an up-to-date version of pip. This also allows you to install pygame locally without *too* much hassle.

The first step is to create a  new virtual enviroment. This is done using the `virtualenv -p python3 <name>`.
This will create a folder called `<name>` which contains some local copies of programs.

The second step is to activate your new virtual enviroment. Run `source <path/to/venv>` and it will change your
PATH making your new programs prioritized. If you run pip3 --version, you should see something along the lines
of `9.x.x ... python3 ...`. If you do, you have installed it propperly and you can do what you normally would.

Each time you open a new terminal, you will need to reactivate the enviroment using the `source` command.
