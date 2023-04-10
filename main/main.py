from src import algorithm


def main():
    distances = algorithm.run()
    print(f"Shortest distance found {distances[-1]}")


if __name__ == "__main__":
    main()
