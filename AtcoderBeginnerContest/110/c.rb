s = gets.chomp.split("").map(&:to_s)
t = gets.chomp.split("").map(&:to_s)

s_count = Hash.new(0)
s.each do |elem|
  s_count[elem] += 1
end

t_count = Hash.new(0)
t.each do |elem|
  t_count[elem] += 1
end


s_num = s_count.values.sort!
t_num = t_count.values.sort!


if s_num == t_num
  puts "Yes"
else
  puts "No"
end
