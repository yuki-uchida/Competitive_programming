N,K = gets.chomp.split(" ").map(&:to_i)

candles = gets.chomp.split(" ").map(&:to_i)

array = []

zero_check = false

if candles.index(0)
  zero_check = true
end



if zero_check

  (N-K+1).times do |i|
    combination = []
    K.times do |j|
      combination << candles[i+j]
    end
    array << combination
  end

else
  candles << 0
  candles.sort!
  (N-K+1).times do |i|
    combination = []
    (K+1).times do |j|
      combination << candles[i+j]
    end
    array << combination
  end
end



new_array = []
array.each do |combi|
  if combi.index(0)
    new_array << combi
  end
end


answer = []
new_array.each_with_index do |combi,i|
  lefts = combi.select{|n| n < 0}
  if lefts.min
    left_sum = lefts.min.abs
  else
    left_sum = 0
  end
  rights = combi.select{|n| n > 0}
  if rights.min
    right_sum = rights.max
  else
    right_sum = 0
  end
  answer << (left_sum*2+right_sum)
  answer << (left_sum+right_sum*2)
end

answer.sort!
p answer[0]

