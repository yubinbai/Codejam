const MAX_COST = 25555

function solve(inp)
    D, I, M, N = inp[1:4]
    # 1..256
    A = inp[5:end] + 1
    # println("join(inp, ' ') $(join(inp, ' '))")
    # println("join(A, ' ') $(join(A, ' '))")

    # cost of making 1..i-1 smooth and end with q
    memo = ones(Int, N + 1, 257) * MAX_COST
    memo[1, 257] = 0

    for i in 2:(N + 1)
        for p in 1:256
            for q in 1:256
                # change value to q
                d = abs(A[i - 1] - q)
                diff = abs(p - q)
                if diff > M
                    if M == 0
                        ins = MAX_COST
                    else
                        # insert
                        ins = (diff % M == 0) ? (diff / M - 1) : div(diff, M)
                        ins *= I
                    end
                else
                    ins = 0
                end
                memo[i, q] = min(memo[i, q], memo[i - 1, p] + d + ins)
            end
        end
        # p == 257 (empty)
        for q in 1:256
            d = abs(A[i - 1] - q)
            memo[i, q] = min(memo[i, q], memo[i - 1, 257] + d)
        end
        memo[i, 257] = memo[i - 1, 257] + D
    end
    # println("join(memo[3, 1:end], ' ') $(join(memo[3, 1:end], ' '))")
    return minimum([memo[N + 1, i] for i in 1:257])
end

fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
inp = [map(int, split(readline(fIn) * readline(fIn))) for caseNo in 1:totalCase]
for caseNo in 1:totalCase
    # @printf("Case #%d: %s\n", caseNo, solve(inp[caseNo]))
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(inp[caseNo]))
end