import pandas as pd
import scipy.signal as signal
import sounddevice as sd
import os
import math
import numpy as np
import time


def play_frequency(frequency, duration=0.25, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)

    # Anti-clicking volume envelope: 5ms fade-in, 15ms fade-out
    fade_in = int(sample_rate * 0.005)
    fade_out = int(sample_rate * 0.015)

    env = np.ones_like(wave)
    if len(wave) > (fade_in + fade_out):
        env[:fade_in] = np.linspace(0, 1, fade_in)
        env[-fade_out:] = np.linspace(1, 0, fade_out)
    else:
        # Fallback for extremely short notes
        half = len(wave) // 2
        env[:half] = np.linspace(0, 1, half)
        env[-half:] = np.linspace(1, 0, half)

    wave *= env
    sd.play(wave.astype(np.float32), sample_rate)
    sd.wait()


def play_arpeggio(midi_notes, note_duration=0.25, repetitions=1):
    """Plays the notes of a chord sequentially with anti-pop protection."""
    for _ in range(repetitions):
        for note in midi_notes:
            freq = midi_to_freq(note)
            play_frequency(freq, duration=note_duration)


def midi_to_freq(midi_note):
    return 440.0 * (2.0 ** ((midi_note - 69) / 12.0))


def play_chord(midi_notes, duration=2.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Mix all the sine waves together
    wave = sum(np.sin(2 * np.pi * midi_to_freq(n) * t) for n in midi_notes)

    # Lower the volume so it doesn't distort/clip
    wave = wave / len(midi_notes)

    sd.play(wave.astype(np.float32), sample_rate)
    sd.wait()


scale = []

play_chord([69, 73, 76, 79])
play_chord([69, 73, 76, 80])
play_chord([69, 73, 76, 78])
play_chord([69, 73, 76, 79])
play_chord([69, 74, 76, 78])



