<!--theme: sjaakvandenberg/cleaver-dark-->
theme: jdan/cleaver-retro

---
#Making games in python

##Frans skarman
##2016

---

###Libraries

- Pygame 

- PySFML (unmaintained)

- PySDL2 (what I will show you)

- Cocos2D


---

###Components of a game

- Graphics

- Input

- Sounds?

- High scores?


---

###SDL2

Install the library
``` Bash
> pip install pysdl2
```

Import it in your project
```Python
import sdl2
import sdl2.ext

def main():
	print("Hello world")

main()
```

---


###The main loop

```Python
while True:
	handle_user_input()

	do_game_stuff()

	draw_things()

	present_to_window()
```

---

