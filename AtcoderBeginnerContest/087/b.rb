a = gets.chomp.to_i
b = gets.chomp.to_i
c = gets.chomp.to_i
x = gets.chomp.to_i
count = 0

0.upto(a) do |i|
  0.upto(b) do |s|
    0.upto(c) do |m|
      if (500*i)+(100*s)+(50*m) == x
        count += 1
      end
    end
  end
end
puts count
