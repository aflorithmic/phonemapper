import unittest
import phonemapper
from phonemapper import phonemapper as pm
import os
import itertools

class TestMap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TEST_DIR = os.path.dirname(os.path.abspath(__file__))
        cls.map_cmu_ipa = pm.load_map(os.path.join(cls.TEST_DIR,'test_cmu_to_ipa.json'))
        cls.data = pm.read_in_data(os.path.join(cls.TEST_DIR,'test_data.csv'))
        cls.test_row = next(itertools.islice(cls.data, 0, 1)) 
        print('test_row=', cls.test_row)
        cls.word = cls.test_row[0]
        print('word=', cls.word)
        cls.ipa = cls.test_row[1]
        print('ipa=', cls.ipa)
        cls.map_ipa_cmu = pm.invert_mapping(cls.map_cmu_ipa)
        cls.missing_phonemes = set()

    def test_map_load(self):
        self.assertEqual(self.map_cmu_ipa['W'], 'w', "Should be 'w'")

    def test_word_expected(self):
        self.assertEqual(self.word, 'hello', "Should be 'hello'")

    def test_ipa_expected(self):
        self.assertEqual(self.ipa, 'hɛləʊ', "Should be 'hɛləʊ'")

    def test_converter(self):
        self.assertEqual(pm.map_phoneme(self.map_ipa_cmu, "h"), 'HH', "Should be 'HH")
    
    def test_full_conversion(self):
        self.assertEqual(pm.map_row(self.map_ipa_cmu, self.test_row, self.missing_phonemes)[2], 'HH <EH> L AH0 <UH>', "Should be 'HH <EH> L AH0 <UH>'")

if __name__ == '__main__':
    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    unittest.main()