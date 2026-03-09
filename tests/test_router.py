# tests/test_router.py

import unittest
from classifier import classify_intent
from router import route_and_respond

class TestAIRouter(unittest.TestCase):

    def test_classify_code_intent(self):
        msg = "How do I sort a list in Python?"
        result = classify_intent(msg)
        self.assertEqual(result['intent'], 'code')
        self.assertTrue(0 <= result['confidence'] <= 1)

    def test_classify_writing_intent(self):
        msg = "Can you help me improve this paragraph?"
        result = classify_intent(msg)
        self.assertEqual(result['intent'], 'writing')
        self.assertTrue(0 <= result['confidence'] <= 1)

    def test_route_code_response(self):
        msg = "Fix this Python bug: for i in range(10) print(i)"
        intent = classify_intent(msg)
        response = route_and_respond(msg, intent)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_unclear_intent(self):
        msg = "Blah blah random text"
        intent = classify_intent(msg)
        response = route_and_respond(msg, intent)
        if intent['intent'] == 'unclear':
            self.assertIn("Are you asking for help with coding, data analysis, writing, or career advice?", response)


if __name__ == "__main__":
    unittest.main()