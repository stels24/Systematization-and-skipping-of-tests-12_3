import unittest
import runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_0 = runner.Runner('Mikhail')
        for i in range(10):
            runner_0.walk()
        self.assertEqual(runner_0.distance, 50)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_1 = runner.Runner('Hasan')
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_2 = runner.Runner('Nik')
        runner_3 = runner.Runner('Svyt')
        for i in range(10):
            runner_2.walk()
            runner_3.run()
        self.assertNotEqual(runner_2.distance, runner_3.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_first(self):
        first_run = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_second(self):
        second_run = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_third(self):
        third_run = runner_and_tournament.Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()