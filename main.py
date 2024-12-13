import heapq

def dijkstra(graph, source):
    # Inisialisasi dist dan prev
    dist = {vertex: float('inf') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    dist[source] = 0

    # Antrian prioritas (heap), dimulai dengan source vertex
    priority_queue = [(0, source)]  # (jarak, vertex)

    while priority_queue:
        # Ambil vertex dengan jarak terkecil
        current_dist, u = heapq.heappop(priority_queue)

        # Jika jarak yang diambil lebih besar dari dist[u], berarti sudah diproses
        if current_dist > dist[u]:
            continue

        # Proses tetangga-tetangga vertex u
        for v, weight in graph[u].items():
            alt = dist[u] + weight  # Jarak alternatif melalui u

            # Jika ditemukan jalur yang lebih pendek ke v
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(priority_queue, (alt, v))  # Masukkan v ke antrian dengan jarak baru

    return dist, prev

def shortest_path(graph, source, target):
    dist, prev = dijkstra(graph, source)
    path = []
    current = target

    # Bangun jalur terpendek dari target ke source
    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()  # Balikkan agar urut dari source ke target
    return path

# Contoh graf coba  ubah vertexnya misal v1 
graph = {
    'v1': {'b': 1, 'c': 4},
    'b': {'v1': 1, 'c': 2, 'd': 5},
    'c': {'v1': 4, 'b': 2, 'd': 1},
    'd': {'v1': 5, 'c': 1}
}

# Menghitung jarak terpendek dan jalur terpendek
source = 'v1'
target = 'd'
dist, prev = dijkstra(graph, source)

print(f"Jarak terpendek dari {source}: {dist}")
print(f"Jalur terpendek dari {source} ke {target}: {shortest_path(graph, source, target)}")
