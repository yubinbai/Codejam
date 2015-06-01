function solve(n, k, mat)
    for r in 1:n
        y = n
        for x in n:-1:1
            if y < 1
                break
            end
            if mat[r][y] != '.'
                y -= 1
                continue
            end
            if mat[r][x] != '.'
                mat[r][y] = mat[r][x]
                mat[r][x] = '.'
                y -= 1
            end
        end
    end
    for r in 1:n
        println("join(mat[r]) $(join(mat[r]))")
    end
    function check(seq, c)
        # println("join(seq) $(join(seq))")
        # println("join([c for i in 1:k]) $(join([c for i in 1:k]))")
        return searchindex(join(seq), join([c for i in 1:k])) > 0
    end


    res = ['R' => false, 'B' => false]
    for color in ['R', 'B']
        for r in 1:n
            res[color] |= check(mat[r], color)
        end
        if res[color]
            continue
        end
        for c in 1:n
            res[color] |= check([mat[r][c] for r in 1:n], color)
        end
        if res[color]
            continue
        end
        for row in 1:n
            r, c = row, 1
            t = ['.']
            while r >= 1 && r <=n && c >= 1 && c <= n
                push!(t, mat[r][c])
                r -= 1
                c += 1
            end
            res[color] |= check(t, color)
        end
        if res[color]
            continue
        end
        for col in 2:n
            r, c = n, col
            t = ['.']
            while r >= 1 && r <=n && c >= 1 && c <= n
                push!(t, mat[r][c])
                r -= 1
                c += 1
            end
            res[color] |= check(t, color)
        end
        if res[color]
            continue
        end
        for row in 1:n 
            r, c = row, 1
            t = ['.']
            while r >= 1 && r <=n && c >= 1 && c <= n
                push!(t, mat[r][c])
                r += 1
                c += 1
            end
            res[color] |= check(t, color)
        end
        if res[color]
            continue
        end
        for col in 2:n 
            r, c = 1, col
            t = ['.']
            while r >= 1 && r <=n && c >= 1 && c <= n
                push!(t, mat[r][c])
                r += 1
                c += 1
            end
            res[color] |= check(t, color)
        end
    end
    if res['R']
        if res['B']
            return "Both"
        else
            return "Red"
        end
    else
        if res['B']
            return "Blue"
        else
            return "Neither"
        end
    end
end


fIn = open("input.txt", "r")
fIn = open("A-small-practice.in", "r")
# fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    n, k = map(int, split(readline(fIn)))
    mat = [[c for c in strip(readline(fIn))] for r in 1:n]
    # for r in 1:n
    #     println("join(mat[r]) $(join(mat[r]))")
    # end

    result = solve(n, k, mat)
    println(fOut, "Case #$caseNo: $result")
end
