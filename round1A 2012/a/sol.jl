fIn = open("input.txt", "r")
fIn = open("A-large.txt", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    a, b = map(int, split(readline(fIn)))
    rate = map(float, split(readline(fIn)))
    # println("a $a rate $(length(rate))")

    curr = BigFloat(1.0)
    mul = [curr]
    for r in rate
        curr *= r
        push!(mul, curr)
    end

    keep = mul[end] * (b - a + 1) + (1 - mul[end]) * (2b - a + 2)
    back = [b - a + 2k + 1 + (b + 1) * (1 - mul[a - k + 1]) for k in 1:a]
    enter = b + 2

    full = back[1:end]
    push!(full, keep)
    push!(full, enter)
    
    @printf(fOut, "Case #%d: %.7f\n", caseNo, minimum(full))
end