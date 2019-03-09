
A,B = gets.split.map(&:to_i)

sum = 0
min_keta = 2**(A.to_s(2).length-1)
max_keta = 2**(B.to_s(2).length-1)
if (min_keta+1) == max_keta
    min_array = (A..min_keta).to_a
    min_array.each do |num|
        sum = sum ^ num
    end
    puts sum
else
    puts "aaa"
    loss_count = min_keta - A

    max_array = (max_keta..B).to_a
    p max_array
    max_array.each do |num|
        sum = sum ^ num
    end
    p sum
end
