function solve(seq, dict)

    function works(x, w1, w2)
        L = length(w1)
        C = 0
        prevC = x * -1
        for i in 1:L
            if w1[i] != w2[i]
                if (i - prevC + 1) <= 5
                    return false, 0, 0
                else
                    prevC = i
                    C += 1
                end
            end
        end
        true, C, min(6, L - prevC + 1)
    end

    N = length(seq)
    memo = ones(Int, N + 1, 6) * 10000
    # for each prefix of the given word what's the smallest number of substitutions needed to 
    # form this word so that the last substitution was k characters ago, for k = 1, 2, 3, ...
    memo[1, 6] = 0
    for i1 = 1:N
        for i2 in 1:i1
            for w in dict[i1 - i2 + 1]
                for x in 1:6
                    worked, C, last = works(x, seq[i2:i1], w)
                    # worked, C, last = true, 6, 6
                    if worked
                        memo[i1 + 1, last] = min(memo[i1 + 1, last], C + memo[i2, x])
                    end
                end
            end
        end
    end
    minimum(memo[N + 1, 1:6])
end

fDict = open("garbled_email_dictionary.txt", "r")
# dict = [Set{ASCIIString}() for i in 1:60]
dict = [ASCIIString[] for i in 1:10]
for line in eachline(fDict)
    s = strip(line)
    push!(dict[length(s)], s)
end

fIn = open("input.txt", "r")
# fIn = open("A-small-practice.in", "r")
# fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    result = solve(strip(readline(fIn)), dict)
    println(fOut, "Case #$caseNo: $result")
end
