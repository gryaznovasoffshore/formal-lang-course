import cfpq_data
import networkx as nx

from dataclasses import dataclass
from typing import *

@dataclass
class Graph:
    nodes: int
    edges: int
    labels: Set[str]

def load_graph(graph_name: str):
    graph_csv = cfpq_data.download(graph_name)
    graph = cfpq_data.graph_from_csv(graph_csv)

    return graph

def get_graph_info(graph_name: str) -> Graph:
    graph = load_graph(graph_name)

    nodes = graph.number_of_nodes()
    edges = graph.number_of_edges()
    labels = cfpq_data.get_sorted_labels(graph)

    return Graph(
        nodes,
        edges,
        labels,
    )

def execute_graph(
    first_cycle: int,
    second_cycle: int,
    labels: Tuple[str, str],
    path: str,
):
    graph = cfpq_data.labeled_two_cycles_graph(
        first_cycle = first_cycle,
        second_cycle = second_cycle,
        labels = labels,
    )

    graph_dot = nx.nx_pydot.to_pydot(graph)
    graph_dot.write(path)