"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화
    if visited is None:
        # 현재 코드의 if not visited:는 visited가 비어있는 리스트 []일 때도 참(True)으로 인식되어 visited = []로 다시 덮어씌웁니다.
        visited = []

    seen = set(visited)

    def _dfs(vertex):
        visited.append(vertex)
        seen.add(vertex)

        for next_vertex in graph[vertex]:
            if next_vertex not in seen:
                _dfs(next_vertex)

    if start not in seen:
        _dfs(start)
    
    return visited

def dfs_stack(graph, start):
    """
    깊이 우선 탐색 (스택)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    visited = [start]
    stack = [start]
        
    while stack:
        vertex = stack.pop()
        
        for node in graph[vertex]:
            if node not in visited:
                visited.append(node)
                stack.append(node)

    return visited


# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색 / 재귀) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

    print("=== DFS (깊이 우선 탐색 / 스택) ===")
    result = dfs_stack(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


