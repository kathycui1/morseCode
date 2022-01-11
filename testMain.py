from main import *
import unittest


class TestMorse(unittest.TestCase):

    # test a single word with letters
    def test_word(self):
        result = morse("tetris")
        self.assertEqual(result, "- . - .-. .. ...")

    # test a single word with letters and numbers
    def test_letters_numbers(self):
        result = morse("kathycui8")
        self.assertEqual(result, "-.- .- - .... -.-- -.-. ..- .. ---..")

    # test a sentence
    def test_sentence(self):
        result = morse("Hey, how about 8pm?")
        self.assertEqual(result, ".... . -.-- --..--   .... --- .--   .- -... --- ..- -   ---.. .--. -- ..--..")

    # test morse code word
    def test_code_word(self):
        result = morse("-.- .- - .... -.--")
        self.assertEqual(result, "KATHY")

    # test morse code sentence
    def test_code_sentence(self):
        result = morse("-.. ---  -.-- --- ..- .-.. .. -.- . -- --- ...- .. . ... ..--..")
        self.assertEqual(result, "DOYOULIKEMOVIES?")


