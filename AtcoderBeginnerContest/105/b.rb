N = gets.chomp.to_i

max_cake = N/4

can_buy = false
max_cake.times do |i|
  if N%4 == 0
    can_buy = true
    break
  elsif (N-(4*(i))) % 7 == 0
    can_buy = true
    break
  end
end

if can_buy
  puts "Yes"
else
  puts "No"
end
