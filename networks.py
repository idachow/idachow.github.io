from sklearn.metrics import jaccard_similarity_score
import itertools as it

def ideas_to_network(ideas_bow, nodes):
    """Given a set of ideas in bag of words (stems) form and a vocabulary set of stem nodes, 
    compute edge weights between all possible stem pairs
    where edge weights are given by the Jaccard index
    Store as numpy matrix?
    """

    edge_weights = [] # to store the edge weights
    edges = [] # for keeping track of edges we've seen

    # for all possible pairs of nodes
    for A, B in it.combinations(nodes, 2):
        # if we haven't seen the pair already
        if not [A, B] in edges and not [B, A] in edges:
            # check the jaccard sim and add to edge weights if it's nonzero
            weight = compute_edge(A, B, ideas_bow)
            if weight > 0:
                edge_weights.append({'pair': [A, B], 'pair_r': [B, A], 'weight': weight})

    return pd.DataFrame(edge_weights);

def in_ideas(node, ideas_bow):
    """Find set of ideas that contain the node
    """
    containers = set()
    for index, row in ideas_bow.iterrows():
        if node in row['stems']:
            containers.add(row['id'])
    return containers

def compute_edge(A, B, ideas_bow):
    """Compute edge between a pair of nodes (stems) A and B using Jaccard index
    """

    # Find SA - set of ideas that contain A
    SA = in_ideas(A, ideas_bow)
    # Find SB - set of ideas that contain B
    SB = in_ideas(B, ideas_bow)

    # jaccard is ratio of intersection(SA, SB) to union(SA, SB)
    return jaccard_similarity_score(SA, SB)