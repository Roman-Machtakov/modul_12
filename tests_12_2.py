import unittest
from .runner_and_tournament import Runner, Tournament



class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        self.all_results.update(tournament.start())
        self.assertTrue("Ник" in self.all_results.values())

    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        self.all_results.update(tournament.start())
        self.assertTrue("Ник" in self.all_results.values())

    def test_usain_andrey_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        self.all_results.update(tournament.start())
        self.assertTrue("Ник" in self.all_results.values())

if __name__ == "__main__":
    unittest.main()