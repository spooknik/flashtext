from flashtext import KeywordProcessor
import logging
import unittest
import json

logger = logging.getLogger(__name__)


class TestDictionaryLoad(unittest.TestCase):
    def setUp(self):
        logger.info("Starting...")

    def tearDown(self):
        logger.info("Ending.")

    def test_closest(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keyword('Hello')
        keyword_processor.add_keyword('skype', 'videocall')

        #closest = keyword_processor.get_closest_keyword('skpe')
        #self.assertEqual(closest, ('videocall', 1))

        

if __name__ == '__main__':
    unittest.main()