function solve(N, A)
    function F(t)
        sqrt((x + vx * t)^2 + (y + vy * t)^2 + (z + vz * t)^2)
    end
    x, y, z, vx, vy, vz = [sum([A[i][j] for i in 1:N]) * 1.0 / N for j in 1:6]
    epi = 1e-10
    if abs(vx) < epi && abs(vy) < epi && abs(vz) < epi
        return @sprintf("%.7f %.7f", sqrt(x^2 + y^2 + z^2), 0.0)
    end

    lo = 0.0
    hi = 100000000.0
    for ii in 1:100000
        m1 = (lo * 2 + hi) / 3
        m2 = (lo + hi * 2) / 3
        d1 = F(m1)
        d2 = F(m2)
        if (d1 < d2) 
            hi = m2
        else 
            lo = m1
        end
    end

    @sprintf("%.7f %.7f", F(lo), lo)
end


fIn = open("input.txt", "r")
fIn = open("B-small-practice.in", "r")
fIn = open("B-large-practice.in", "r")
fOut = open("output.txt", "w")
totalCase = int(readline(fIn))
for caseNo in 1:totalCase
    N = int(readline(fIn))
    A = [map(int, split(strip(readline(fIn)))) for i in 1:N]
    # @printf("Case #%d: %s\n", caseNo, solve(inp[caseNo]))
    @printf(fOut, "Case #%d: %s\n", caseNo, solve(N, A))
end