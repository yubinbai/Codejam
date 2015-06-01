function solve(N, mat)

    function visit(u, visited)
        visited[u] = true
        for v in 1:N
            if mat[u, v]
                if visited[v]
                    res = true
                else
                    visit(v, visited)
                end
            end
        end
    end

    res = false
    for i in 1:N
        visited = falses(N)
        visit(i, visited)
    end
    res ? "Yes" : "No"
end

fIn = open("input.txt", "r")
fIn = open("A-small-practice.in", "r")
fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    N = int(readline(fIn))
    mat = falses(N, N)
    for i in 1:N
        line = map(int, split(strip(readline(fIn))))
        for c in line[2:end]
            mat[i, c] = true
        end
    end
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(N, mat))
end
