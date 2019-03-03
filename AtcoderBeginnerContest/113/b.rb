N = gets.chomp.to_i
T, A = gets.chomp.split(" ").map(&:to_i)
h = gets.chomp.split(" ").map(&:to_i)
h2 = []
h.each do |i| 
    h2 << (A - (T - (i*0.006))).abs
end
puts h2.index(h2.min)+1