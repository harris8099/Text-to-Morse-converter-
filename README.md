# 🔠 Morse Code Machine

A modern **Text → Morse Code converter** with sound, visual feedback, and a clean UI.

This application lets you convert text into Morse code, play it with realistic timing, and visualize the signal using an LED-style indicator — all in a smooth desktop interface.

---

## ✨ Features

* 🔤 Convert text to Morse code instantly
* 🔊 Real-time audio playback (dot/dash tones)
* 🔴 LED indicator synced with Morse signals
* 🎚️ Adjustable speed (WPM – Words Per Minute)
* 🔇 Mute / Unmute audio
* 📋 Large, copyable Morse output
* 🎨 Modern UI using `customtkinter`

---

## 🖥️ Preview

![App Preview](image.png)

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/harris8099/Text-to-Morse-converter-.git
cd Text-to-Morse-converter-
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install numpy pygame customtkinter
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 🧠 How It Works

* Text is converted into Morse using a dictionary mapping
* Morse timing follows international standards:

  * Dot = 1 unit
  * Dash = 3 units
  * Letter gap = 3 units
  * Word gap = 7 units
* Audio is generated dynamically using `pygame`
* LED blinks in sync with the signal

---

## 📂 Project Structure

```
├── main.py
├── requirements.txt
├── image.png
└── README.md
```

---

## 🛠️ Tech Stack

* Python 🐍
* customtkinter 🎨
* pygame 🔊
* numpy 📊

---

## 🤝 Contributing

Contributions are welcome!

If you’d like to improve the UI, add decoding, or enhance features:

1. Fork the repo
2. Create a new branch
3. Submit a pull request

---

## 💡 Future Improvements

* ⌨️ Live key input (real-time Morse typing)
* 📥 Morse → Text decoder
* 💾 Export Morse as audio file (.wav)
* 🎛️ Advanced UI (knobs, signal meter)
* 🔌 ESP32 hardware integration

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

Inspired by classic Morse communication systems and modern UI design.
# 🔠 Morse Code Machine

A modern **Text → Morse Code converter** with sound, visual feedback, and a clean UI.

This application lets you convert text into Morse code, play it with realistic timing, and visualize the signal using an LED-style indicator — all in a smooth desktop interface.

---

## ✨ Features

* 🔤 Convert text to Morse code instantly
* 🔊 Real-time audio playback (dot/dash tones)
* 🔴 LED indicator synced with Morse signals
* 🎚️ Adjustable speed (WPM – Words Per Minute)
* 🔇 Mute / Unmute audio
* 📋 Large, copyable Morse output
* 🎨 Modern UI using `customtkinter`

---

## 🖥️ Preview

![App Preview](image.png)

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/harris8099/Text-to-Morse-converter-.git
cd Text-to-Morse-converter-
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install numpy pygame customtkinter
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 🧠 How It Works

* Text is converted into Morse using a dictionary mapping
* Morse timing follows international standards:

  * Dot = 1 unit
  * Dash = 3 units
  * Letter gap = 3 units
  * Word gap = 7 units
* Audio is generated dynamically using `pygame`
* LED blinks in sync with the signal

---

## 📂 Project Structure

```
├── main.py
├── requirements.txt
├── image.png
└── README.md
```

---

## 🛠️ Tech Stack

* Python 🐍
* customtkinter 🎨
* pygame 🔊
* numpy 📊

---

## 🤝 Contributing

Contributions are welcome!

If you’d like to improve the UI, add decoding, or enhance features:

1. Fork the repo
2. Create a new branch
3. Submit a pull request

---

## 💡 Future Improvements

* ⌨️ Live key input (real-time Morse typing)
* 📥 Morse → Text decoder
* 💾 Export Morse as audio file (.wav)
* 🎛️ Advanced UI (knobs, signal meter)
* 🔌 ESP32 hardware integration

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

Inspired by classic Morse communication systems and modern UI design.
