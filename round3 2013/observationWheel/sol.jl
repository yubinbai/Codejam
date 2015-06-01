addprocs(4)

@everywhere function solve(status)
    N = length(status)
    memo = [join(['X' for i in 1:N]) => 0.0]

    function avg(w)
        if haskey(memo, w)
            return memo[w]
        end
        s = 0.0
        for i in 1:N
            j = i
            r = N
            while true
                if w[j] == '.'
                    s += r
                    w1 = [c for c in w]
                    w1[j] = 'X'
                    s += avg(join(w1))
                    break
                else
                    r -= 1
                    j += 1
                    j = (j - 1 + N) % N + 1
                end
            end
        end
        memo[w] = 1.0 * s / N
    end

    avg(status)
end

fIn = open("input.txt", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
res = zeros(totalCase)
inp = [strip(readline(fIn)) for _i in 1:totalCase]
res = pmap(solve, inp)
# for caseNo in 1:totalCase
#     res[caseNo] = solve(inp[caseNo])
# end
for caseNo in 1:totalCase
    @printf(fOut, "Case #%d: %f\n", caseNo, res[caseNo])
end

