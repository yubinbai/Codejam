using Base.Collections


function solve(H, row, col, ce, fl)

    # earliest time to enter (r2, c2)
    function enter_time(r1, c1, r2, c2)
        if min(ce[r1][c1], ce[r2][c2]) - max(fl[r1][c1], fl[r2][c2]) < 50
            return typemax(Int)
        end
        th = ce[r2][c2] - 50
        if H <= th
            return typemin(Int)
        else
            return H - th
        end
    end

    prio = ones(Int, row, col) * typemax(Int)
    prio[1, 1] = typemin(Int) + 1
    q = (Int, Int, Int)[] 
    heappush!(q, (prio[1, 1], 1, 1))
    while length(q) > 0
        v1, r1, c1 = heappop!(q)
        if v1 != prio[r1, c1]
            continue
        end
        for (r2, c2) in [(r1 + 1, c1), (r1 - 1, c1), (r1, c1 - 1), (r1, c1 + 1)]
            if r2 >=1 && r2 <= row && c2 >= 1 && c2 <= col
                t = enter_time(r1, c1, r2, c2)
                if t != typemax(Int)
                    t = max(t, prio[r1, c1])
                    if H - t >= fl[r1][c1] + 20
                        t += 10
                    else
                        t += 100
                    end
                    if t < prio[r2, c2]
                        prio[r2, c2] = t
                        heappush!(q, (t, r2, c2))
                    end
                end
            end
        end
    end
    return prio[row, col]
end

fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")

totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    H, N, M = map(int, split(readline(fIn))) 
    ce = [map(int, split(readline(fIn))) for i in 1:N]
    fl = [map(int, split(readline(fIn))) for i in 1:N]
    ans = solve(H, N, M, ce, fl)
    ans = (ans > 0) ? ans * 0.1 : 0.0
    println(fOut, "Case #$caseNo: $(ans)")
end
