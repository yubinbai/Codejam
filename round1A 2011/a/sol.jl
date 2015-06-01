@everywhere function solve(inp)
    # wd = d * pd / 100; wg = g * pg / 100; d < g; wd < wg
    n, pd, pg = inp
    if pg == 0 
        return pd == 0
    end
    if pg == 100
        return pd == 100
    end
    d = 100 / gcd(100, pd)
    return d <= n
end
# fIn = open("input.txt", "r")
# fIn = open("a-small.txt", "r")
fIn = open("a-large.txt", "r")
fOut = open("output.txt", "w")

totalCase = int(readline(fIn))
inp = [map(int, split(readline(fIn))) for caseNo in 1:totalCase]
# for caseNo in 1:totalCase
    # @printf("%s\n", solve(inp[caseNo]))
# end
res = map(solve, inp)
for caseNo in 1:totalCase
    println(fOut, "Case #$caseNo: $(res[caseNo] ? "Possible" : "Broken")")
end
