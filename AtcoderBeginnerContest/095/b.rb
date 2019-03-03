N, M, X = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i)
#0<=Xの時
ans1 = a.select{|num| num < X}.length
#X=>5の時
ans2 = a.select{|num| num > X}.length

ans = ans1>ans2 ? ans2 : ans1
puts ans
