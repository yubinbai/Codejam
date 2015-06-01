fIn = open("input.txt", "r")
fOut = open("output.txt", "w")

function test(vendors, t, d)
    last = typemin(Float64)
    for i in 1:length(vendors)
        z = vendors[i] - t
        y = last + d
        if (z < y)
            z = y
        end
        if (vendors[i] + t < z)
            return false
        end
        last = z
    end
    return true
end

for caseNo in 1:int(readline(fIn))
    c, d = map(int, split(readline(fIn), ' '))
    vendors = zeros(Float64, 0)
    for i in 1:c
        p, v = map(int, split(readline(fIn), ' '))
        for w in 1:v
            push!(vendors, float(p))
        end
    end
    minT, maxT = 0.0, 2e20
    while nextfloat(minT) < maxT
        mid = (minT + maxT) / 2
        if test(vendors, mid, d)
            maxT = mid 
        else
            minT = nextfloat(mid)
        end
    end
    @printf(fOut, "Case #%d: %.7f\n", caseNo, minT)
end