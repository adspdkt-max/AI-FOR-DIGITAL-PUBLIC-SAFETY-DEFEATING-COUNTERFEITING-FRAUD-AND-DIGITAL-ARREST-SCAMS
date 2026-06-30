import networkx as nx

def build_fraud_network():

    G = nx.Graph()

    # Scammers
    G.add_node("Scammer_A", type="scammer")
    G.add_node("Scammer_B", type="scammer")

    # Victims
    G.add_node("Victim_1", type="victim")
    G.add_node("Victim_2", type="victim")
    G.add_node("Victim_3", type="victim")
    G.add_node("Victim_4", type="victim")

    # Connections
    G.add_edge("Scammer_A", "Victim_1")
    G.add_edge("Scammer_A", "Victim_2")
    G.add_edge("Scammer_A", "Victim_3")

    G.add_edge("Scammer_B", "Victim_3")
    G.add_edge("Scammer_B", "Victim_4")

    return G


def analyze_network():

    G = build_fraud_network()

    centrality = nx.degree_centrality(G)

    top_suspect = max(centrality, key=centrality.get)

    return {
        "total_nodes": G.number_of_nodes(),
        "total_connections": G.number_of_edges(),
        "top_suspect": top_suspect,
        "centrality_scores": centrality
    }
