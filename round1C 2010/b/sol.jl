function solve(L, P, C)
    e = 1
    while L * C ^ e < P
        e *= 2
    end
    int(log(2, e))
end

fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    L, P, C = map(BigInt, split(strip(readline(fIn))))
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(L, P, C))
end