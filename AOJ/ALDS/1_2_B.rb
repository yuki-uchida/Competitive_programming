##選択ソート

A = gets.to_i 
b = gets.chomp.split(" ").map(&:to_i)
sorted_list = []
sort_count = 0
b.each_with_index do |num,i|
    min_index = 0 
    min_num = -1
    (i).upto(A-1) do |j|
        if min_num >= 0
            num_index = (min_num > b[j]) ? [b[j], j] : [min_num, min_index]
            min_num, min_index = num_index[0],num_index[1]
        else
            min_num = b[j]
            min_index = j
        end
    end
    if b[i] != b[min_index]
        b[i],b[min_index] = b[min_index],b[i]
        sort_count += 1
    end
end
output_string = ""
b.each_with_index do |num,i|
    if i == 0
        output_string = "#{num}"
    else
        output_string = output_string + " #{num}"    
    end
end
puts output_string
p sort_count
