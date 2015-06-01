
fIn = open("input.txt", "r")
# fIn = open("a-small.txt", "r")
# fIn = open("a-large.txt", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    n, m = map(int, split(readline(fIn)))
    dict = [strip(readline(fIn)) for i in 1:n]
    len = map(length, dict)

    # println(dct)
    result = [""] 
    for i in 1:m
        trial = strip(readline(fIn))
        words = solve(dct, trial)
        idx = typemax(Int)
        for w in words
            idx = minimum(idx, search(allWords, w))
        end 
        push!(results, allWords[idx])
    end
    println("Case #$caseNo:$(join(result, ' '))")
end
