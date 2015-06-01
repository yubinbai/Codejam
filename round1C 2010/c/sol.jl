addprocs(4)

@everywhere function solve(inp)
    # brute force
    N, M, mat = inp

    function check(x, y, len)
        # println("N $N, M $M")
        # println("x $(x) y $(y) len $(len)")
        for i in x:x+len-1, j in y:y+len-1
            if mat[i, j] == -1
                return false
            elseif i > x && mat[i, j] == mat[i-1, j]
                return false
            elseif j > y && mat[i, j] == mat[i, j-1]
                return false
            end
        end
        return true
    end

    function mark(x, y, len)
        for i in x:x+len-1, j in y:y+len-1
            mat[i, j] = -1
        end
    end

    maxK = min(N, M)
    res = zeros(Int, maxK)
    for len in maxK:-1:1, i in 1:N, j in 1:M
        if i + len - 1 <= N && j + len - 1 <= M
            if check(i, j, len)
                res[len] += 1
                mark(i, j, len)
            end
        end
    end

    counter = 0
    resStr = ""
    for k in maxK:-1:1
        if res[k] != 0
            counter += 1
            resStr *= "$k $(res[k])\n"
        end
    end
    "$counter\n" * resStr
end

fIn = open("input.txt", "r")
fIn = open("C-small-practice.in", "r")
fIn = open("C-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
inp = (Int, Int, Array{Int, 2})[]
for caseNo in 1:totalCase
    N, M = map(BigInt, split(strip(readline(fIn))))
    mat = zeros(Int8, N, M)
    for i in 1:N
        for (j, c) in enumerate(strip(readline(fIn)))
            a = int("0x$c")
            mat[i, (j - 1) * 4 + 1] = int( (1 << 3) & a > 0)
            mat[i, (j - 1) * 4 + 2] = int( (1 << 2) & a > 0)
            mat[i, (j - 1) * 4 + 3] = int( (1 << 1) & a > 0)
            mat[i, (j - 1) * 4 + 4] = int( (1 << 0) & a > 0)
        end
    end
    push!(inp, (N, M, copy(mat)))
end
res = pmap(solve, inp)
for caseNo in 1:totalCase
    @printf(fOut, "Case #%d: %s", caseNo, res[caseNo])
end
