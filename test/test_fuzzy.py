from flashtext import KeywordProcessor
import logging
import unittest
import json
import re

logger = logging.getLogger(__name__)


class TestKeywordReplacer(unittest.TestCase):
    def setUp(self):
        logger.info("Starting...")

    def tearDown(self):
        logger.info("Ending.")

    def test_fuzzy_extract_deletion(self):
        """
        Fuzzy deletion
        """
        keyword_proc = KeywordProcessor()
        for keyword in (('skype', 'messenger'), ):
            keyword_proc.add_keyword(*keyword)

        sentence = "hello, do you have skpe ?"
        extracted_keywords = [('messenger', 19, 23)]
        #self.assertEqual(keyword_proc.extract_keywords(sentence, span_info=True, max_cost=1), extracted_keywords)


    def test_extract_addition(self):
        """
        Fuzzy addition
        """
        keyword_proc = KeywordProcessor()
        for keyword in (('colour here', 'couleur ici'), ('and heere', 'et ici')):
            keyword_proc.add_keyword(*keyword)

        sentence = "color here blabla and here"

        extracted_keywords = [('couleur ici', 0, 10), ('et ici', 18, 26)]
        self.assertListEqual(keyword_proc.extract_keywords(sentence, span_info=True, max_cost=1), extracted_keywords)


    def test_correct_keyword_addition(self):
        keyword_proc = KeywordProcessor()
        for keyword in (('colour here', 'couleur ici'), ('and heere', 'et ici')):
            keyword_proc.add_keyword(*keyword)

        current_dict = keyword_proc.keyword_trie_dict['c']['o']['l']['o']
        closest_node, cost, depth = next(
            keyword_proc._correct_word('r', max_cost=1, start_node=current_dict),
            ({}, 0, 0)
            )
        self.assertDictEqual(closest_node, current_dict['u']['r'])
        self.assertEqual(cost, 1)
        self.assertEqual(depth, 2)

        #import ipdb; ipdb.set_trace()
        current_dict_continued = {'e' : {'e': {'r': {'e': {'_keyword_': 'et ici'}}}}}
        closest_node, cost, depth = next(
            keyword_proc._correct_word('ere', max_cost=1, start_node=current_dict_continued),
            ({}, 0, 0)
        )
        self.assertDictEqual(closest_node, current_dict_continued['e']['e']['r']['e'])
        self.assertEqual(cost, 1)
        self.assertEqual(depth, 4)


if __name__ == '__main__':
    unittest.main()