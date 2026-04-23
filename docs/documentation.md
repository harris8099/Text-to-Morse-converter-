# 🔠 Technical Documentation: Morse Code Machine

This document outlines the core architecture, logic, and audio generation pipeline for the `main.py` Morse Code Machine application.

---

## 🏗️ Architecture Overview

The application uses a modular, event-driven architecture combining a graphical user interface with a background audio processing thread. It is built on four primary technical pillars:
1.  **GUI Framework:** `customtkinter` for modern UI elements and standard `tkinter` for custom canvas drawings (the LED).
2.  **Audio Synthesizer:** `numpy` generates mathematical waveforms, and `pygame` processes them for zero-latency playback.
3.  **Timing Engine:** Calculates precise sleep durations for signal dots, dashes, and pauses based on the standard Words Per Minute (WPM) formula.
4.  **Concurrency:** `threading` ensures the UI remains responsive while the blocking `time.sleep()` calls execute during playback.

---

## ⚙️ Dependencies

* `customtkinter`: Renders the dark-mode UI, buttons, sliders, and text boxes.
* `tkinter`: Specifically used for the `Canvas` widget to draw the circular LED.
* `numpy`: Handles fast, array-based mathematical generation of audio waveforms.
* `pygame`: Initializes the audio mixer (`44100` Hz, 16-bit, stereo) and plays the generated sounds.
* `threading`: Offloads the audio/visual playback loop from the main GUI thread.
* `time`: Manages the precise delays required for Morse code timing.

---

## ⏱️ Timing Engine & WPM Calculation

The speed of Morse code is governed by the Words Per Minute (WPM) slider. The base unit of time is the duration of a single "dot". 

### Timing Variables
The application dynamically calculates timings using the standard Morse code ratio:
* **Dot (`.`):** 1 time unit
* **Dash (`_`):** 3 time units
* **Intra-character gap (between dots/dashes):** 1 time unit
* **Letter gap (between characters):** 3 time units
* **Word gap (between words):** 7 time units

### WPM Formula
The script calculates the base "dot" duration in seconds using the standard formula:
```python
DOT = 1.2 / wpm
DASH = DOT * 3