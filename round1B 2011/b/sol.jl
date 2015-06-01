fIn = open("input.txt", "r")
fOut = open("output.txt", "w")

function test(vendors, t, d)
    v = copy(vendors)
    v[1] -= t 
    v[end] += t
    left, right = 2, length(vendors) - 1
    while left < right
        leftPt = v[left-1] + d
        if leftPt <= v[left]-t
            v[left] = v[left]-t
        elseif v[left] - t <= leftPt && leftPt <= v[left] + t
            v[left] = leftPt
        else
            return false
        end
        rightPt = v[right+1] - d
        if rightPt >= v[right] + t
            v[right] = v[right] + t
        elseif v[right] - t <= rightPt && rightPt <= v[right] + t
            v[right] = rightPt
        else
            return false
        end
        left += 1
        right -= 1
    end
    len = length(vendors)
    if len % 2 == 1
        mid = (len + 1) / 2
        # valid range
        leftPt = max(v[mid] - t, v[mid-1] + d)
        rightPt = min(v[mid] + t, v[mid+1] - d)
        return leftPt <= rightPt
    else
        return v[len/2+1] - v[len/2] >= d
    end
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
        # @printf(fOut, "max %.9f min %.9f mid %.9f diff %e\n", maxT, minT, mid, maxT - minT)
    end
    @printf(fOut, "Case #%d: %.7f\n", caseNo, minT)
end