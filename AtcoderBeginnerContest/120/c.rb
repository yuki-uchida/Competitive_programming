S = gets.chomp.split("").map(&:to_i)
zero_count = 0
one_count = 0
S.each do |num|
    if num == 0
        zero_count += 1
    else
        one_count += 1
    end
end

if zero_count >= one_count
    puts one_count*2
else
    puts zero_count*2
end
