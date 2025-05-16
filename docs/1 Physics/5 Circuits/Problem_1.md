# Problem 1

## **Equivalent Resistance Calculation Using Graph Theory**

## **Introduction**

Calculating the equivalent resistance of a circuit is a fundamental problem in electrical engineering. Traditional methods, which involve iteratively applying series and parallel resistor rules, can become complex and cumbersome for intricate circuits. Graph theory offers a powerful and systematic alternative by representing a circuit as a graph, where nodes are junctions and edges are resistors. This approach not only simplifies calculations but also provides a deeper understanding of circuit analysis.

---

## **Theory**

### **Traditional Methods vs. Graph Theory**
- **Traditional Methods**: Iteratively applying series and parallel resistor rules.
- **Graph Theory**: Representing a circuit as a graph simplifies complex networks.

### **Benefits of Using Graph Theory**
1. **Systematic Approach**: Provides a structured way to analyze circuits.
2. **Simplification**: Simplifies complex networks into manageable graphs.
3. **Automation**: Enables automated circuit analysis, useful in simulation software.
4. **Versatility**: Highlights the interplay between electrical and mathematical concepts.

---

## **Task: Implementing Equivalent Resistance Calculation Using Graph Theory**

### **Algorithm Description**

The algorithm for calculating equivalent resistance using graph theory involves the following steps:

1. **Graph Representation**:
   - Represent the circuit as a graph where:
     - Nodes: Junctions in the circuit.
     - Edges: Resistors connecting the junctions.
     - Edge Weights: Resistance values of the resistors.

2. **Iterative Simplification**:
   - Iteratively reduce the graph by identifying and simplifying series and parallel connections.

3. **Series Reduction**:
   - Identify series connections (linear chains of resistors).
   - Replace each series connection with a single equivalent resistor by summing their resistance values.

4. **Parallel Reduction**:
   - Identify parallel connections (resistors connected between the same two nodes).
   - Replace each parallel connection with a single equivalent resistor using the formula:
     $$
     R_{\text{eq}} = \left( \sum_{i=1}^{n} \frac{1}{R_i} \right)^{-1}
     $$

5. **Termination**:
   - Repeat steps 3 and 4 until the graph is reduced to a single equivalent resistance between the input and output nodes.



### **Python Implementation**

