import unittest


class TestCaseExtension(unittest.TestCase):
    def assertNoExceptionThrown(self, function):
        try:
            function()
        except Exception as e:
            self.fail("Expected function " + function.__name__ + " to not throw an exception but got " + e.__class__.__name__)
