import unittest
import test_12_3_sistem


runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3_sistem.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3_sistem.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)