# addprocs(4)

function solve(inp)
    N, L, H = inp[1:3]
    freq = inp[4:end]

    for f1 in L:H
        work = true
        for f2 in freq
            g = gcd(f1, f2)
            if g != f1 && g != f2
                work = false
            end
        end
        if work
            return f1
        end
    end
    return "NO"
end

fIn = open("input.txt", "r")
fIn = open("C-small-practice.in", "r")
# fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")

totalCase = int(readline(fIn))
inp = [map(int, split(readline(fIn) * readline(fIn))) for caseNo in 1:totalCase]
for caseNo in 1:totalCase
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(inp[caseNo]))
end
# res = pmap(solve, inp)
# for caseNo in 1:totalCase
#     println(fOut, "Case #$caseNo: $(res[caseNo])")
# end
