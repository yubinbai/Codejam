function solve(seq, dict)

    function diffs(w1, w2)
        L = length(w1)
        C = Int[]
        prevC = -5
        for i in 1:L
            if w1[i] != w2[i]
                if i - prevC < 5
                    return false, C
                else
                    prevC = i
                    push!(C, i)
                end
            end
        end
        true, C
    end

    N = length(seq)
    memo = ones(Int, N + 1, 5) * 10000
    # for each prefix of the given word what's the smallest number of substitutions needed to 
    # form this word so that the last substitution was k characters ago, for k = 1, 2, 3, ...
    memo[1, 5] = 0
    for i1 = 1:N
        for i2 in max(1, i1 - 9):i1
            for w in dict[i1 - i2 + 1]
                work, C = diffs(seq[i2:i1], w)
                if !work
                    continue
                end
                if length(C) == 0
                    for x in 1:5
                        last = min(5, x + length(w))
                        memo[i1 + 1, last] = min(memo[i1 + 1, last], memo[i2, x])
                    end
                    continue
                end
                for x in 1:5
                    if C[1] + x > 5
                        last = min(5, length(w) - C[end] + 1)
                        memo[i1 + 1, last] = min(memo[i1 + 1, last], length(C) + memo[i2, x])
                    end
                end
            end
        end
    end
    minimum(memo[N + 1, 1:5])
end

fDict = open("garbled_email_dictionary.txt", "r")
# dict = [Set{ASCIIString}() for i in 1:10]
dict = [ASCIIString[] for i in 1:10]
for line in eachline(fDict)
    s = strip(line)
    push!(dict[length(s)], s)
end

fIn = open("input.txt", "r")
# fIn = open("C-small-practice.in", "r")
# fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    result = solve(strip(readline(fIn)), dict)
    # println(fOut, "Case #$caseNo: $result")
    println("Case #$caseNo: $result")
end
