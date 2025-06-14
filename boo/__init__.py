import time
import framebuf
from lib.display import Display
from lib.userinput import UserInput
from apps.boo.menu import menu  
from apps.boo.stats import stats  
import network  
import ntptime  


display = Display()
input = UserInput()

# Wi-Fi credentials
WIFI_NETWORKS = [
    ("YOUR_INTERNET", "password"),
    ("YOUR HOTSPOT", "password")
]


x_pos = 0
y_pos = 0
x_vel = 2
y_vel = 2


blink_interval = 3  
blink_duration = 0.2  
last_blink_time = time.ticks_ms()  


DATE_FILE_PATH = '/apps/boo/last_date.txt'

def load_image(filename):
    with open(f'/apps/boo/{filename}.raw', 'rb') as f:
        return f.read()

def draw_framebuffer(framebuffer, x_offset, y_offset):
    width = 32
    height = 32
    for y in range(height):
        for x in range(width):
            if framebuffer.pixel(x, y):
                display.pixel(x + x_offset, y + y_offset, 0xFFFF)

def draw_text(x, y, text, color):
    """Draw text on the display with a simulated larger size."""
    CHAR_WIDTH = 8
    cursor_x = x
    for char in text:
        if char == ' ':
            cursor_x += CHAR_WIDTH
        else:
            display.text(text=char, x=cursor_x, y=y, color=color)
            cursor_x += CHAR_WIDTH

def connect_wifi():
    """Connect to one of the predefined Wi-Fi networks."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    available_networks = wlan.scan()
    ssid_list = [network[0].decode() for network in available_networks]
    
    for ssid, password in WIFI_NETWORKS:
        if ssid in ssid_list:
            print(f"Connecting to {ssid}...")
            wlan.connect(ssid, password)
            for _ in range(10):  
                if wlan.isconnected():
                    print("Connected to Wi-Fi!")
                    return True
                time.sleep(1)
            print("Failed to connect to Wi-Fi")
    
    return False

def update_date():
    """Update the saved date using the NTP time."""
    try:
        ntptime.settime()  
        current_time = time.time()
        with open(DATE_FILE_PATH, 'w') as f:
            f.write(str(current_time))
    except Exception as e:
        print("Error updating date:", e)

def get_saved_date():
    """Retrieve the last saved date from the file."""
    try:
        with open(DATE_FILE_PATH, 'r') as f:
            return int(f.read().strip())
    except:

        return time.time()

def main_loop():
    global x_pos, y_pos, x_vel, y_vel, last_blink_time


    if connect_wifi():
        update_date()
    else:
        print("Using last saved date...")
        last_saved_date = get_saved_date()
        print("Last saved date:", time.localtime(last_saved_date))

    while True:
        keys = input.get_new_keys()

        if "2" in keys:
            stats(display, input)

        elif "1" in keys:
            menu(display, input)

        current_time = time.ticks_ms()


        ghost_data = load_image('ghost')
        blink_data = load_image('ghost_blink')
        
        ghost_fb = framebuf.FrameBuffer(bytearray(ghost_data), 32, 32, framebuf.MONO_HLSB)
        blink_fb = framebuf.FrameBuffer(bytearray(blink_data), 32, 32, framebuf.MONO_HLSB)


        if time.ticks_diff(current_time, last_blink_time) % (blink_interval * 1000) < blink_duration * 1000:
            framebuffer = blink_fb
        else:
            framebuffer = ghost_fb

        display.fill(0)
        draw_framebuffer(framebuffer, x_pos, y_pos)


        draw_text(x=5, y=0, text='1: Menu 2: Stats', color=0xFFFF)

        display.show()


        x_pos += x_vel
        y_pos += y_vel


        if x_pos <= 0 or x_pos + 32 >= 240:
            x_vel = -x_vel
        if y_pos <= 0 or y_pos + 32 >= 135:
            y_vel = -y_vel


        del ghost_data, blink_data, ghost_fb, blink_fb

        time.sleep(0.1)


main_loop()
