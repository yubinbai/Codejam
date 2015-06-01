A = 0
B = 100
pnt = [i for i in 1:(B - A + 1)]
rank = zeros(Int, B - A + 1)

function find(i)
    if pnt[i] != i
        pnt[i] = find(pnt[i])
    end
    return pnt[i]
end

function union(i, j)
    p1 = find(i)
    p2 = find(j)
    if rank[p1] < rank[p2]
        pnt[p1] = p2
    else
        pnt[p2] = p1
        if rank[p1] == rank[p2]
            rank[p1] += 1
        end
    end
end


# test
for i in 1:80
    a = rand(A:B, 2)
    union(a[1] - A + 1, a[2] - A + 1)
end
println("join(pnt, ' ') $(join(pnt, ' '))")
a = Set()
for c in pnt
    push!(a, c)
end
println("length(a) $(length(a))")
