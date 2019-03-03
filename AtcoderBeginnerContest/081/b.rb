N = gets.chomp.to_i
numbers = gets.chomp.split(" ").map(&:to_i)
count = 0
while numbers.select{ |n| n%2 != 0}.empty? do
  numbers = numbers.map{|number| number / 2 }
  count += 1
end


puts count
