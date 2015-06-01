function allFactors(number)
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

@time allFactors(120000000000000)