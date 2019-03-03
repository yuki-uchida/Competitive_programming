N = gets.chomp.to_i
flowers_high = gets.chomp.split(" ").map(&:to_i)

new_list = []
flowers_high.each_with_index do |num,i|
  if i == 0
    new_list << num
  else
    new_list << num - flowers_high[i-1]
  end
end


puts new_list.select{|num| num >= 0}.inject(:+)
