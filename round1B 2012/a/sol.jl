@everywhere function solve(inp)
    function worked(c, p)
        # chosen c, percent p
        s = copy(J)
        total = sum(s)
        limit = s[c] + total * p
        alloc = total * (1 - p) 
        splice!(s, c)
        sort!(s)
        for i in 1:length(s) - 1
            if s[i + 1] > s[i]
                diff = s[i + 1] - s[i]
                if alloc <= diff * i
                    s[1:i] += alloc / i
                    alloc = 0
                    break
                else
                    s[1:i] += diff
                    alloc -= diff * i
                end
            end
        end
        if alloc > 0
            s += alloc / length(s)
            # println("c $c p $p s $(join(s, ' '))")
        end
        return limit >= s[1]
    end

    N = int(inp[1])
    J = inp[2:end]
    result = zeros(N)
    for i in 1:N
        left, right = 0.0, 1.0
        while nextfloat(left) < right
            mid = (left + right) / 2
            if worked(i, mid)
                right = mid
            else
                left = nextfloat(mid)
            end
        end
        result[i] = left * 100
    end
    join(result, ' ')
end

fIn = open("input.txt", "r")
fIn = open("a-small.in", "r")
fIn = open("a-large.in", "r")
fOut = open("output.txt", "w")

totalCase = int(readline(fIn))
inp = [map(float, split(readline(fIn))) for caseNo in 1:totalCase]
# for caseNo in 1:totalCase
    # @printf("%s\n", solve(inp[caseNo]))
# end
res = map(solve, inp)
for caseNo in 1:totalCase
    println(fOut, "Case #$caseNo: $(res[caseNo])")
end
