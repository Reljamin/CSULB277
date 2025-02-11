import unittest
from cecs328pa1 import asymptotic_analysis

class TestAsymptoticAnalysis(unittest.TestCase):
    def test_exponential_growth(self):
        self.assertTrue(asymptotic_analysis("2**n", "3**n", "O"))  # True
        self.assertFalse(asymptotic_analysis("3**n", "2**n", "O"))  # False
        self.assertTrue(asymptotic_analysis("2**n", "2**n", "Θ"))  # True

    def test_logarithmic_vs_polynomial(self):
        self.assertTrue(asymptotic_analysis("log(n)", "n", "O"))  # True
        self.assertFalse(asymptotic_analysis("n", "log(n)", "O"))  # False
        self.assertTrue(asymptotic_analysis("log(n)**2", "log(n)", "Ω"))  # True

    def test_mixed_functions(self):
        self.assertTrue(asymptotic_analysis("n*log(n)", "n**2", "O"))  # True
        self.assertTrue(asymptotic_analysis("n*log(n)", "n*log(n)", "Θ"))  # True
        self.assertTrue(asymptotic_analysis("n**2 + n*log(n)", "n**2", "O"))  # True

    def test_dominant_term_importance(self):
        self.assertTrue(asymptotic_analysis("n**2 + n", "n**2", "O"))  # True
        self.assertTrue(asymptotic_analysis("n**2 + n", "n**2", "Θ"))  # True
        self.assertTrue(asymptotic_analysis("n**2 + n", "n**2", "Ω"))  # True
        self.assertFalse(asymptotic_analysis("n**2 + n", "n", "O"))  # False

    def test_proffessor_test_cases(self):
        self.assertFalse(asymptotic_analysis("log(n)**2", "lg(n**3)", "O"))  # False
        self.assertFalse(asymptotic_analysis("2*n**2 + n*log(n) + 5", "n**2", "Θ"))  # True
        self.assertTrue(asymptotic_analysis("n**2 + n + 5", "n*(log(n))**2", "Ω"))  # True


if __name__ == "__main__":
    unittest.main()
