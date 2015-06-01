function subsets{T}(seq::Array{T})
    function _subsets(step)
        push!(results, copy(path))
        for i in step:length(seq)
            push!(path, seq[i])
            _subsets(i+1)
            pop!(path)
        end
    end
    results = Array[]
    path = T[]
    _subsets(1)
    return results
end

seq = [i for i in "abbc"]
@time s = subsets(seq)
@printf("length %d\n", length(s))
for i in 1:length(s)
    println("[$(join(s[i], ", "))]")
end