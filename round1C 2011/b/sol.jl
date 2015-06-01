addprocs(4)

@everywhere function solve(inp)
    l, t, n, c = map(int, inp[1:4])
    cycleC = map(int, inp[5:end])
    dist = [cycleC[(i - 1) % c + 1] for i in 1:n]
    if l == 0
        return sum([dist[i] for i in 1:n]) * 2
    elseif l == 1
        result = typemax(Int)
        for l1 in 1:n 
            curr = 0
            for i in 1:n
                if i == l1 && (t >= curr && t <= curr + dist[i] * 2)
                    d = dist[i]
                    d1 = (t - curr) * 0.5
                    d2 = d - d1
                    curr = t + d2
                elseif i == l1 && curr > t
                    curr += dist[i]
                else
                    curr += dist[i] * 2
                end
            end
            result = min(curr, result)
        end
        return result
    elseif l == 2
        result = typemax(Int)
        for l1 in 1:n
            for l2 in l1 + 1:n
                curr = 0
                for i in 1:n
                    if (i == l1 || i == l2) && (t >= curr && t <= curr + dist[i] * 2)
                        d = dist[i]
                        d1 = (t - curr) * 0.5
                        d2 = d - d1
                        curr = t + d2
                    elseif (i == l1 || i == l2) && curr > t
                        curr += dist[i]
                    else
                        curr += dist[i] * 2
                    end
                end
                result = min(curr, result)
            end
        end
        return result
    end
end

fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
# fIn = open("a-large.txt", "r")
fOut = open("output.txt", "w")

totalCase = int(readline(fIn))
inp = [map(float, split(readline(fIn))) for caseNo in 1:totalCase]
# for caseNo in 1:totalCase
#     @printf("Case #%d: %d\n", caseNo, solve(inp[caseNo]))
# end
res = pmap(solve, inp)
for caseNo in 1:totalCase
    println(fOut, "Case #$caseNo: $(res[caseNo])")
end
