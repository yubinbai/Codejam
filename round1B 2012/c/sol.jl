function solve(inp)
    N = int(inp[1])
    A = inp[2:end]
    d = Dict()

    # After choosing t sets, there will be t choose 2 pairs, and each
    # set will have sum at most 6 * 1012. Therefore, the expected
    # number of collisions would be approximately t2 / (12 * 10^12).
    # When t is around 10^6, this expectation will be near 1, and the
    # reasoning from the birthday paradox says that we'll likely
    # have our collision.

    while true
        # generate new selection
        sel = zeros(Int, 6)
        while true
            rand!(1:N, sel)
            sort!(sel)
            worked = true
            for i in 2:6
                if sel[i - 1] == sel[i]
                    worked = false
                end
            end
            if worked
                break
            end
        end
        sel = [A[sel[i]] for i in 1:6]
        sort!(sel)
        s = sum(sel)
        if haskey(d, s) && d[s] != sel
            return join(d[s], ' '), join(sel, ' ')
        else
            d[s] = copy(sel)
        end
    end
    return "not", "found"
end


fIn = open("input.txt", "r")
fIn = open("c-small.in", "r")
# fIn = open("c-large.in", "r")
fOut = open("output.txt", "w")

totalCase = int(readline(fIn))
inp = [map(int, split(readline(fIn))) for caseNo in 1:totalCase]
for caseNo in 1:totalCase
    res = solve(inp[caseNo])
    @printf(fOut, "Case #%d: \n%s\n%s\n", caseNo, res[1], res[2])
end
# res = map(solve, inp)
# for caseNo in 1:totalCase
#     println(fOut, "Case #$caseNo: $(res[caseNo])")
# end
