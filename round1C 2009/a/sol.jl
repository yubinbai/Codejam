function solve(inp)
    s = Set()
    for c in inp
        push!(s, c)
    end
    N = length(s)
    if N == 1
        return parseint("1"^length(inp), 2)
    end
    used = [false for i in 1:N]
    used[2] = true
    d = Dict()
    r = 0
    for (i, c) in enumerate(inp)
        r *= N
        if i == 1
            d[c] = 1
            r = 1
        elseif haskey(d, c)
            r += d[c]
        else
            for j in 1:N
                if !used[j]
                    d[c] = j - 1
                    used[j] = true
                    break
                end
            end
            r += d[c]
        end
    end
    r
end


fIn = open("input.txt", "r")
fIn = open("A-small-practice.in", "r")
# fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    # @printf("Case #%d: %s\n", caseNo, solve(inp[caseNo]))
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(strip(readline(fIn))))
end