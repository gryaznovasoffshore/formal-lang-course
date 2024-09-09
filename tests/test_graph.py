import pytest
import cfpq_data
import networkx as nx

from project.graph import get_graph_info, execute_graph, Graph

available_name = cfpq_data.DATASET

@pytest.mark.parametrize("graph_name", available_name[:3])
def test_get_graph_info(graph_name):
    actual_graph = get_graph_info(graph_name)

    graph = cfpq_data.graph_from_csv(cfpq_data.download(graph_name))
    expected_graph = Graph(
        nodes=graph.number_of_nodes(),
        edges=graph.number_of_edges(),
        labels=cfpq_data.get_sorted_labels(graph),
    )

    assert actual_graph == expected_graph


@pytest.mark.parametrize(
    [
        "first_cycle",
        "second_cycle",
        "labels",
        "expected_graph_path",
    ],
    [
        (3, 2, ("a", "b"), "tests/test_data/graph_tests/first_graph.dot"),
        (4, 4, ("label=test_m_1", "label=test_m_2"), "tests/test_data/graph_tests/second_graph.dot"),
    ],
)
def test_execute_graph(
    tmp_path,
    labels,
    expected_graph_path,
    first_cycle,
    second_cycle,
):
    actual_path = tmp_path / "tmp_graph.dot"
    execute_graph(
        first_cycle, second_cycle, labels, str(actual_path)
    )

    actual_graph = nx.nx_pydot.read_dot(actual_path)
    expected_graph = nx.nx_pydot.read_dot(expected_graph_path)

    assert nx.utils.graphs_equal(expected_graph, actual_graph)