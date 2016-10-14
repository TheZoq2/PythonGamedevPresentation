import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "resources")

#Uncomment the following line if you want text. It requires you to place a .ttf font
#in the resources directory called pixelated.ttf
#FONTMANAGER = sdl2.ext.FontManager(RESOURCES.get_path("pixeled.ttf"), size=5)

class Renderer:
    def __init__(self, title, size):
        sdl2.ext.init()
        self.window = sdl2.ext.Window(title, size=size)
        main_renderer = sdl2.ext.Renderer(self.window)

        #You can change this value if you want to change the size of each
        #pixel in the window. Increase if you want a more pixel-art like 
        #game
        main_renderer.scale = (1,1)
        self.window.show()

        self.factory = sdl2.ext.SpriteFactory(renderer=main_renderer)

        self.cam_pos = (0,0)

        self.renderer = self.factory.create_sprite_render_system(self.window)




    def render_sprites(self, sprites):
        rect = sdl2.rect.SDL_Rect(0, 0, 0, 0)

        for sprite in sprites:
            rect.x = sprite.x - self.cam_pos[0]
            rect.y = sprite.y - self.cam_pos[1]
            rect.w, rect.h = sprite.size

            scale_x, scale_y = sprite.scale
            rect.w = int(scale_x * rect.w)
            rect.h = int(scale_y * rect.h)

            if sprite.center:
                rect.x -= rect.w // 2
                rect.y -= rect.h // 2

            if sdl2.render.SDL_RenderCopyEx(self.renderer.sdlrenderer,
                                            sprite.texture,
                                            None,
                                            rect,
                                            sprite.angle,
                                            None,
                                            sdl2.render.SDL_FLIP_NONE) == -1:
                return False

    def present(self):
        """
        This function should be called when you want to draw a whole frame
        """
        sdl2.render.SDL_RenderPresent(self.renderer.sdlrenderer)



    def set_camera_position(self, pos):
        self.cam_pos = pos



    def load_sprite(self, path):
        sprite = self.factory.from_image(RESOURCES.get_path(path))
        sprite.angle = 0
        sprite.scale = (1, 1)
        sprite.center = True
        return sprite


    def create_rect(self, color, size):
        sprite = self.factory.from_color(color, size=size)
        sprite.angle = 0
        sprite.scale = (1, 1)
        sprite.center = True
        return sprite


    def render_text(text):
        surface = FONTMANAGER.render(text)
        sprite = self.factory.from_surface(surface)
        sprite.angle = 0
        sprite.scale = (1, 1)
        sprite.center = True
        return sprite
