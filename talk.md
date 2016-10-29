#Slide 1:

Introduction


#Library choise:

In order to draw graphics using python (or any other language), you need to use an external library. 
Unfortunley, when it comes to python, there is a lack of good graphics libraries. 

A lot of people would suggest using pygame which is a good option. It is well maintained and a lot of people
have used it during previous gamejams. However, the documentation isn't the best and it doesn't support
hardware acceleration which may make your game slow. That shouldn't be a problem but along with the lack
of hardware acceleration comes another issue: you can't rotate images without some extra code. There are
some other caviates with pygame but it is still a great library which you should atleast have a look
at if you are interested.

Last gamejam, I wanted to use something other than pygame for my game and I came across pysfml. It is a
great library, it's based on a well established C++ library and did things the way you would expect. However,
it is not maintained anymore, is not in any package managers and does not compile right now.

For that reason, I have decided to do this presentation on a library called PySDL. SDL is a low level 
graphics library that is well established in other languages. The python bindings are maintained
and the documentation seems decent. It does have some caviates of its own though, which I will get to later.

There are some other libraries out there that may also be of interest. I have tried cocos2d during a gamejam
but it is not as simple as the other libraries and does things in a different way. There are also things
like panda 3d if you want to go down the 3d route.


#Components of a game

What components do you need to make a game?

The first thing we need is graphics. The players need to be able to see what's going on in the game while
playing. This could be anything from a text based interface to fancy 3d graphics. Today we will only
use simple 2d graphics, both because it's a lot easier than 3d graphics and because it is what SDL supports.
For most gamejam games, 2d graphics is the perfect balance between graphics quality and ease of development.

Another thing we need is input. Most games would be pretty boring if you were unable to interract with them.
SDL supports a wide variety of input devices but for this game, we will just use the keyboard.

Another thing which is usually forgotten during gamejams is sound. SDL supports playing sounds aswell
so if we have time, we will add it to this game.


#Getting started with SDL

SDL, unlike most other libraries you have used so far in the introductory course is not built into python
so you will have to install it yourself. Luckily, python has a really neat tool for installing libraries
called pip. On most linux distros, you can install it using the package manager of your choise. For windows,
the process might be a bit more involved but it should be fairly simple.

Once you have acquired pip, you simply need to run `pip install pysdl2` and it will download and install
the library for you.

With the library installed by pip, you should be able to simply import it into your python program. So lets
open a new file and type `import sdl2`, the base library, aswell as `import sdl2.ext` which provides more
advanced features for using SDL with python specifically.

If we run the file and everything is installed correctly, it should simply exit without any error messages.
Good, it did. Time to make the actual game


#The downside of SDL
Like I mentioned in the beginning of the presentation, sdl2 has some downsides. The main one being that
some boilerplate code is required for using the hardware accelerated graphics which I mentioned earlier. 
The code required is around 100 lines and I have created a simple python file which you can import into 
your project that should make using SDL easier. 

The file can be found at `github.com/thezoq2/...`

Let's download it.
`wget <url>`

For those that don't know, wget downloads files from the terminal.

Once we have it downloaded, we can import it into the project by writing `from render_util import Renderer`.

Now we can test it out by writing `renderer = Renderer(<title>, <screen resolution as tuple>)`

If we run this code, we see a window popping up briefly. This means that the renderer works, but we have no
code for our game which means that the script exits immeadietly. 

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


