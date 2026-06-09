def verify_edge_count(vertices: int, edges: int) -> bool:
    max_edges = vertices * (vertices - 1) // 2
    return 0 <= edges <= max_edges


if __name__ == '__main__':
    print(verify_edge_count(5, 10))
