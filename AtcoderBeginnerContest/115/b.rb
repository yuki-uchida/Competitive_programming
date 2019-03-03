N = gets.chomp.to_i
p_s = []
N.times do |i|
    p_s << gets.chomp.to_i
end

p_s = p_s.sort
sum = 0
p_s.each_with_index do |p, i|
    if i == p_s.length-1
        sum = sum + p/2
    else
        sum = sum + p
    end
end

puts sum
