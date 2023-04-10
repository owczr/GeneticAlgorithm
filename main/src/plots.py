import matplotlib.pyplot as plt


def create_fig_and_axs():
    fig, axs = plt.subplots(2, 3, figsize=(30, 20))
    gs = axs[1, 0].get_gridspec()
    axs[1, 2].remove()
    axs[1, 1].remove()
    axs[1, 0].remove()
    axbig = fig.add_subplot(gs[1, 0:])
    axbig.tick_params(axis='y', which='both', bottom=False, top=False, labelbottom=False)
    fig.tight_layout()

    return fig, axs, axbig


def points(ax, x_lim, y_lim, points, title):
    ax.set_xlim(*x_lim)
    ax.set_ylim(*y_lim)
    x, y = zip(*points)
    ax.scatter(x, y)
    ax.set_title(title)


def lines(ax, chromosomes, points):
    for first, second in zip(chromosomes[:-1], chromosomes[1:]):
        x1, y1 = points[first]
        x2, y2 = points[second]
        ax.plot([x1, x2], [y1, y2], 'k-')
    x1, y1 = points[-1]
    x2, y2 = points[0]
    ax.plot([x1, x2], [y1, y2], 'k-')


def distances(ax, distances):
    ax.plot(distances)
    ax.set_title("Decreasing distance in each iteration")
    ax.set_ylabel("Distance")
    ax.set_xlabel("Iteration")

