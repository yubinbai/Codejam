using Base.Profile
# If a number only has factors 2, 3, and 5, it is an ugly number. For example,
# 6 and 10 are two  ugly numbers, but 14 is not because it has a factor of 7.
# Usually 1 is considered to be the first ugly number.
# What  is the arbitrary k th ugly number?



function uglyNumbers(size)
    results = map(BigInt, [2, 3, 5])

    pointer2 = 1
    pointer3 = 2
    pointer5 = 3
    for i in 4:size
        currMin = min(results[pointer2] << 1, results[pointer3] * 3, results[pointer5] * 5)

        while results[pointer2] << 1 <= currMin
            pointer2 += 1
        end

        while results[pointer3] * BigInt(3) <= currMin
            pointer3 += 1
        end

        while results[pointer5] * BigInt(5) <= currMin
            pointer5 += 1
        end

        push!(results, currMin)
    end
    results
end

@time results = uglyNumbers(100000)
# @profile uglyNumbers()
# Profile.print(format=:flat)
# println("join(results, ' ') $(join(results, ' '))")
println(results[end])
