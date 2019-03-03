N = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)
num = a.length
num.times do |i|
  b = a.sort
  if i < num/2
    puts b[num/2]
  else

  end
end
