type Point
    x::Real
    y::Real
end

function signedArea2(p0, p1, p2)
    return p0.x * p1.y + p2.x * p0.y + p1.x * p2.y - p2.x * p1.y - p0.x * p2.y - p1.x * p0.y
end

function area(p0, p1, p2)
    return 0.5 * abs(signedArea2(p0, p1, p2))
end

a, b, c = Point(-1,0), Point(0, 5), Point(5, 0)
@time for i in 1:10000000
    ar2 = signedArea2(a, b, c)
end

# println("ar2 $(ar2)")
# println("area(a, b, c) $(area(a, b, c))")