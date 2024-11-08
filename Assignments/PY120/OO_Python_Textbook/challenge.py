
class Candidate:


    def __init__(self,name:str):
        if not isinstance(name, str):
            raise TypeError('Candidate name must be a string')
        self.name = name
        self._votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.votes += other
        return self

    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, count):
        self._votes = count



class Election:

    def __init__(self, cnds):
        if not isinstance(cnds, set):
            raise TypeError('The candidates must be a set of at least one candidate')
        if not all([isinstance(cnd, Candidate) for cnd in cnds]):
            raise TypeError('Candidates must contain only objects of type Candidates')
        self.candidates = cnds

    def results(self):
        winner = None
        total_votes = 0
        for cnd in self.candidates:
            total_votes += cnd.votes
            if not winner or cnd.votes > winner.votes:
                winner = cnd
            print(f'{cnd.name}: {cnd.votes}')

        print(f'\n{winner.name} won: {(winner.votes / total_votes) * 100}% of votes')


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()