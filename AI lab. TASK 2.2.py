class BudgetAnalyzer:
    def __init__(self, movies):
        self.movies = movies
    def average_budget(self):
        return sum(b for _, b in self.movies) / len(self.movies)

    def high_budget(self):
        average= self.average_budget()
        return [(n, b, b - average) for n, b in self.movies if b > average], average

    def show_results(self):
        high_budget, average = self.high_budget()
        print(f"\nAverage Budget: ${average:,.2f}\n")
        print("Movies are above average:")
        for n, b, d in high_budget:
            print(f"{n}: ${b:,.2f} (+${d:,.2f})")
        print(f"\nTotal above average: {len(high_budget)}")

    def add_movies(self):
        for _ in range(int(input("How many movies? "))):
            self.movies.append((input("Movie: "), int(input("Budget: "))))

movies = [
    ("Wednesday Adam", 2000000),
    ("Alice in Borderland", 10000000),
    ("Squid Game", 5000000),
    ("All Of Are Us Dead", 809000000),
    ("True Beauty", 805000000),
    ("Queen Of Tears", 786000000),
]

analyzer = BudgetAnalyzer(movies)
analyzer.add_movies()
analyzer.show_results()
