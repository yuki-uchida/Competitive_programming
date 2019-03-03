numbers = gets.chomp.split("").map(&:to_i)
count = 0
numbers.each do |number|
  if number == 1
    count += 1
  end
end
puts count
