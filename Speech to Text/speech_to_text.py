# Import packages
import speech_recognition as sr
import pyaudio

# Settings
recognizer = sr.Recognizer()

# Identify working mics
def identify_microphone():
    device_index = None
    highest_volume = 0
    for (index, device) in sr.Microphone().list_working_microphones().items():
        with sr.Microphone(device_index=index) as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.record(source, duration=1)
        volume = max(audio.frame_data)
        print(f'Device: {device} on index {index} registered audio {volume}.')
        if volume > highest_volume:
            highest_volume = volume
            device_index = index
    return device_index

# Listen from mic
def record_audio(device_index):
    with sr.Microphone(device_index=device_index) as source:
        print('Listening...')
        audio = recognizer.listen(source, timeout=10000)
    return audio

# Convert to text
def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        raise ValueError('Non recognizable audio.')
    except sr.RequestError as e:
        raise ConnectionError(f'Connection problem: {e}.')

if __name__ == '__main__':
    device_index = identify_microphone()
    audio = record_audio(device_index)
    try:
        text = recognize_speech(audio)
        print(text)
    except Exception as e:
        print(e)