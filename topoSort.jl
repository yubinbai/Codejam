function topoSort(graph)
    function topoVisit(u)
        visited[u] = 1
        for v in graph[u]
            if (visited[v] == 0)
                topoVisit(v)
            end
        end
        unshift!(topoSorted, u)
    end
    visited = [k => 0 for k in keys(graph)]
    topoSorted = typeof(first(keys(graph)))[]
    for v in keys(graph)
        if visited[v] == 0
            topoVisit(v)
        end
    end
    return topoSorted
end

graph = {0 => [1], 1 => [3], 2 => [1], 3 => [2, 4], 4 => [5], 5 => [7], 6 => [4], 7 => [6]}
println(join(topoSort(graph), ' '))
