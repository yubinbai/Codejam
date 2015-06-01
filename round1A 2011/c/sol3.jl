using Base.Collections

function makeGraph(n, m, cards)
    # classify cards
    T = Int[]
    C0 = Int[]
    C1 = Int[]
    C2 = Int[]
    for (i, c) in enumerate(cards)
        if c[3] > 0
            push!(T, i)
        elseif c[1] == 0
            push!(C0, i)
        elseif c[1] == 1
            push!(C1, i)
        elseif c[1] == 2
            push!(C2, i)
        end
    end

    # makeGraph
    # use a two layer dict to store edges
    edge = Dict()
    # edge = zeros(Int32, sz, sz)
    # hand - the number of drawn cards.
    # turns - the number of turns left.
    # t - T[t] is the first T card that we haven't played yet.
    # c1 - C1[c1] is the first C1 card which we are not yet sure if we are going to play.
    # c2 - C2[c2] is the first C2 card which we are not yet sure if we are going to play.
    # (hand, turns, t, c1, c2)

    # start node = 1, end node = 2
    nodes = Dict()
    nodes[(n, 1, 1, 1, 1)] = 1
    nodes[(0, 0, 0, 0, 0)] = 2
    nNodes = 2
    # println(nodes)


    q = (Int64,Int64,Int64,Int64,Int64)[]
    push!(q, (n, 1, 1, 1, 1))
    while length(q) > 0
        (hand, turns, t, c1, c2) = curr = shift!(q)
        nCurr = nodes[curr]

        # If we have a T card in our hand, we can play it.
        # Condition: T[t].index < hand
        # Weight: T[t].score
        # Target node: (min(N, hand + T[t].card_draw), min(N, turns + T[t].turns - 1), t + 1, c1, c2)
        if turns > 0 && t > 0 && t <= length(T) && T[t] <= hand
            cCurr = cards[T[t]]
            newNode = (min(n + m, hand + cCurr[1]), min(n + m, turns + cCurr[3] - 1), t + 1, c1, c2)
            push!(q, newNode)
            nNodes += 1
            nodes[newNode] = nNodes
            if haskey(edge, nCurr)
                edge[nCurr][nNodes] = cCurr[2]
            else
                edge[nCurr] = [nNodes => cCurr[2]]
            end
            # println(nodes)
        end
        # If we have a C1 card in our hand, we can play the first one.
        # Condition: C1[c1].index < hand
        # Weight: C1[c1].score
        # Target node: (min(N, hand + 1), turns - 1, t, c1 + 1, c2)
        if turns > 0 && c1 > 0 && c1 <= length(C1) && C1[c1] <= hand
            cCurr = cards[C1[c1]]
            newNode = (min(n + m, hand + 1), turns - 1, t, c1 + 1, c2)
            push!(q, newNode)
            nNodes += 1
            nodes[newNode] = nNodes
            if haskey(edge, nCurr)
                edge[nCurr][nNodes] = cCurr[2]
            else
                edge[nCurr] = [nNodes => cCurr[2]]
            end
            # println(nodes)
        end

        # If we have a C1 card in our hand, we can throw away the first one.
        # Condition: C1[c1].index < hand
        # Weight: 0
        # Target node: (hand, turns, t, c1 + 1, c2)
        if turns > 0 && c1 > 0 && c1 <= length(C1) && C1[c1] <= hand
            cCurr = cards[C1[c1]]
            newNode = (hand, turns, t, c1 + 1, c2)
            push!(q, newNode)
            nNodes += 1
            nodes[newNode] = nNodes
            if haskey(edge, nCurr)
                edge[nCurr][nNodes] = 0
            else
                edge[nCurr] = [nNodes => 0]
            end
            # println(nodes)
        end

        # If we have a C2 card in our hand, we can play the first one.
        # Condition: C2[c2].index < hand
        # Weight: C2[c2].score
        # Target node: (min(N, hand + 2), turns - 1, t, c1, c2 + 1)
        if turns > 0 && c2 > 0 && c2 <= length(C2) && C2[c2] <= hand
            cCurr = cards[C2[c2]]
            newNode = (min(n + m, hand + 2), turns - 1, t, c1, c2 + 1)
            push!(q, newNode)
            nNodes += 1
            nodes[newNode] = nNodes
            if haskey(edge, nCurr)
                edge[nCurr][nNodes] = cCurr[2]
            else
                edge[nCurr] = [nNodes => cCurr[2]]
            end
            # println(nodes)
        end

        # If we have a C2 card in our hand, we can throw away the first one.
        # Condition: C2[c2].index < hand
        # Weight: 0
        # Target node: (hand, turns, t, c1, c2 + 1)
        if turns > 0 && c2 > 0 && c2 <= length(C2) && C2[c2] <= hand
            cCurr = cards[C2[c2]]
            newNode = (hand, turns, t, c1, c2 + 1)
            push!(q, newNode)
            nNodes += 1
            nodes[newNode] = nNodes
            if haskey(edge, nCurr)
                edge[nCurr][nNodes] = 0
            else
                edge[nCurr] = [nNodes => 0]
            end
            # println(nodes)
        end
    end
    for (cNode, nodeNo) in nodes
        if nodeNo != 2
            (hand, turns, t, c1, c2) = cNode
            c0before = Int[]
            for c in C0
                if c <= hand
                    push!(c0before, cards[c][2])
                end
            end
            sort!(c0before)
            if !haskey(edge, nodeNo)
                edge[nodeNo] = Dict()
            end
            if turns >= length(c0before)
                edge[nodeNo][2] = sum(c0before)
            else
                edge[nodeNo][2] = sum(c0before[(end-turns+1):end])
            end
        end
    end

    edge, nodes, nNodes
end

function topoSort(graph, N)
    function topoVisit(u)
        visited[u] = 1
        if haskey(graph, u)
            for v in keys(graph[u])
                if (visited[v] == 0)
                    topoVisit(v)
                end
            end
        end
        unshift!(topoSorted, u)
    end
    visited = [k => 0 for k in 1:N]
    topoSorted = typeof(first(keys(graph)))[]
    for v in keys(graph)
        if visited[v] == 0
            topoVisit(v)
        end
    end
    return topoSorted
end

function maxPath(incoming, source, N, listNode)
    dist = zeros(Int, N)
    for e1 in listNode
        for (e2, v2) in incoming[e1]
            dist[e1] = max(dist[e2] + v2, dist[e1])
        end
    end
    maximum(dist)
end

fIn = open("input.txt", "r")
# fIn = open("C-small-practice.in", "r")
# fIn = open("C-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))

    # read data file
    n = int(readline(fIn))
    cards = [map(int, split(readline(fIn))) for i in 1:n]
    m = int(readline(fIn))
    append!(cards, [map(int, split(readline(fIn))) for i in 1:m])

    edge, nodes, nNodes = makeGraph(n, m, cards)
    incoming = [Dict() for i in 1:nNodes]
    for (k1, v1) in edge
        for (k2, v2) in v1
            incoming[k2][k1] = v2
        end
    end
    # println(incoming)
    listNode = topoSort(edge, nNodes)
    result = maxPath(incoming, 1, nNodes, listNode)
    println("Case #$caseNo: $(result)")
end
