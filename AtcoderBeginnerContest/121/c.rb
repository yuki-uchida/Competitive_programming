N,M = gets.split.map(&:to_i)
hash = {}
N.times do |i|
    a,b = gets.split.map(&:to_i)
    if hash[a]
        hash[a] += b
    else
        hash[a] = b
    end 
end

array = hash.sort

sum_drink = 0
sum_price = 0
array.each_with_index do |d,i|
    if M >= (sum_drink + d[1])
        sum_price += d[0] * d[1]
        sum_drink += d[1]
    else
        sum_price += d[0] * (M - sum_drink)
        sum_drink = M
    end
end

puts sum_price
