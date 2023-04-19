# Import packages
import speech_recognition as sr

# Settings
recognizer = sr.Recognizer()

# Identify working mics
for (index, device) in sr.Microphone().list_working_microphones().items():
    print(f'Device: {device} on index {index}.')

# Listen from mic
def record_audio():
    with sr.Microphone(device_index=4) as source:
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
    audio = record_audio()
    try:
        text = recognize_speech(audio)
        print(text)
    except Exception as e:
        print(e)