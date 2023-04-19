# About
Code to implement speech recognition using local microphone and Google API to text conversion. I requires at least a working device and internet connection. Adjustments on ambient noise, voice detection threshold and timeout can be made.
# Packages
- PyAudio
- Speech_Recognition
# Logic
1. Check for local devices;
2. Identify which device is detecting the loudest noise;
3. Turn on microphone;
4. Identify silence after voice was recorded;
5. Send audio data to Google API;
6. Present best related text identified.
