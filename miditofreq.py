import numpy as np
import sounddevice as sd


def midi_to_freq(midi_note):
    if midi_note is None:  # Handle musical rests
        return 0
    return 440.0 * (2.0 ** ((midi_note - 69) / 12.0))


def generate_sine_wave(frequency, duration, sample_rate=44100):
    if frequency == 0:
        return np.zeros(int(sample_rate * duration))

    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)

    # 5ms fade-in, 15ms fade-out
    fade_in = int(sample_rate * 0.005)
    fade_out = int(sample_rate * 0.015)
    env = np.ones_like(wave)
    if len(wave) > (fade_in + fade_out):
        env[:fade_in] = np.linspace(0, 1, fade_in)
        env[-fade_out:] = np.linspace(1, 0, fade_out)

    return wave * env


def play_song(melody_track, chord_track, sample_rate=44100):
    total_melody_time = sum(item[1] for item in melody_track)
    total_audio_length = int(sample_rate * total_melody_time)

    master_melody_wave = np.zeros(total_audio_length)
    master_chord_wave = np.zeros(total_audio_length)

    # 2. Build the Melody Timeline
    current_sample = 0
    for note, duration in melody_track:
        if note is None:
            wave = np.zeros(int(sample_rate * duration))
        else:
            freq = midi_to_freq(note)
            wave = generate_sine_wave(freq, duration, sample_rate)

        end_sample = current_sample + len(wave)

        if end_sample <= total_audio_length:
            master_melody_wave[current_sample:end_sample] += wave
        current_sample = end_sample

    current_sample = 0
    for chord_notes, duration in chord_track:
        chord_wave = np.zeros(int(sample_rate * duration))

        if chord_notes:
            valid_notes = [n for n in chord_notes if n is not None]

            if valid_notes:
                for note in valid_notes:
                    freq = midi_to_freq(note)
                    chord_wave += generate_sine_wave(freq, duration, sample_rate)
                chord_wave /= len(valid_notes)

        end_sample = current_sample + len(chord_wave)
        if end_sample <= total_audio_length:
            master_chord_wave[current_sample:end_sample] += chord_wave
        current_sample = end_sample

    mixed_master = (master_melody_wave * 0.6) + (master_chord_wave * 0.4)

    max_val = np.max(np.abs(mixed_master))
    if max_val > 0:
        mixed_master /= max_val

    sd.play(mixed_master.astype(np.float32), sample_rate)
    sd.wait()


melody = [
    (72, 0.5),
    (72, 0.5),
    (71, 0.25),
    (71, 0.25),
    (71, 0.25),
    (71, 0.5),
    (69, 0.25),
    (69, 1.3),
    (71, 0.3),
    (72, 0.3),
    (None, 0.2),
    (72, 0.25),
    (72, 0.25),
    (72, 0.25),
    (74, 0.25),
    (71, 0.25),
    (67, 0.25),
    (71, 0.25),
    (69, 0.25),
    (69, 1.5),
    (67, 0.3),
    (65, 0.3),
]

chords = [
    ([57, 60, 64], 1.0),  # Am for 1.0 second
    ([55, 59, 62], 1.5),  # G for 1.5 seconds
    ([53, 57, 60], 1.9),  # F for 1.5 seconds
    ([None], 0.2),
    ([57, 60, 64], 1.0),  # Am for 1.0 second
    ([55, 59, 62], 1.5),  # G for 1.5 seconds
    ([53, 57, 60], 2.2),  # F for 1.5 seconds
]

print("No Tears Left to Cry: Ariana Grande Intro")
play_song(melody, chords)