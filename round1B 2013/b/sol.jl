function solve(N, x, y)
    currSum = size = BigInt(1)
    while currSum + 2 * (size + 2) - 1 <= N
        currSum += 2 * (size + 2) - 1
        size += 2
    end
    if abs(x - y) in 0:2:size && abs(x + y) in 0:2:size
        return 1.0
    end
    if abs(x - y) > (size + 1) || abs(x - y) % 2 != 0
        return 0.0
    end
    # on the edge
    outerLayer = N - currSum
    if outerLayer < y
        return 0.0
    end
    if outerLayer >= size + 2
        overflow = outerLayer - (size + 1)
        outerLayer -= 2 * overflow
        y -= overflow
    end
    combSum = sum([comb(outerLayer, i) for i in 0:y])
    return 1 - combSum * 1.0 / (2 ^ outerLayer)
end


function comb(n, k)
    return factorial(BigInt(n)) / (factorial(BigInt(k)) * factorial(BigInt(n - k)))
end


fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    N, x, y = map(int, split(readline(fIn)))

    result = solve(N, x, y)
    @printf(fOut, "Case #%d: %.6f\n", caseNo, result)
end
