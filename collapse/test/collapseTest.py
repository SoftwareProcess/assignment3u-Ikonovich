from unittest import TestCase
import collapse.collapse as c

class CollapseTest(TestCase):

    # 100 collapse
    #    Desired level of confidence:    boundary value analysis
    #    Input-output Analysis
    #      inputs: value -> numeric; .GE. 0 and .LT. 100; mandatory, unvalidated
    #      outputs: 
    #         normal:  single digit string
    #         abnormal: None
    #         side effects:  none
    
    
    #  Sample happy path test -- replace with your own
    def testSingleDigitInput(self):
        value = '7'
        expectedResult = '7'
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def testMultiDigitInput(self):
        value = '7359247210'
        expectedResult = '4'
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    #  Sad path test -- Non-numeric input
    def testNonNumericInput(self):
        value = 'a'
        expectedResult = None
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    #Sad path test -- Negative input value
    def testNegativeInput(self):
        value = '-1'
        expectedResult = None
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)   
    
    #Sad path test -- input over 50 digits
    def testFiftyOneDigitInput(self):
        value = '354122460412069184449688835653388948582633418359859'
        expectedResult = None
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    #  Sad path test -- missing input
    def testMissingInput(self):
        value = None
        expectedResult = None
        actualResult = c.collapse()
        self.assertEqual(expectedResult, actualResult)
        
            #  Sad path test -- Input is 'None'
    def testNoneInput(self):
        value = None
        expectedResult = None
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    
