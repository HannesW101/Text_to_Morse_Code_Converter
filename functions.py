import tkinter as tk
from UI import App
import pygame
from time import sleep
import threading

# initialise the mixer
pygame.mixer.init()

# flag to control whether the Morse code is playing or not
is_playing = False

# Load audio files for morse code
dot_sound = pygame.mixer.Sound('Sounds/morse-code-dot.mp3')
dash_sound = pygame.mixer.Sound('Sounds/morse-code-dash-.mp3')

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}


# conversion using morse code dictionary
def text_to_morse(input_string):
    return ' '.join(MORSE_CODE_DICT[char.upper()] for char in input_string if char.upper() in MORSE_CODE_DICT)


# morse code sound logic
def play_morse_code(morse_string, app_instance):
    global is_playing
    is_playing = True
    for idx, char in enumerate(morse_string):
        if not is_playing:
            break
        app_instance.highlight_char_at_index(idx)
        if char == ".":
            dot_sound.play()
            sleep(0.1)  # duration of the dot sound
        elif char == "-":
            dash_sound.play()
            sleep(0.3)  # duration of the dash sound
        else:
            sleep(0.1)  # duration of spaces between characters or words
    app_instance.remove_highlighting()
    is_playing = False


class FunctionalApp(App):
    def clear_default_text(self, event=None):
        if self.input_text.get("1.0", tk.END).strip() == "Type the text you want converted here":
            self.input_text.delete("1.0", tk.END)

    def convert_text(self, event=None):
        text = self.input_text.get("1.0", tk.END).strip()
        # conversion
        text = text_to_morse(text)
        # Output
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)

    def play_sound(self, event=None):
        global is_playing

        # Check if it's already playing and stop it
        if is_playing:
            is_playing = False
            return

        text = self.output_text.get("1.0", tk.END).strip()

        # Start a new thread for playing the Morse code
        thread = threading.Thread(target=play_morse_code, args=(text, self))
        thread.start()

        # Bind click anywhere to stop the sound
        self.root.bind("<Button-1>", self.stop_sound)

    def stop_sound(self, event=None):
        global is_playing
        is_playing = False
        # Unbind the event so that it doesn't interfere with other interactions
        self.root.unbind("<Button-1>")

    def highlight_char_at_index(self, idx):
        # Clear previous tag if any
        self.output_text.tag_remove("highlight", "1.0", tk.END)

        # Create tag for the character at given index
        self.output_text.tag_add("highlight", f"1.0+{idx}c", f"1.0+{idx + 1}c")
        self.output_text.tag_config("highlight", foreground="#192655")

    def remove_highlighting(self):
        # Remove the tag
        self.output_text.tag_remove("highlight", "1.0", tk.END)
