import unittest
from unittest.mock import MagicMock, patch
import speech_to_text as stt

class TestSpeechToText(unittest.TestCase):

    @patch('speech_to_text.sr.Microphone')
    @patch('speech_to_text.sr.Recognizer.listen')
    def test_record_audio(self, mock_listen, mock_microphone):
        audio = stt.record_audio()
        self.assertIsNotNone(audio)
        mock_microphone.assert_called_once()
        mock_listen.assert_called_once()

    @patch('speech_to_text.sr.Recognizer.recognize_google')
    def test_recognize_speech(self, mock_recognize_google):
        mock_audio = MagicMock()
        mock_recognize_google.return_value = 'Hello, world!'
        text = stt.recognize_speech(mock_audio)
        self.assertEqual(text, "Hello, world!")
        mock_recognize_google.assert_called_once_with(mock_audio)

    @patch("speech_to_text.sr.Recognizer.recognize_google")
    def test_convert_to_text_unknown_value_error(self, mock_recognize_google):
        mock_audio = MagicMock()
        mock_recognize_google.side_effect = stt.sr.UnknownValueError()
        with self.assertRaises(ValueError):
            stt.recognize_speech(mock_audio)
    
    @patch("speech_to_text.sr.Recognizer.recognize_google")
    def test_convert_to_text_request_error(self, mock_recognize_google):
        mock_audio = MagicMock()
        mock_recognize_google.side_effect = stt.sr.RequestError("API error")
        with self.assertRaises(ConnectionError):
            stt.recognize_speech(mock_audio)

if __name__ == '__main__':
    unittest.main()