import customtkinter as ctk
import tkinter as tk
import numpy as np
import pygame
import threading
import time

# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Init audio
pygame.mixer.init(frequency=44100, size=-16, channels=2)

# Constants
FREQ = 800
SAMPLE_RATE = 44100

# State
is_playing = False
is_muted = False

# Morse dictionary
morse_code = {
    'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
    'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
    'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
    'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
    'Y': '_.__', 'Z': '__..',
    '0': '_____', '1': '.____', '2': '..___', '3': '...__',
    '4': '...._', '5': '.....', '6': '_....', '7': '__...',
    '8': '___..', '9': '____.'
}

# Generate tone
def generate_tone(duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = np.sin(2 * np.pi * FREQ * t)
    audio = (tone * 32767).astype(np.int16)
    stereo = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo)

# Convert text → morse (NO "/")
def text_morse(text):
    words = text.upper().split()
    try:
        return '   '.join(   # 3 spaces between words
            ' '.join(morse_code[c] for c in word)
            for word in words
        )
    except KeyError:
        return "Only A-Z and 0-9 allowed!"

# LED
def led_on():
    canvas.itemconfig(led, fill="#ff3b3b")

def led_off():
    canvas.itemconfig(led, fill="#330000")

# Play Morse
def play_morse(morse):
    global is_playing
    is_playing = True
    status_label.configure(text="Playing...")

    wpm = speed_slider.get()
    DOT = 1.2 / wpm
    DASH = DOT * 3

    dot_sound = generate_tone(DOT)
    dash_sound = generate_tone(DASH)

    words = morse.split("   ")

    for w_i, word in enumerate(words):
        letters = word.split(" ")

        for l_i, letter in enumerate(letters):
            for s_i, symbol in enumerate(letter):
                if not is_playing:
                    break

                led_on()

                if not is_muted:
                    if symbol == '.':
                        dot_sound.play()
                    elif symbol == '_':
                        dash_sound.play()

                time.sleep(DOT if symbol == '.' else DASH)
                led_off()

                if s_i != len(letter) - 1:
                    time.sleep(DOT)

            if l_i != len(letters) - 1:
                time.sleep(DOT * 3)

        if w_i != len(words) - 1:
            time.sleep(DOT * 7)

    led_off()
    status_label.configure(text="Stopped")

# Controls
def start():
    text = entry.get()
    morse = text_morse(text)

    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", morse)
    output_box.configure(state="disabled")

    threading.Thread(target=play_morse, args=(morse,), daemon=True).start()

def stop():
    global is_playing
    is_playing = False
    pygame.mixer.stop()
    led_off()
    status_label.configure(text="Stopped")

def toggle_mute():
    global is_muted
    is_muted = not is_muted
    mute_btn.configure(text="Unmute" if is_muted else "Mute")

# UI
app = ctk.CTk()
app.title("Morse Code Machine")
app.geometry("540x520")

# Title
title = ctk.CTkLabel(app, text="Morse Code Machine", font=("Courier", 24, "bold"))
title.pack(pady=15)

# Input
entry = ctk.CTkEntry(app, width=380, placeholder_text="Enter text...")
entry.pack(pady=10)

# Buttons
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="Play", command=start, width=100).grid(row=0, column=0, padx=5)
ctk.CTkButton(btn_frame, text="Stop", command=stop, width=100, fg_color="#ff5555").grid(row=0, column=1, padx=5)

mute_btn = ctk.CTkButton(btn_frame, text="Mute", command=toggle_mute, width=100)
mute_btn.grid(row=0, column=2, padx=5)

# Slider
speed_label = ctk.CTkLabel(app, text="Speed (WPM)")
speed_label.pack()

speed_slider = ctk.CTkSlider(app, from_=5, to=30, number_of_steps=25)
speed_slider.set(15)
speed_slider.pack(pady=10)

# Output (BIG + copyable)
output_box = ctk.CTkTextbox(
    app,
    width=450,
    height=120,
    font=("Courier", 20, "bold"),
    corner_radius=10
)
output_box.pack(pady=10)
output_box.configure(state="disabled")

# LED
canvas = tk.Canvas(app, width=60, height=60, bg="#1a1a1a", highlightthickness=0)
canvas.pack(pady=10)
led = canvas.create_oval(10, 10, 50, 50, fill="#330000")

# Status
status_label = ctk.CTkLabel(app, text="Idle")
status_label.pack(pady=10)

app.mainloop()