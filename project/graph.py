import cfpq_data
import networkx as nx

from typing import *
from dataclasses import dataclass

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
) -> nx.MultiDiGraph:
    graph = cfpq_data.labeled_two_cycles_graph(
        first_cycle,
        second_cycle,
        labels = labels,
    )
    if path:
        save_graph(graph, path)

    return graph


def save_graph(graph: nx.MultiDiGraph, dot_path: str) -> None:
    nx.nx_pydot.write_dot(graph, dot_path)