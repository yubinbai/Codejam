addprocs(4)

@everywhere function solve(status)
    N = length(status)
    memo = ones(1 << N) * -1
    memo[end] = 0.0

    function avg(w)
        if memo[w + 1] != -1.0
            return memo[w + 1]
        end
        s = 0.0
        for i in 0:N-1
            j = i
            r = N
            while true
                if ((1 << j) & w) == 0
                    s += r
                    s += avg((1 << j) | w)
                    break
                else
                    r -= 1
                    j += 1
                    j %= N 
                end
            end
        end
        memo[w + 1] = 1.0 * s / N
    end

    n = parseint(replace(replace(status, '.', '0'), 'X', '1'), 2)
    avg(n)
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
