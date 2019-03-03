N,M,X,Y = gets.chomp.split(" ").map(&:to_i)

x = gets.chomp.split(" ").map(&:to_i)
y = gets.chomp.split(" ").map(&:to_i)

ok = false


(X+1..Y).each do |num|
  if x.select{|n| n < num}.length == x.length && y.select{|n| n >= num}.length == y.length
    ok = true
  end
end


if ok
  puts "No War"
else
  puts "War"
end
