import unittest
import utils

class DataCheckTest(unittest.TestCase):
    def testCorrect(self):
        fields = ['id', 'name']
        scenario = {
            'id': 0,
            'name': "blabla"
        }
        self.assertTrue(
            utils.checkData(scenario, fields)
        )
    
    def testBrokenScenario(self):
        fields = ['id', 'name']
        scenario = {
            "name": "blabla"
        }
        self.assertFalse(
            utils.checkData(scenario, fields)
        )

if __name__ == '__main__':
    unittest.main()