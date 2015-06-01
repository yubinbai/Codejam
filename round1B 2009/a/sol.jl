type Node
    name::ASCIIString
    isLeaf::Bool
    w::Real
    left::Node
    right::Node

    function Node(w::Real, isLeaf::Bool)
        me = new()
        me.isLeaf = isLeaf
        me.w = w 
        me 
    end
end

function parseTree(s)
    # is leaf?
    if isdigit(s[end-1])
        return Node(float(s[2:end-1]), true)
    else
        startL = search(s, '(', 2)
        endL = 0
        depth = 0
        for i in startL:length(s)
            if s[i] == '('
                depth += 1
            elseif s[i] == ')'
                depth -= 1
            end
            if depth == 0
                endL = i
                break
            end
        end
        startR = endL + 1
        endR = length(s) - 1
        w, n = split(s[2:startL - 1])
        e = Node(float(w), false)
        e.name = n
        e.left = parseTree(s[startL:endL])
        e.right = parseTree(s[startR:endR])
        e
    end
end

function getWeight(treeNode, test)
    f = Set()
    for c in test[3:end]
        push!(f, c)
    end
    p = 1.0
    while treeNode.isLeaf == false
        p *= treeNode.w
        if treeNode.name in f
            treeNode = treeNode.left
        else
            treeNode = treeNode.right
        end
    end
    p *= treeNode.w
end

fIn = open("input.txt", "r")
fIn = open("A-small-practice.in", "r")
fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    L = int(readline(fIn))
    tStr = join([strip(readline(fIn)) for i in 1:L])
    tree = parseTree(tStr)
    N = int(readline(fIn))
    @printf(fOut, "Case #%d:\n", caseNo)
    for i in 1:N
        test = split(strip(readline(fIn)))
        @printf(fOut, "%.7f\n", getWeight(tree, test))
    end
end
