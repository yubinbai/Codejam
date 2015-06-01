function uniqueSubsets{T}(seq::Array{T})
    function _uniqueSubsets(step)
        push!(results, copy(path))
        for i in step:length(seq)
            if i != step && seq[i] == seq[i-1]
                continue
            end
            push!(path, seq[i])
            _uniqueSubsets(i+1)
            pop!(path)
        end
    end
    results = Array[]
    path = T[]
    _uniqueSubsets(1)
    return results
end

seq = [i for i in "abbcdefghijklmnopqrstuvw"]
@time s = uniqueSubsets(seq)
@printf("length %d\n", length(s))
for i in 1:10
    println("[$(join(s[i], ", "))]")
end
# for i in uniqueSubsets(seq)
#     # @printf("%s\n", typeof(i))
#     print_joined(STDOUT, i, ",")
#     # println(i)
# end
