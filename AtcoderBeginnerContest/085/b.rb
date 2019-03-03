N = gets.chomp.to_i
diameters = []
N.times do |i|
  diameters << gets.chomp.to_i
end
diameters.uniq!
puts diameters.length
