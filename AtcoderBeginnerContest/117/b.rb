N = gets.to_i
L_list = gets.split.map(&:to_i)
L_list.sort!
L_list_max = L_list.pop
sum = 0
L_list.each{|i| sum += i}
if sum > L_list_max
    puts "Yes"
else
    puts "No"
end
