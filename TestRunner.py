import unittest

from Tests.TestAccount import test_user_pass
from Tests.TestAttuatori import test_pompa
from Tests.TestAttuatori import test_CO2
from Tests.TestAttuatori import test_temp_reg
from Tests.TestAttuatori import test_umid

def runSuite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_user_pass))
    suite.addTests(loader.loadTestsFromModule(test_CO2))
    suite.addTests(loader.loadTestsFromModule(test_temp_reg))
    suite.addTests(loader.loadTestsFromModule(test_umid))
    suite.addTests(loader.loadTestsFromModule(test_pompa))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    runSuite()
