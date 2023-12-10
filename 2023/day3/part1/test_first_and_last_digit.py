import unittest
from solution import *

class TestDigitFuncs(unittest.TestCase):
    line = '607.............123.....................508..........*892................+..=138.381..967...............*....%......926...........218....712'

    def test_firstDigit(self):
        self.assertEqual(firstDigit(self.line, 7), -1)
        
        # start of self.line '607.......'
        self.assertEqual(firstDigit(self.line, 0),  0) # char at charpos 6
        self.assertEqual(firstDigit(self.line, 1),  0) # char at charpos 0
        self.assertEqual(firstDigit(self.line, 2),  0) # char at charpos 7

        # end of self.line '.......712'
        self.assertEqual(firstDigit(self.line, 139),  137)  # char at charpos 7
        self.assertEqual(firstDigit(self.line, 138),  137)  # char at charpos 1
        self.assertEqual(firstDigit(self.line, 137),  137)  # char at charpos 2

        """
        numbers between start and end of self.line = '....+..=138.381..967....'
        """

        # '....+..=138.381..967....'
        #          ^
        #          |
        #        charPos = 77            
        self.assertEqual(firstDigit(self.line, 77),  77)  # char at charpos 1
        self.assertEqual(firstDigit(self.line, 78),  77)  # char at charpos 3
        self.assertEqual(firstDigit(self.line, 79),  77)  # char at charpos 8

        # '....+..=138.381..967....'
        #              ^
        #              |
        #          charPos = 81            
        self.assertEqual(firstDigit(self.line, 81),  81)  # char at charpos 3
        self.assertEqual(firstDigit(self.line, 82),  81)  # char at charpos 8
        self.assertEqual(firstDigit(self.line, 83),  81)  # char at charpos 1

        # '....+..=138.381..967....'
        #                   ^
        #                   |
        #                 charPos = 86            
        self.assertEqual(firstDigit(self.line, 86),  86)  # char at charpos 9
        self.assertEqual(firstDigit(self.line, 87),  86)  # char at charpos 6
        self.assertEqual(firstDigit(self.line, 88),  86)  # char at charpos 7
    
    def test_lastDigit(self):
        self.assertEqual(lastDigit(self.line, 7), -1)
        
        # start of self.line '607.......'
        self.assertEqual(lastDigit(self.line, 0),  2) # char at charpos 6
        self.assertEqual(lastDigit(self.line, 1),  2) # char at charpos 0
        self.assertEqual(lastDigit(self.line, 2),  2) # char at charpos 7

        # end of self.line '.......712'
        self.assertEqual(lastDigit(self.line, 139),  139)  # char at charpos 7
        self.assertEqual(lastDigit(self.line, 138),  139)  # char at charpos 1
        self.assertEqual(lastDigit(self.line, 137),  139)  # char at charpos 2

        """
        numbers between start and end of self.line = '....+..=138.381..967....'
        """

        # '....+..=138.381..967....'
        #          ^
        #          |
        #        charPos = 77            
        self.assertEqual(lastDigit(self.line, 77),  79)  # char at charpos 1
        self.assertEqual(lastDigit(self.line, 78),  79)  # char at charpos 3
        self.assertEqual(lastDigit(self.line, 79),  79)  # char at charpos 8

        # '....+..=138.381..967....'
        #              ^
        #              |
        #          charPos = 81            
        self.assertEqual(lastDigit(self.line, 81),  83)  # char at charpos 3
        self.assertEqual(lastDigit(self.line, 82),  83)  # char at charpos 8
        self.assertEqual(lastDigit(self.line, 83),  83)  # char at charpos 1

        # '....+..=138.381..967....'
        #                   ^
        #                   |
        #                 charPos = 86            
        self.assertEqual(lastDigit(self.line, 86),  88)  # char at charpos 9
        self.assertEqual(lastDigit(self.line, 87),  88)  # char at charpos 6
        self.assertEqual(lastDigit(self.line, 88),  88)  # char at charpos 7
    
    




if __name__ == '__main__':
    unittest.main()