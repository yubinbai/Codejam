fIn = open("input.txt", "r")
fOut = open("output.txt", "w")
for caseNo in 1:int(readline(fIn))
    n = int(readline(fIn))
    mat = [readline(fIn) for i in 1:n]
    wp = Float64[]
    for i in 1:n
        num = den = 0
        for j in 1:n
            if mat[i][j] == '1'
                num += 1
                den += 1
            elseif mat[i][j] == '0'
                den += 1
            end
        end
        push!(wp, num/den)
    end
    owp = Float64[]
    for currT in 1:n
        wpT = Float64[]
        for i in 1:n
            num = den = 0
            for j in 1:n
                if i == currT || j == currT
                    continue
                end
                if mat[i][j] == '1'
                    num += 1
                    den += 1
                elseif mat[i][j] == '0'
                    den += 1
                end
            end
            if num == 0 && den == 0
                push!(wpT, 0)
            else
                push!(wpT, num/den)
            end
        end
        played = Float64[]
        for i in 1:n
            if mat[currT][i] != '.'
                push!(played, wpT[i])
            end
        end
        # println("$currT, [$(join(played, ','))]")
        push!(owp, sum(played)/length(played))
    end
    oowp = Float64[]
    for currT in 1:n
        played = Float64[]
        for i in 1:n
            if mat[currT][i] != '.'
                push!(played, owp[i])
            end
        end
        push!(oowp, sum(played)/length(played))
    end

    # println("[$(join(wp, ','))]")
    # println("[$(join(owp, ','))]")
    # println("[$(join(oowp, ','))]")
    @printf(fOut, "Case #%d:\n", caseNo)
    for i in 1:n
        @printf(fOut, "%.8f\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25)
    end
end

