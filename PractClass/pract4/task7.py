from pathlib import Path


def load_csv(filename):
    text = Path(filename).read_text().strip()
    rows = []
    for line in text.split('\n')[1:]:
        rows.append(line.split(';'))
    return rows


class Cluster:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def jaccard_dist(row1, row2):
    pass  # TODO


def cluster_dist(func, data1, data2):
    pass  # TODO


def hclust(rows):
    clusters = [Cluster([row]) for row in rows]
    while len(clusters) > 1:
        pass  # TODO
    return clusters[0]


def gen_dot(cluster, min_dist):
    pass  # TODO


rows = load_csv('data/langs.csv')
cluster = hclust(rows)
print(gen_dot(cluster, 0.5))
