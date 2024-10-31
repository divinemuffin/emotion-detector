import unittest

from EmotionDetection.emotion_detection import emotion_detector, get_raw_emotions_w_dominant

class TestEmotionPackage(unittest.TestCase):
    def test_joy(self):
        joyTest = get_raw_emotions_w_dominant(emotion_detector("I am glad this happened"))
        self.assertEqual(joyTest['dominant_emotion'], 'joy')
        
    def test_anger(self):
        angerTest = get_raw_emotions_w_dominant(emotion_detector("I am really mad about this"))
        self.assertEqual(angerTest['dominant_emotion'], 'anger')
        
    def test_disgust(self):
        disgustTest = get_raw_emotions_w_dominant(emotion_detector("I feel disgusted just hearing about this"))
        self.assertEqual(disgustTest['dominant_emotion'], 'disgust')
        
    def test_sadness(self):
        sadnessTest = get_raw_emotions_w_dominant(emotion_detector("I am so sad about this"))
        self.assertEqual(sadnessTest['dominant_emotion'], 'sadness')
        
    def test_fear(self):
        fearTest = get_raw_emotions_w_dominant(emotion_detector("I am really afraid that this will happen"))
        self.assertEqual(fearTest['dominant_emotion'], 'fear')

unittest.main()