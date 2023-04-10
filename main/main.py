from src import algorithm


def main():
    distances, chromosomes = algorithm.run()
    print(f"Shortest distance found {distances[-1]}")
    print(f"Best chromosomes found {chromosomes[-1]}")


if __name__ == "__main__":
    main()
