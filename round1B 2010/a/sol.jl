function solve(inp, test)
    s = Set()
    for line in inp
        a = split(line[2:end], '/')
        for i in 1:length(a)
            push!(s, join(a[1:i], '/'))
        end
    end
    cnt = 0
    for line in test
        a = split(line[2:end], '/')
        for i in 1:length(a)
            str = join(a[1:i], '/')
            if !(str in s)
                push!(s, join(a[1:i], '/'))
                cnt += 1
            end
        end
    end
    cnt
end

fIn = open("input.txt", "r")
fIn = open("A-small-practice.in", "r")
fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    N, M = map(int, split(readline(fIn)))
    inp = [strip(readline(fIn)) for i in 1:N]
    test = [strip(readline(fIn)) for i in 1:M]
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(inp, test))
end