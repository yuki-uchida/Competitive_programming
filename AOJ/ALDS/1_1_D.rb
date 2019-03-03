N = gets.chomp.to_i
nums = []
N.times do |i|
    nums << gets.chomp.to_i
end

min_num = nums[0]
max_num = -1000000000
nums.each_with_index do |num, i|
    # puts "#{max_num},#{min_num}"
    if i < nums.length && i >= 1
        max_num = num - min_num > max_num ? num - min_num : max_num
        min_num = num < min_num ? num : min_num
    end
end
p max_num
