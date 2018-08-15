import random


class RandomGenException(Exception):
    pass


class RandomGen:
    sample_set = None

    def __init__(self, random_nums, probabilities):

        assert len(random_nums) == len(probabilities), "Lists must be of equal size"
        assert sum(probabilities) == 1, "List of probabilities must equal 1"

        self.sample_set = [(0, None)]
        for idx, (p, n) in enumerate(zip(probabilities, random_nums)):
            upper_bound = self.sample_set[idx][0] + p
            self.sample_set.append((upper_bound, n))

    def next_num(self):
        u = random.random()
        for idx, (p, n) in enumerate(self.sample_set):
            _p = self.sample_set[idx - 1][0]
            if _p <= u <= p:
                return n

        raise RandomGenException

    def _alias(self):
        """A more efficient method discussed here http://keithschwarz.com/darts-dice-coins/"""
