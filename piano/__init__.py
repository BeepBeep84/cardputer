import time
from machine import I2S, Pin
import math
from lib import userinput, display


disp = display.Display()


SCK_PIN = 41
WS_PIN = 43
SD_PIN = 42
I2S_ID = 1
BUFFER_LENGTH_IN_BYTES = 8192
SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.STEREO
SAMPLE_RATE_IN_HZ = 64000


audio_out = I2S(
    I2S_ID,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mode=I2S.TX,
    bits=SAMPLE_SIZE_IN_BITS,
    format=FORMAT,
    rate=SAMPLE_RATE_IN_HZ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

# Frequency of musical notes
tones = {
    # White keys
    "C4": 262, "D4": 294, "E4": 330, "F4": 349, "G4": 392,
    "A4": 440, "B4": 494, "C5": 523, "D5": 587, "E5": 659,
    # Black keys (sharps, skipping E# and B#)
    "CS4": 277, "DS4": 311, "FS4": 370, "GS4": 415, "AS4": 466,
    "CS5": 554, "DS5": 622, "FS5": 740, "GS5": 831, "AS5": 932
}

def gen_sin_wave(freq, volume):
    radians_increment = (math.pi / SAMPLE_RATE_IN_HZ) * freq / 2
    samples = bytearray()
    rads_current = 0
    while rads_current < math.pi:
        sample = math.floor(((math.sin(rads_current)) * 127.5 * volume))
        samples += bytearray((sample, sample))
        rads_current += radians_increment
    return samples

def play_tone(freq, vol, length):
    samples = gen_sin_wave(freq, vol)
    num_sample_loops = int(length * freq)
    for _ in range(num_sample_loops):
        audio_out.write(samples)

def play_note(note, vol=0.5, length=0.2):
    freq = tones[note]
    play_tone(freq, vol, length)


input_handler = userinput.UserInput()

# Mapping keyboard keys to notes (white and black keys)
key_to_note = {
    # White keys (QWERTYUIOP)
    'Q': "C4", 'W': "D4", 'E': "E4", 'R': "F4", 'T': "G4",
    'Y': "A4", 'U': "B4", 'I': "C5", 'O': "D5", 'P': "E5",
    
    # Black keys (123467890)
    '1': "CS4", '2': "DS4", '4': "FS4", '5': "GS4", '6': "AS4",
    '7': "CS5", '8': "DS5", '0': "AS5"
}


def draw_key_layout():
    disp.fill(0x7bcf)  
    
    # Text for black and white key rows
    black_keys_text = " 1 2 3 4 5 6 7 8 9 0 "
    black_notes_text = " C D   F G A   C D   "
    white_keys_text = " Q W E R T Y U I O P  "
    white_notes_text = " C D E F G A B C D E   "


    screen_width = 240
    black_keys_width = len(black_keys_text) * 8  
    white_keys_width = len(white_keys_text) * 8

    black_keys_x = (screen_width - black_keys_width) // 2
    white_keys_x = (screen_width - white_keys_width) // 2


    disp.fill_rect(0, 5, screen_width, 15, 0x0000)  
    disp.text("[black keys -  sharp]", (screen_width - 21 * 8) // 2, 8, 0xFFFF)  


    disp.text(black_keys_text, black_keys_x, 30, 0xFFFF)  
    disp.text(black_notes_text, black_keys_x, 45, 0xFFFF)  


    disp.fill_rect(0, 61, screen_width, 15, 0xFFFF)  
    disp.text("[white keys - natural]", (screen_width - 22 * 8) // 2, 66, 0x0000)  


    disp.text(white_keys_text, white_keys_x, 85, 0x0000)  
    disp.text(white_notes_text, white_keys_x, 100, 0x0000)  

    disp.show()


draw_key_layout()


while True:
    pressed_keys = input_handler.get_new_keys()  
    
    if pressed_keys:
        for key in pressed_keys:
            upper_key = key.upper()  
            if upper_key in key_to_note:
                note = key_to_note[upper_key]
                play_note(note, vol=0.5, length=0.2)  
                print(f"Playing note: {note}")  

    time.sleep(0.1)

audio_out.deinit()
