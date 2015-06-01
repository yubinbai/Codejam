function solve(seq, dict)

    function working(s)
        L = length(s)
        sa = [c for c in s]
        res = (Int, Int, Int)[]
        if s in dict[L]
            push!(res, (0, 1, 1))
        end
        # nC == 1
        for i in 1:L
            t = sa[i]
            sa[i] = '*'
            if join(sa) in dict[L]
                push!(res, (1, i, i))
            end
            sa[i] = t
        end
        # nC == 2
        if L < 6
            return res
        end
        for i in 1:L-5
            for ii in i+5:L
                t, tt = sa[i], sa[ii]
                sa[i] = sa[ii] = '*'
                if join(sa) in dict[L]
                    push!(res, (2, i, ii))
                end
                sa[i], sa[ii] = t, tt
            end
        end
        res
    end

    N = length(seq)
    memo = ones(Int, N + 1, 5) * 10000
    # for each prefix of the given word what's the smallest number of substitutions needed to 
    # form this word so that the last substitution was k characters ago, for k = 1, 2, 3, ...
    memo[1, 5] = 0
    for i1 = 1:N
        for i2 in max(1, i1 - 9):i1
            for (nC, firstC, lastC) in working(seq[i2:i1])
                L = i1 - i2 + 1
                if nC == 0
                    for x in 1:5
                        last = min(5, x + L)
                        memo[i1 + 1, last] = min(memo[i1 + 1, last], memo[i2, x])
                    end
                    continue
                else
                    for x in 1:5
                        if firstC + x > 5
                            last = min(5, L - lastC + 1)
                            memo[i1 + 1, last] = min(memo[i1 + 1, last], nC + memo[i2, x])
                        end
                    end
                end
            end
        end
    end
    minimum(memo[N + 1, 1:5])
end

fDict = open("garbled_email_dictionary.txt", "r")
dict = [Set{ASCIIString}() for i in 1:10]
for line in eachline(fDict)
    s = strip(line)
    L = length(s)
    sa = [c for c in s]
    push!(dict[L], s)
    # nC == 1
    for i in 1:L
        t = sa[i]
        sa[i] = '*'
        push!(dict[L], join(sa))
        sa[i] = t
    end
    # nC == 2
    if L < 6
        continue
    end
    for i in 1:L-5
        for ii in i+5:L
            t, tt = sa[i], sa[ii]
            sa[i] = sa[ii] = '*'
            push!(dict[L], join(sa))
            sa[i], sa[ii] = t, tt
        end
    end
end
# println(dict[1])

fIn = open("input.txt", "r")
fIn = open("C-small-practice.in", "r")
fIn = open("C-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    result = solve(strip(readline(fIn)), dict)
    println(fOut, "Case #$caseNo: $result")
    # println("Case #$caseNo: $result")
end
