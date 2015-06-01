function solve(N, M, mat)
    used = falses(N, M)
    ok = falses(N, M)
    

    for i in N:-1:1, j in M:-1:1
        if i == N || j == M
            continue
        end
        if (mat[i, j + 1] != mat[i, j]) && (mat[i + 1, j] != mat[i, j]) && (mat[i + 1, j + 1] == mat[i, j])
            ok[i, j] = true
        end
    end

    # println(ok)

    maxA = zeros(Int, N, M)
    maxK = min(N, M)
    res = zeros(Int, maxK)

    for k in maxK:-1:1
        for i in N:-1:1
            for j in M:-1:1
                if used[i, j]
                    maxA[i, j] = 0
                    continue
                end

                if ok[i, j]
                    # println("N $N M $M i $(i) j $j")
                    maxA[i, j] = 1 + min(maxA[i + 1, j], maxA[i, j + 1], maxA[i + 1, j + 1])
                else
                    maxA[i, j] = 1
                end
            end
        end

        count = 0
        for i in 1:N
            for j in 1:M
                if maxA[i, j] >= k
                    count += 1
                    # used[i:k-1+i, j:k-1+j] = 1
                    for ii in 0:k-1
                        for jj in 0:k-1
                            used[i + ii, j + jj] = true
                        end
                    end
                    # maxA[i:k-1+i, max(1-k, -1*j+1)+j:k-1+j] = 0
                    for ii in 0:k-1
                        for jj in max(1-k, -1*j+1):k-1
                            maxA[i + ii, j + jj] = 0
                        end
                    end
                end
            end
        end
        res[k] = count
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
    N, M = map(int, split(strip(readline(fIn))))
    mat = falses(N, M)
    for i in 1:N
        for (j, c) in enumerate(strip(readline(fIn)))
            a = int("0x$c")
            mat[i, (j - 1) * 4 + 1] = (1 << 3) & a > 0
            mat[i, (j - 1) * 4 + 2] = (1 << 2) & a > 0
            mat[i, (j - 1) * 4 + 3] = (1 << 1) & a > 0
            mat[i, (j - 1) * 4 + 4] = (1 << 0) & a > 0
        end
    end
    @printf(fOut, "Case #%d: %s", caseNo, solve(N, M, mat))
end
