type FenwickTree{T}

    tree::Array{T, 1}

    function FenwickTree{T}(size::Int, v::T)
        a = 1
        while a <= size
            a = a << 1
        end
        new([v for i in 1:a])
    end

end

FenwickTree(size, v) = FenwickTree{typeof(v)}(size::Int, v)

function increase{T}(t::FenwickTree{T}, idx::Int, delta::T)
    while idx + 1 < length(t.tree)
        t.tree[idx + 1] += delta
        idx |= idx + 1
    end
end

function getSum{T}(t::FenwickTree{T}, left::Int, right::Int)
    if right >= left
        _sum(t, right) - _sum(t, left - 1)
    else
        throw(BoundsError())
    end
end

function _sum{T}(t::FenwickTree{T}, idx)
    currSum = 0
    while idx >= 0
        currSum += t.tree[idx + 1]
        idx &= idx + 1
        idx -= 1
    end
    return currSum
end

N = 10000000

t = FenwickTree(N, 0.0)
println("typeof(t) $(typeof(t))")


for i in 1:N
    increase(t, i, i*1.0)
end

@time for i in 1:N
    BigFloat(getSum(t, 1, i))
end

# println(getSum(t, 100, 1))

