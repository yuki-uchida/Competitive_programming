def g(x)
    ramains_list =  (x/4*4..x).to_a
    return ramains_list.inject(:^)
end

A, B = gets.split.map(&:to_i)

p g(B) ^ g(A-1)
