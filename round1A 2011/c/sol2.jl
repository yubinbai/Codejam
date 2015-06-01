function solve(n, m, cards)
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

    # hand - the number of drawn cards.
    # turns - the number of turns left.
    # t - T[t] is the first T card that we haven't played yet.
    # c1 - C1[c1] is the first C1 card which we are not yet sure if we are going to play.
    # c2 - C2[c2] is the first C2 card which we are not yet sure if we are going to play.
    # (hand, turns, t, c1, c2)

    # scores of nodes
    nodes = [(n, 1, 1, 1, 1) => 0, (0, 0, 0, 0, 0) => 0]

    q = (Int64,Int64,Int64,Int64,Int64)[]
    push!(q, (n, 1, 1, 1, 1))
    while length(q) > 0
        (hand, turns, t, c1, c2) = curr = shift!(q)
        vCurr = nodes[curr]

        # If we have a T card in our hand, we can play it.
        # Condition: T[t].index < hand
        # Weight: T[t].score
        # Target node: (min(N, hand + T[t].card_draw), min(N, turns + T[t].turns - 1), t + 1, c1, c2)
        if turns > 0 && t > 0 && t <= length(T) && T[t] <= hand
            cCurr = cards[T[t]]
            node1 = (min(n + m, hand + cCurr[1]), min(n + m, turns + cCurr[3] - 1), t + 1, c1, c2)
            push!(q, node1)
            if haskey(nodes, node1) && nodes[node1] < cCurr[2] + vCurr
                nodes[node1] = cCurr[2] + vCurr
            else
                nodes[node1] = cCurr[2] + vCurr
            end
        end
        # If we have a C1 card in our hand, we can play the first one.
        # Condition: C1[c1].index < hand
        # Weight: C1[c1].score
        # Target node: (min(N, hand + 1), turns - 1, t, c1 + 1, c2)
        if turns > 0 && c1 > 0 && c1 <= length(C1) && C1[c1] <= hand
            cCurr = cards[C1[c1]]
            node1 = (min(n + m, hand + 1), turns - 1, t, c1 + 1, c2)
            push!(q, node1)
            if haskey(nodes, node1)
                nodes[node1] = max(cCurr[2] + vCurr, nodes[node1])
            else
                nodes[node1] = cCurr[2] + vCurr
            end
        end

        # If we have a C1 card in our hand, we can throw away the first one.
        # Condition: C1[c1].index < hand
        # Weight: 0
        # Target node: (hand, turns, t, c1 + 1, c2)
        if turns > 0 && c1 > 0 && c1 <= length(C1) && C1[c1] <= hand
            cCurr = cards[C1[c1]]
            node1 = (hand, turns, t, c1 + 1, c2)
            push!(q, node1)
            if haskey(nodes, node1)
                nodes[node1] = max(vCurr, nodes[node1])
            else
                nodes[node1] = vCurr
            end
        end

        # If we have a C2 card in our hand, we can play the first one.
        # Condition: C2[c2].index < hand
        # Weight: C2[c2].score
        # Target node: (min(N, hand + 2), turns - 1, t, c1, c2 + 1)
        if turns > 0 && c2 > 0 && c2 <= length(C2) && C2[c2] <= hand
            cCurr = cards[C2[c2]]
            node1 = (min(n + m, hand + 2), turns - 1, t, c1, c2 + 1)
            push!(q, node1)
            if haskey(nodes, node1)
                nodes[node1] = max(cCurr[2] + vCurr, nodes[node1])
            else
                nodes[node1] = cCurr[2] + vCurr
            end
        end

        # If we have a C2 card in our hand, we can throw away the first one.
        # Condition: C2[c2].index < hand
        # Weight: 0
        # Target node: (hand, turns, t, c1, c2 + 1)
        if turns > 0 && c2 > 0 && c2 <= length(C2) && C2[c2] <= hand
            cCurr = cards[C2[c2]]
            node1 = (hand, turns, t, c1, c2 + 1)
            push!(q, node1)
            if haskey(nodes, node1)
                nodes[node1] = max(vCurr, nodes[node1])
            else
                nodes[node1] = vCurr
            end
        end
    end
    for (e, v) in nodes
        zeroNode = (0, 0, 0, 0, 0)
        if e != zeroNode
            (hand, turns, t, c1, c2) = e
            c0before = Int[]
            for c in C0
                if c <= hand
                    push!(c0before, cards[c][2])
                end
            end
            sort!(c0before)
            if turns >= length(c0before)
                nodes[zeroNode] = max(sum(c0before) + v, nodes[zeroNode])
            else
                nodes[zeroNode] = max(sum(c0before[(end-turns+1):end]) + v, nodes[zeroNode])
            end
        end
    end

    result = maximum([v for (k, v) in nodes])
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

    result = solve(n, m, cards)
    println(fOut, "Case #$caseNo: $(result)")
end
