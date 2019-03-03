N = gets.chomp.to_i
nums = gets.chomp.split(" ").map(&:to_i)
output_str = ""
nums.length.times do |i|
    if i >= 1
        i.times do |j|
            if nums[j] > nums[i]
                nums[i],nums[j] = nums[j],nums[i]
            end
        end
    end

    nums.each_with_index do |num, o_i|
        if o_i == nums.length-1
            output_str = output_str + "#{num}" + "\n"
        else
            output_str = output_str + "#{num} "
        end
    end
end
puts output_str
