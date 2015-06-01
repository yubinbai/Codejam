addprocs(4)

@everywhere function solve(inp)
    P, Q, p = inp
    memo = Dict()

    # Finds the minimum amount of gold needed, 
    # if we only consider the cells from a to b, inclusive.
    function dp(a, b)
        # First, look up the cache to see if the 
        # result is computed before.
        if haskey(memo, (a, b))
            return memo[a, b]
        end

        # Start the computation.  
        r = typemax(Int)
        for i in 1:Q
            if p[i] >= a && p[i] <= b
                tmp = (b - a) + dp(a, p[i] - 1) + dp(p[i] + 1, b);
                r = min(tmp, r)
            end
        end
        memo[a, b] = r
    end
    dp(1, P)
end

fIn = open("input.txt", "r")
fIn = open("C-small-practice.in", "r")
fIn = open("C-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
inp = (Int, Int, Array{Int, 1})[]
for caseNo in 1:totalCase
    P, Q = map(int, split(readline(fIn)))
    p = map(int, split(readline(fIn)))
    push!(inp, (P, Q, copy(p)))
end
res = pmap(solve, inp)

for caseNo in 1:totalCase
    @printf(fOut, "Case #%d: %s\n", caseNo, res[caseNo])
end
