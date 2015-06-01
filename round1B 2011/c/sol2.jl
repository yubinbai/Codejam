function getPoly(n, m, u, v)

    poly = Array{Int, 1}[] 
    push!(poly, [i for i in 1:n])
    # println("typeof $(typeof(poly))")

    for i in 1:m
        a, b = u[i], v[i]
        for (idx, p) in enumerate(poly)
            if in(a, p) && in(b, p)
                p1 = splice!(poly, idx)
                i1, i2 = findfirst(p1, a), findfirst(p1, b)
                # println("i1 $i1 i2 $i2")
                p2 = p1[i1:i2]
                p3 = vcat(p1[1:i1],  p1[i2:end])
                insert!(poly, idx, p2)
                insert!(poly, idx + 1, p3)
                # println("p2 $(join(p2, ' '))")
                # println("p3 $(join(p3, ' '))")
                break
            end
        end
    end
    # for p in poly
    #     println("p $(join(p, ' '))")
    # end
    poly
end

function getColor(poly, c, n)

    function fillP(currP)
        # fill currP
        # fill 1..c, fulfill all colors
        for c1 in 1:c
            if any([color[x] == c1 for x in currP])
                continue
            else
                for x in currP
                    if hasColor[x] == 0
                        color[x] = c1
                        hasColor[x] = 1
                        break
                    end
                end
            end
        end
        # fill c..end, no same color in adj
        for (i, x) in enumerate(currP)
            if hasColor[x] == 1
                continue
            else
                left = currP[(i == 1) ? length(currP) : i - 1]
                right = currP[(i == length(currP)) ? 1 : i + 1]
                for c1 in 1:c
                    if (color[left] != c1 || hasColor[left] == 0) && (color[right] != c1 || hasColor[right] == 0)
                        color[x] = c1
                        hasColor[x] = 1
                    end
                end
            end
        end
    end

    color = zeros(Int, n)
    hasColor = zeros(Int, n)
    # first one has inner edge (1, end)
    color[poly[1][1]] = 1
    color[poly[1][end]] = c
    currP = poly[1]

    while sum(hasColor) < n
        for p in poly
            sumC = sum([hasColor[x] for x in p])
            if sumC < length(p)
                fillP(p)
            end
        end
    end
    color
end

fIn = open("input.txt", "r")
fOut = open("output.txt", "w")

for caseNo in 1:int(readline(fIn))
    n, m = map(int, split(readline(fIn), ' '))
    u = map(int, split(readline(fIn), ' '))
    v = map(int, split(readline(fIn), ' '))

    poly = getPoly(n, m, u, v)
    c = minimum(map(length, poly))
    println(fOut, "Case #$caseNo: $c")

    color = getColor(poly, c, n)
    println(fOut, "$(join(color, ' '))")

end
