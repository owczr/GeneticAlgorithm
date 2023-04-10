import matplotlib.pyplot as plt

from src import algorithm
import src.plots as plots
from src.utils import X_LIM, Y_LIM


def main():
    distances, chromosomes, points = algorithm.run()

    # Create figure and axes
    fig, axs, axbig = plots.create_fig_and_axs()

    # Plot first chromosomes
    plots.points(axs[0][0], X_LIM, Y_LIM, points, "First iteration")
    plots.lines(axs[0][0], chromosomes[0], points)

    # Plot middle chromosomes
    plots.points(axs[0][1], X_LIM, Y_LIM, points, "Middle iteration")
    plots.lines(axs[0][1], chromosomes[len(chromosomes) // 2], points)

    # Plot last chromosomes
    plots.points(axs[0][2], X_LIM, Y_LIM, points, "Last iteration")
    plots.lines(axs[0][2], chromosomes[-1], points)

    # Plot decreasing distances
    plots.distances(axbig, distances)

    plt.show()


if __name__ == "__main__":
    main()
