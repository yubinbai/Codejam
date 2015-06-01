using Base.Collections
const N = 10000

function dijkstra(source)
    dist = [edgeWeight[source, i] for i in 1:N]
    dist[source] = 0
    visited = zeros(Int8, N)
    queue = PriorityQueue()
    for i in 1:N 
        enqueue!(queue, i, dist[i])
    end
    visitedCount = 0
    while visitedCount <= N && length(queue) > 0
        v1, d1 = peek(queue)
        dequeue!(queue)
        if visited[v1] != 0
            continue
        end
        dist[v1] = d1
        visited[v1] = 1
        visitedCount += 1
        for v2 in 1:N
            shorterD = edgeWeight[v1, v2] + d1
            if dist[v2] > shorterD
                dist[v2] = shorterD
                queue[v2] = shorterD
            end
        end
    end
    return dist
end


edgeWeight = rand(N, N)
@time dijkstra(1)
# @time for i in 1:N
#     dijkstra(i)
# end
