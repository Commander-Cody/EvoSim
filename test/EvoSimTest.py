import unittest
from TestUtil.TestCaseExtension import TestCaseExtension
from EvoSim import main


class EvoSimTest(TestCaseExtension):
    def test_main_function_runs_without_errors(self):
        self.assertNoExceptionThrown(main)


if __name__ == '__main__':
    unittest.main()
