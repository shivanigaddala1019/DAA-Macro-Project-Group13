import matplotlib.pyplot as plt


def build_tree(arr, x, y, spacing, positions, edges):
    """Build the recursion tree by dividing the array."""

    node = (x, y, str(arr))
    positions.append(node)

    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        left_x = x - spacing
        right_x = x + spacing
        child_y = y - 1

        left_node = (left_x, child_y, str(left))
        right_node = (right_x, child_y, str(right))

        edges.append((node, left_node))
        edges.append((node, right_node))

        build_tree(left, left_x, child_y,
                   spacing / 2, positions, edges)

        build_tree(right, right_x, child_y,
                   spacing / 2, positions, edges)


def draw_tree():
    arr = [8, 4, 6, 2, 7, 3, 1, 5]

    positions = []
    edges = []

    build_tree(arr, 0, 3, 4, positions, edges)

    fig, ax = plt.subplots(figsize=(16, 9))

    # Draw connections between parent and child nodes.
    for parent, child in edges:
        ax.plot(
            [parent[0], child[0]],
            [parent[1], child[1]],
            linewidth=1.5
        )

    # Draw the array labels.
    for x, y, label in positions:
        ax.text(
            x, y, label,
            ha="center",
            va="center",
            fontsize=9,
            bbox=dict(boxstyle="round,pad=0.5")
        )

    ax.set_title(
        "Merge Sort Recursion Tree",
        fontsize=18
    )

    ax.axis("off")
    plt.tight_layout()

    plt.savefig(
        "Unit1_AlgorithmAnalysis/Visualization.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


if __name__ == "__main__":
    draw_tree()