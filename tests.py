import unittest

from collections import Counter

from probability_task import RandomGen


class TestRandomGenerator(unittest.TestCase):

    def test_number_with_0_probabilty(self):
        random_generator = RandomGen(
            random_nums=[1, 2], probabilities=[0, 1]
        )

        sample = 10
        numbers = [random_generator.next_num() for i in range(sample)]
        number_count = Counter(numbers)
        self.assertEqual(sample, number_count[2])
        self.assertTrue(1 not in number_count)

    def test_numbers_with_distant_probabilty(self):
        random_generator = RandomGen(
            random_nums=[1, 2], probabilities=[0.1, 0.9]
        )
        sample = 20
        numbers = [random_generator.next_num() for _ in range(sample)]
        number_count = Counter(numbers)
        self.assertTrue(number_count[2] > number_count[1])

    def test_number_with_largest_probability(self):
        random_generator = RandomGen(
            random_nums=[1, 2, 3, 4], probabilities=[0.1, 0.1, 0.1, 0.7]
        )
        sample = 20
        numbers = [random_generator.next_num() for _ in range(sample)]
        number_count = Counter(numbers)
        most_common = number_count.most_common(1)[0][0]
        self.assertEqual(most_common, 4)

    def test_number_with_smallest_probability(self):
        random_generator = RandomGen(
            random_nums=[1, 2], probabilities=[0.1, 0.9]
        )
        sample = 20
        numbers = [random_generator.next_num() for _ in range(sample)]
        number_count = Counter(numbers)

        # "1" might not be generated
        if 1 in number_count:
            least_common = number_count.most_common()[-1][0]
            self.assertEqual(least_common, 1)

    def test_bad_probabilities(self):
        with self.assertRaises(AssertionError):
            RandomGen(
                random_nums=[1, 2], probabilities=[1, 1]
            )

    def test_non_equal_input(self):
        with self.assertRaises(AssertionError):
            RandomGen(
                random_nums=[1, 2, 3], probabilities=[0.5, 0.5]
            )


if __name__ == '__main__':
    unittest.main()
