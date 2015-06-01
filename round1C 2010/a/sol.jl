function solve(N, lines)
    prev = (Int, Int)[]
    total = 0
    for (a1, b1) in lines
        for (a2, b2) in prev
            if (a1 - a2) * (b1 - b2) < 0
                total += 1
            end
        end
        push!(prev, (a1, b1))
    end
    total
end

fIn = open("input.txt", "r")
fIn = open("A-small-practice.in", "r")
fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    # @printf("Case #%d: %s\n", caseNo, solve(inp[caseNo]))
    N = int(readline(fIn))
    lines = [map(int, split(readline(fIn))) for i in 1:N]
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(N, lines))
end