#Slide 1

Some sort of introduction


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
all games. Both networking and high scores can be done by regular python and C++ without any libraries but for 
non text based graphics you need to use some kind of external library. 

#SFML

Before the fall gamejam, I held a similar presentation on game development using 
the library pygame. _Were any of you there?_. Pygame is nice, but as I touched
on in the last talk, it has some issues. At the time, SFML, which I will talk about today
didn't compile propperly. Luckily that has changed and we can use it again

Unlike pygame, everything is drawn on the GPU instead of on the CPU which has some great
benefits. First of all, it's a lot faster because GPUs are built to draw graphics really quickly.
Second, in pygame, an image is what you draw to the screen directly, which means that when you
want to rotate the thing you want to draw, you need to create a new image, with the content rotated
and then draw it. This is slow and makes rotation around a certain point much harder than it should be.

#C++ / python

Another neat thing about SFML is that it has bindings for a lot of languages. This includes
languages like java and c but also more exotic thigns like Rust, go, ocaml and haskell. Some of
them may be a bit outdated but most of them should work.

Today, I will focus on using C++ and python. Everyone here probably knows some python and it is a
nice language for thigns like gamejams where quick development is more important than fast
code and fast execution. C++ on the other hand is very fast and, in my opinion, easier to maintain.

Another neat thing about having a library with both python and C++ bindings is that if you decide
to try come C++ at some point, you can use SFML which you already know and you can start making
cool things faster.

#Installation

__TODO__

#Introduction to drawing

##(Something to draw on) A window

###Unresponsive window

##Shapes?

##Textured shapes (sprites)

##Transformations

###How drawing is done
Loading things -> storing in ram -> uploading to the GPU

##Particle effects


##Viewports?

#Inputs and events

_?_
#More advanced things

##Shaders


_?_

#Code structure

#Some tips for the jam


