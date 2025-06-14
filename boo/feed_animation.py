import time
import framebuf
from lib.display import Display


IMAGE_WIDTH = 32
IMAGE_HEIGHT = 32
TEXT_COLOR = 0xFFFF  
TEXT_X_OFFSET = IMAGE_WIDTH + 5 
TEXT_Y_OFFSET = 10  

def load_image(filename):
    with open(f'/apps/boo/{filename}.raw', 'rb') as f:
        return f.read()

def draw_framebuffer(display, framebuffer, x_offset, y_offset):
    """Draw the framebuffer on the display at a specified position."""
    for y in range(IMAGE_HEIGHT):
        for x in range(IMAGE_WIDTH):
            if framebuffer.pixel(x, y):
                display.pixel(x + x_offset, y + y_offset, 0xFFFF)  

def draw_text(display, x, y, text):
    """Draw text on the display at the specified position."""
    display.text(text=text, x=x, y=y, color=TEXT_COLOR)

def feed_animation(display):
    """Play the feed animation with text appearing one at a time."""
    ghost_eat_data = load_image('ghost_eat')
    ghost_blink_data = load_image('ghost_blink')

    ghost_eat_fb = framebuf.FrameBuffer(bytearray(ghost_eat_data), IMAGE_WIDTH, IMAGE_HEIGHT, framebuf.MONO_HLSB)
    ghost_blink_fb = framebuf.FrameBuffer(bytearray(ghost_blink_data), IMAGE_WIDTH, IMAGE_HEIGHT, framebuf.MONO_HLSB)

    
    x, y = 48, 48
    text_x = x + TEXT_X_OFFSET  
    text_y = y  

    
    texts = ["OM", "NOM", "NOM"]
    text_y_offsets = [0, TEXT_Y_OFFSET, 2 * TEXT_Y_OFFSET]  

    
    for i in range(3):  
        display.fill(0)  
        if i % 2 == 0:
            draw_framebuffer(display, ghost_eat_fb, x, y)
        else:
            draw_framebuffer(display, ghost_blink_fb, x, y)


        for j in range(i + 1):
            draw_text(display, text_x, text_y + text_y_offsets[j], texts[j])

        display.show()
        time.sleep(0.5)  

    
    for _ in range(6):  
        display.fill(0)  
        if _ % 2 == 0:
            draw_framebuffer(display, ghost_eat_fb, x, y)
        else:
            draw_framebuffer(display, ghost_blink_fb, x, y)

      
        for j in range(3):
            draw_text(display, text_x, text_y + text_y_offsets[j], texts[j])

        display.show()
        time.sleep(0.2) 

 
    display.fill(0)
    display.show()
