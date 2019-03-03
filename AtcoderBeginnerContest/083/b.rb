n,a,b, = gets.chomp.split(" ").map(&:to_i)
ans = 0
1.upto(n) do |i|
    sum = 0
    array = i.to_s.split("").map(&:to_i)
    array.each do |num|
      sum += num
    end
    if (sum >= a)&&(sum <= b)
      ans += i
    end
end
puts ans
