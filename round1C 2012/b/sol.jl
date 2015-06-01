function solve(n, k, mat)
end


fIn = open("input.txt", "r")
# fIn = open("B-small-practice.in", "r")
# fIn = open("A-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    D, N, A = split(strip(readline(fIn)))
    D = float(D)
    N = int(N)
    A = int(A)
    t = float[]
    x = float[]
    for i in 1:N
        a, b = map(float, split(readline(fIn)))
        push!(t, a)
        push!(x, b)
    end


    result = solve(n, k, mat)
    println(fOut, "Case #$caseNo: $result")
end
