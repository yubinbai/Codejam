 # Unfortunately, even though the number of runs of boxes and toys is small, the total number of
 #  boxes and toys can be very large, so this algorithm is not practical. But we can modify it so 
 # that f[x][y] will be the maximum number of toys that could be placed in boxes using the first x 
 # runs of boxes and the first y runs of toys. Now f[x][y] is the maximum of:

# f[x-1][y]
# f[x][y-1]
# f[a][b]+g(a,b,x,y), for all a<x, b<y
# Similarly to before, the last case only applies if the type of box run x matches the type of toy run y. 
# It corresponds to only using boxes of that type between runs a+1 and x, and toys of that type between 
# runs b+1 and y. g(a,b,x,y) is the minimum of the number of those toys and the number of those boxes, 
# which is the number of toys that can be placed in boxes in that range.

function solve(N, M, a, A, b, B)

    cumA = zeros(Int, N, 101)
    cumB = zeros(Int, M, 101)

    for typ in 1:100
        for i in 1:N
            if i > 1
                cumA[i, typ] = cumA[i - 1, typ]
            end
            if A[i] == typ
                cumA[i, typ] += a[i]
            end
        end
        for i in 1:M
            if i > 1
                cumB[i, typ] = cumB[i - 1, typ]
            end
            if B[i] == typ
                cumB[i, typ] += b[i]
            end
        end
    end

    dp = zeros(Int, N + 1, M + 1)
    
    for i in 1:N, j in 1:M
        # f[a][b]+g(a,b,x,y), for all a<x, b<y
        # Similarly to before, the last case only applies if the type of box run x matches the type of toy run y. 
        # It corresponds to only using boxes of that type between runs a+1 and x, and toys of that type between 
        # runs b+1 and y. g(a,b,x,y) is the minimum of the number of those toys and the number of those boxes, 
        # which is the number of toys that can be placed in boxes in that range.
        dp[i + 1, j + 1] = max(dp[i + 1, j + 1], dp[i, j + 1], dp[i + 1, j])
        if A[i] == B[j]
            typ = A[i]
            for ni in 0:i-1, nj in 0:j-1
                countA = cumA[i, typ] - ( ni == 0 ? 0 : cumA[ni, typ])
                countB = cumB[j, typ] - ( nj == 0 ? 0 : cumB[nj, typ])
                dp[i + 1, j + 1] = max(dp[i + 1, j + 1], dp[ni + 1, nj + 1] + min(countA, countB))
            end
        end
    end
    # println(dp)
    dp[N + 1, M + 1]
end


fIn = open("input.txt", "r")
fIn = open("C-small-practice.in", "r")
fIn = open("C-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    N, M = map(int, split(readline(fIn)))
    a = Int[]
    A = Int[]
    line = map(int, split(readline(fIn)))
    for i in 1:N
        push!(a, line[(i - 1) * 2 + 1])
        push!(A, line[(i - 1) * 2 + 2])
    end
    b = Int[]
    B = Int[]
    line = map(int, split(readline(fIn)))
    for i in 1:M
        push!(b, line[(i - 1) * 2 + 1])
        push!(B, line[(i - 1) * 2 + 2])
    end
    
    result = solve(N, M, a, A, b, B)
    println(fOut, "Case #$caseNo: $result")
end
