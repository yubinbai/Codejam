const phi = (1 + sqrt(5.0)) / 2.0

function solve(inp)
    a1, a2, b1, b2 = inp[1:4]
    total = 0
    for b in b1:b2
        lim = max(int(ceil(b * phi)), a1)
        if a2 >= lim
            total += a2 - lim + 1
        end
    end
    for a in a1:a2
        lim = max(int(ceil(a * phi)), b1)
        if b2 >= lim
            total += b2 - lim + 1
        end
    end
    return total
end

fIn = open("input.txt", "r")
fIn = open("C-small-practice.in", "r")
fIn = open("C-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
inp = [map(int, split(readline(fIn))) for caseNo in 1:totalCase]
for caseNo in 1:totalCase
    # @printf("Case #%d: %s\n", caseNo, solve(inp[caseNo]))
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(inp[caseNo]))
end