blue_num = gets.chomp.to_i
blue_cards = []
blue_num.times do |i|
  blue_cards << gets.chomp.to_s
end
red_num = gets.chomp.to_i
red_cards = []
red_num.times do |i|
  red_cards << gets.chomp.to_s
end
yen = []
blue_cards.each_with_index do |blue_card,i|
   add_count = blue_cards.select {|t| t == blue_card}.length
   remove_count = red_cards.select {|t| t == blue_card}.length
   yen << add_count - remove_count
end
yen.sort!{|a, b| b <=> a }
if yen.first < 0
  puts 0
else
  puts yen.first
end
