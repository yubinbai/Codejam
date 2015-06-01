function solve(seq)
    seqv = int128(seq)
    seq = [c for c in seq]
    N = length(seq)
    sorted = sort!(copy(seq))
    if seq == nthperm(sorted, factorial(int128(N)))
        push!(seq, '0')
        reverse!(seq)
        first = 1
        while seq[first] == '0'
            first += 1
        end
        seq[1] = seq[first]
        seq[first] = '0'
        return join(seq)
    end
    low, high = int128(1), int128(factorial(N))
    while low < high
        mid = (low + high) >> 1
        v = int128(join(nthperm(sorted, mid)))
        if v > seqv
            high = mid
        else
            low = mid + 1
        end
    end
    join(nthperm(sorted, low))
end

fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(strip(readline(fIn))))
end