```python

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def calculate_equivalent_resistance(graph, input_node, output_node):
    """
    Calculate the equivalent resistance of a circuit represented as a graph.

    Parameters:
    - graph (nx.Graph): A networkx graph representing the circuit.
      Nodes are junctions, and edges are resistors with 'resistance' attribute.
    - input_node (str): The starting node for resistance calculation.
    - output_node (str): The ending node for resistance calculation.

    Returns:
    - float: The equivalent resistance between the input and output nodes.
    """
    graph = graph.copy()  # Operate on a copy to avoid modifying the original graph

    while len(graph.nodes) > 2:
        # Series Reduction
        for node in list(graph.nodes):  # Iterate over a copy of the nodes
            if graph.degree(node) == 2:
                edges = list(graph.edges(node, data=True))
                if len(edges) == 2:
                    node1, node2, data1 = edges[0][0], edges[0][1], edges[0][2]
                    node3, node4, data2 = edges[1][0], edges[1][1], edges[1][2]

                    r1 = data1['resistance']
                    r2 = data2['resistance']
                    R_eq = r1 + r2

                    # Remove the series connection
                    graph.remove_node(node)

                    # Add the equivalent resistor
                    new_node1 = node1 if node1 != node else node3
                    new_node2 = node2 if node2 != node else node4
                    graph.add_edge(new_node1, new_node2, resistance=R_eq)
                break  # Break to restart the loop after modification

        # Parallel Reduction
        for node1 in list(graph.nodes):
            for node2 in list(graph.nodes):
                if node1 != node2 and graph.has_edge(node1, node2):
                    edges_between = [(u, v, data) for u, v, data in graph.edges(data=True)
                                     if ((u == node1 and v == node2) or (u == node2 and v == node1))]
                    
                    if len(edges_between) > 1:
                        R_eq = (sum(1 / data['resistance'] for u, v, data in edges_between))**(-1)

                        # Remove parallel resistors
                        edges_to_remove = [(u, v) for u, v, data in edges_between]
                        for u, v in edges_to_remove:
                            graph.remove_edge(u, v)

                        # Add the equivalent resistor
                        graph.add_edge(node1, node2, resistance=R_eq)
                break  # Break to restart the loop after modification

    # Return the final equivalent resistance
    for u, v, data in graph.edges(data=True):
        return data['resistance']
    return 0  # If no resistance is found

def visualize_circuit(graph, title="Circuit Diagram", pos=None):
    """
    Visualizes the circuit graph using matplotlib.
    """
    if pos is None:
        pos = nx.spring_layout(graph)  # You can use other layout algorithms

    plt.figure(figsize=(10, 8))  # Adjust figure size for better visualization
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12, font_weight='bold',
            edgecolors='gray', linewidths=0.5)  # Added edgecolors for better node visibility
    edge_labels = nx.get_edge_attributes(graph, 'resistance')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, bbox=dict(alpha=0.7, edgecolor="none"))  # Added bbox for label readability
    plt.title(title, fontsize=16)  # Increased title font size
    plt.box(False)  # Remove the surrounding box
    plt.show()
    return pos  # Return the layout for consistent visualization

def simulate_circuit(graph, input_node, output_node, voltage_source):
    

    # Create the admittance matrix and source vector
    num_nodes = len(graph.nodes)
    node_index = {node: i for i, node in enumerate(graph.nodes)}
    Y = np.zeros((num_nodes, num_nodes))
    I = np.zeros(num_nodes)

    # Fill the admittance matrix
    for u, v, data in graph.edges(data=True):
        r = data['resistance']
        g = 1 / r  # Conductance
        i = node_index[u]
        j = node_index[v]

        Y[i, i] += g
        Y[j, j] += g
        Y[i, j] -= g
        Y[j, i] -= g

    # Add the voltage source
    input_index = node_index[input_node]
    output_index = node_index[output_node]
    Y[input_index, :] = 0
    Y[output_index, :] = 0
    Y[input_index, input_index] = 1
    Y[output_index, output_index] = 1
    I[input_index] = voltage_source
    I[output_index] = 0

    # Solve for node voltages
    try:
        V = np.linalg.solve(Y, I)
    except np.linalg.LinAlgError:
        print("Singular matrix! Check your circuit configuration.")
        return None

    node_voltages = {node: V[i] for node, i in node_index.items()}

    # Calculate edge currents
    edge_currents = {}
    for u, v, data in graph.edges(data=True):
        r = data['resistance']
        V_u = node_voltages[u]
        V_v = node_voltages[v]
        I_uv = (V_u - V_v) / r
        edge_currents[(u, v)] = I_uv

    return node_voltages, edge_currents

def display_simulation_results(graph, node_voltages, edge_currents, pos):
    
    if node_voltages is None:
        return

    plt.figure(figsize=(12, 10))
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12, font_weight='bold',
            edgecolors='gray', linewidths=0.5)

    # Display resistance values
    edge_labels_resistance = nx.get_edge_attributes(graph, 'resistance')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels_resistance, font_size=8,
                                bbox=dict(alpha=0.7, edgecolor="none"))

    # Display voltage values
    node_labels_voltage = {node: f"{voltage:.2f}V" for node, voltage in node_voltages.items()}
    nx.draw_networkx_labels(graph, pos, labels=node_labels_voltage, font_size=8, font_color='green',
                            bbox=dict(alpha=0.7, edgecolor="none"))

    # Display current values
    edge_labels_current = {edge: f"{current:.2f}A" for edge, current in edge_currents.items()}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels_current, font_size=8, font_color='red',
                                bbox=dict(alpha=0.7, edgecolor="none"), label_pos=0.7)  # Adjust label_pos for better placement

    plt.title("Circuit Simulation Results", fontsize=16)
    plt.box(False)
    plt.show()

# Example 1: Simple Series and Parallel Combination
graph1 = nx.Graph()
graph1.add_edge('A', 'B', resistance=10)
graph1.add_edge('B', 'C', resistance=20)
graph1.add_edge('A', 'C', resistance=30)
pos1 = visualize_circuit(graph1, title="Example 1: Simple Series and Parallel")
R_eq1 = calculate_equivalent_resistance(graph1, 'A', 'C')
print(f"Equivalent Resistance for Example 1: {R_eq1:.2f} ohms")
node_voltages1, edge_currents1 = simulate_circuit(graph1, 'A', 'C', 12)
if node_voltages1:
    display_simulation_results(graph1, node_voltages1, edge_currents1, pos1)

# Example 2: Nested Configuration
graph2 = nx.Graph()
graph2.add_edge('A', 'B', resistance=10)
graph2.add_edge('B', 'C', resistance=20)
graph2.add_edge('A', 'D', resistance=30)
graph2.add_edge('D', 'C', resistance=40)
pos2 = visualize_circuit(graph2, title="Example 2: Nested Configuration")
R_eq2 = calculate_equivalent_resistance(graph2, 'A', 'C')
print(f"Equivalent Resistance for Example 2: {R_eq2:.2f} ohms")
node_voltages2, edge_currents2 = simulate_circuit(graph2, 'A', 'C', 12)
if node_voltages2:
    display_simulation_results(graph2, node_voltages2, edge_currents2, pos2)

# Example 3: Complex Graph with Multiple Cycles
graph3 = nx.Graph()
graph3.add_edge('A', 'B', resistance=10)
graph3.add_edge('B', 'C', resistance=20)
graph3.add_edge('C', 'D', resistance=30)
graph3.add_edge('D', 'A', resistance=40)
graph3.add_edge('A', 'C', resistance=50)
pos3 = visualize_circuit(graph3, title="Example 3: Complex Graph with Multiple Cycles")
R_eq3 = calculate_equivalent_resistance(graph3, 'A', 'D')
print(f"Equivalent Resistance for Example 3: {R_eq3:.2f} ohms")
node_voltages3, edge_currents3 = simulate_circuit(graph3, 'A', 'D', 12)
if node_voltages3:
    display_simulation_results(graph3, node_voltages3, edge_currents3, pos3)

```