import pytest
from src.rts_resource_manager import ResourceManager, Node

def test_create_resource_manager():
    rts = ResourceManager()
    assert rts.graph.number_of_nodes() == 0
    assert len(rts.nodes) == 0
    assert rts.canvas == None
    assert rts.pos == None

def test_create_node():
    node = Node('node test')
    assert node.name == 'node test'
    assert node.usable == True
    assert len(node.dependencies) == 0

def test_load_resources_loads_all_nodes_correctly():
    rts = ResourceManager()
    rts.load_resources('tests/resources_test.txt')
    assert rts.graph.number_of_nodes() == 6
    assert len(rts.nodes) == 6
    assert rts.graph.has_node('handgun')
    assert rts.graph.has_node('bullets')
    assert rts.graph.has_node('ore')
    assert rts.graph.has_node('turret')
    assert rts.graph.has_node('bombs')
    assert rts.graph.has_node('pistol')
    assert 'handgun' in rts.nodes
    assert 'bullets' in rts.nodes
    assert 'ore' in rts.nodes
    assert 'turret' in rts.nodes
    assert 'bombs' in rts.nodes
    assert 'pistol' in rts.nodes

def test_load_resources_loads_all_edges_correctly():
    rts = ResourceManager()
    rts.load_resources('tests/resources_test.txt')
    assert rts.graph.number_of_edges() == 5
    assert rts.graph.has_edge('handgun', 'bullets')
    assert rts.graph.has_edge('bullets', 'ore')
    assert rts.graph.has_edge('bombs', 'ore')
    assert rts.graph.has_edge('turret', 'bullets')
    assert rts.graph.has_edge('pistol', 'bullets')
    assert 'bullets' in rts.nodes['handgun'].dependencies
    assert 'ore' in rts.nodes['bullets'].dependencies
    assert 'ore' in rts.nodes['bombs'].dependencies
    assert 'bullets' in rts.nodes['turret'].dependencies
    assert 'bullets' in rts.nodes['pistol'].dependencies

def test_load_resources_raise_value_error_on_invalid_format():
    rts = ResourceManager()
    with pytest.raises(ValueError):
        rts.load_resources('tests/invalid_format.txt')

def test_delete_node():
    rts = ResourceManager()
    rts.load_resources('tests/resources_test.txt')
    rts.delete_node('bullets')
    assert 'bullets' not in rts.nodes

def test_add_node():
    rts = ResourceManager()
    rts.load_resources('tests/resources_test.txt')
    rts.add_node('plane')
    assert 'plane' in rts.nodes

def test_add_link():
    rts = ResourceManager()
    rts.load_resources('tests/resources_test.txt')
    rts.add_link('start_node_test', 'end_node_test')
    assert rts.graph.has_edge('start_node_test', 'end_node_test')
def test_print_graph(capsys):
    rts = ResourceManager()
    rts.load_resources('tests/resources_test.txt')
    rts.print_graph()
    print_output = capsys.readouterr()
    assert print_output.out == "Resources graph:\nhandgun  ->  ['bullets']\nbullets  ->  ['ore']\nore  ->  []\nbombs  ->  ['ore']\nturret  ->  ['bullets']\npistol  ->  ['bullets']\n"
