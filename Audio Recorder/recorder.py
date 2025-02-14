import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

def find_loopback_device():
    for i in range(p.get_device_count()):
        dev_info = p.get_device_info_by_index(i)
        if "Virtual Audio Cable" in dev_info.get('name'):
            return i
    return None

device_index = find_loopback_device()
print(device_index)

def record_audio(index):
    p = pyaudio.PyAudio()
    OUTPUT_FILENAME = f"output/output_{index}.wav"
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=index)

    print("Recording...")

    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
