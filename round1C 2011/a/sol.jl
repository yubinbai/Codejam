fIn = open("input.txt", "r")
fIn = open("a-large.in", "r")
# fIn = open("a-small.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    row, column = map(int, split(readline(fIn)))
    mat = [[c for c in strip(readline(fIn))] for _i in 1:row]
    hasWorked = true
    for r in 1:row
        for c in 1:column
            if mat[r][c] != '#'
                continue
            end
            try
                if mat[r][c + 1] != '#' || mat[r + 1][c] != '#' || mat[r + 1][c + 1] != '#'
                    hasWorked = false
                    continue
                end
                mat[r][c] = '/'
                mat[r][c + 1] = '\\'
                mat[r + 1][c] = '\\'
                mat[r + 1][c + 1] = '/'
            catch
                # bound error
                hasWorked = false
                continue
            end
        end
    end
    if hasWorked
        println(fOut, "Case #$caseNo:")
        for r in 1:row
            println(fOut, join(mat[r]))
        end
    else
        println(fOut, "Case #$caseNo: \nImpossible")
    end
end
