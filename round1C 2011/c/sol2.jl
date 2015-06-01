# addprocs(4)

const MAXF = 1000000

@everywhere function allFactors(number)
    result = Uint[]
    for i in 1:int(sqrt(number)) + 1
        a, b = div(number, i), mod(number, i)
        if b == 0
            if i < a
                push!(result, i)
                push!(result, a)
            else
                if a == i
                    push!(result, a)
                end
                break
            end
        end
    end
    sort!(result)
end

@everywhere function solve(inp)
    N, L, H = inp[1:3]
    freq = inp[4:end]
    # Add 1 to the beginning of the list of inputs (in O(1) time :) )
    push!(freq, 1)
    N += 1
    sort!(freq)
    # Calculate the prefix LCMs and suffix GCDs (in O(N) GCD operations, 
    # each taking O(log H) time (as we do not consider results greater than H)

    # GCD(fk+1, ..., fN)
    GCD = copy(freq)
    for k in N-1:-1:1
        GCD[k] = gcd(freq[k], GCD[k + 1])
    end

    # LCM(f1, ..., fk)
    LCM = copy(freq)
    for k in 2:N
        currG = gcd(LCM[k - 1], freq[k])
        c = LCM[k - 1] * float(freq[k]) / float(currG)
        LCM[k] = (c >= MAXF) ? MAXF : LCM[k - 1] * freq[k] / currG
    end

    # println(join(freq, ' '))
    # println(join(GCD, ' '))
    # println(join(LCM, ' '))

    # interval fk and fk+1
    for k in 1:N - 1
        # For each k from 1 to N-1 check whether the appropriate LCM divides the appropriate GCD 
        # (if no, proceed to next interval);
        if GCD[k + 1] % LCM[k] != 0
            continue
        end
        # if the LCM falls into [L, H] (if yes, return the LCM) 
        if LCM[k] >= L && LCM[k] <= H
            return LCM[k]
        end
        # whether the intervals [LCM, GCD] and [L, H] intersect (if no, proceed to the next interval)
        left = max(LCM[k], L)
        right = min(GCD[k + 1], H)
        if left >= right
            continue
        end

        # If we are still analyzing this interval, find all the divisors of the GCD and 
        # check them one by one. This takes O(sqrt(H)) time.
        for f in allFactors(GCD[k + 1])
            if f % LCM[k] == 0 && f >= L && f <= H
                return f
            end
        end
    end

    # If no answer was found as yet, it remains to check the smallest multiple of 
    # the LCM of all the inputs that is greater or equal than L. This is done in constant time.
    d = div(L, LCM[end])
    rem = mod(L, LCM[end])
    if rem == 0
        return LCM[end]  
    elseif (d + 1) * LCM[end] <= H
        return (d + 1) * LCM[end]
    end
    return "NO"
end

fIn = open("input.txt", "r")
# fIn = open("C-small-practice.in", "r")
fIn = open("C-large-practice.in", "r")
fOut = open("output1.txt", "w")

totalCase = int(readline(fIn))
inp = [map(int, split(readline(fIn) * readline(fIn))) for caseNo in 1:totalCase]
for caseNo in 1:totalCase
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(inp[caseNo]))
end
# res = pmap(solve, inp)
# for caseNo in 1:totalCase
#     println(fOut, "Case #$caseNo: $(res[caseNo])")
# end
