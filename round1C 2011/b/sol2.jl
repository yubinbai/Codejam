addprocs(4)

@everywhere function solve(inp)
    l, t, N, c = inp[1:4]
    cycleC = inp[5:end]
    dist = [cycleC[(i - 1) % c + 1] for i in 1:N]
    ans = sum(dist) * 2

    # Edges that your flagship will pass before any speed boosters can be built.
    pos = 1 
    while pos <= N
        if t >= 2 * dist[pos]
            t -= 2 * dist[pos]
            pos += 1
        else
            break
        end
    end
    if pos > N
        return int(ans)
    end

    # Edges whose speed boosters would finish while your flagship is moving along the edge.
    if t % 2 == 1
        println("print")
    end
    dist[pos] -= t / 2

    # Edges whose speed boosters can be built before your flagship gets there.
    benefit = dist[pos:end]
    try
        sort!(benefit)
        start = max(1, length(benefit) - l + 1)
        ans -= sum(benefit[start:end])
    catch e
        println("l $l pos $pos length $(length(dist))")
    end
    return int(ans)
end

fIn = open("input.txt", "r")
# fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
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
