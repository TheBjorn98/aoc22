include("util.jl")

function part1()
    data = readfilebyday(1, 1)
    data = map(x -> parse(Int, x), data)
    @show data
end

part1()
