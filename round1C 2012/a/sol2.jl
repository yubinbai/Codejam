addprocs(4)
@everywhere function solve(inp)

    N, mat = inp

    for k in 1:N, i in 1:N, j in 1:N
        if mat[i, k] && mat[k, j]
            if mat[i, j]
                return "Yes"
            else
                mat[i, j] = true
            end
        end
    end
    "No"
end

fIn = open("input.txt", "r")
fIn = open("A-small-practice.in", "r")
fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
inp = (Int, Array{Bool, 2})[]
for caseNo in 1:totalCase
    N = int(readline(fIn))
    mat = falses(N, N)
    for i in 1:N
        line = map(int, split(strip(readline(fIn))))
        for c in line[2:end]
            mat[i, c] = true
        end
    end
    push!(inp, (N, copy(mat)))
end
res = pmap(solve, inp)
for caseNo in 1:totalCase
    @printf(fOut, "Case #%d: %s\n", caseNo, res[caseNo])
end
