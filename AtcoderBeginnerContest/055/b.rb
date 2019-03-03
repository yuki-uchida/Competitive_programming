N = gets.chomp.to_i
power = 1
N.times do |i|
  power = power*(i+1)%1000000007
end
puts power
