fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    N = int(readline(fIn))
    req = (Int, Int)[]
    for i in 1:N
        a, b = map(int, split(readline(fIn)))
        push!(req, (b, a))
    end
    sort!(req, rev=true)
    s1 = falses(N)
    s2 = falses(N)
    twoDone = N
    cost = 0 
    currS = 0
    for i in 1:2N
        while twoDone >= 1 && req[twoDone][1] <= currS
            if !s2[twoDone]
                if !s1[twoDone]
                    s1[twoDone] = s2[twoDone] = true
                    currS += 2
                    cost += 1
                else
                    s2[twoDone] = true
                    currS += 1
                    cost += 1
                end
            end
            twoDone -= 1
        end
        if currS == 2N
            break
        end
        for j in 1:twoDone
            if req[j][2] <= currS && !s1[j]
                s1[j] = true
                currS += 1
                cost += 1
                break
            end
        end
    end
    @printf(fOut, "Case #%d: %s\n", caseNo, (currS == 2N) ? cost : "Too Bad")
end