N,K = gets.chomp.split(" ").map(&:to_i)
A = gets.chomp.split(" ").map(&:to_i)
total = {}
A.each do |i|
  unless total[i]
    total[i] = 1
  else
    total[i] = total[i] + 1
  end
end
sum = 0
total = total.values
total = total.sort {|a, b| b <=> a }
K.times do |i| # 2
  if total[i]
    sum = sum + total[i]
  end
end
