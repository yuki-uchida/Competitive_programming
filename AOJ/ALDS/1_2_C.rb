def bubble_sort(n,nums)
    0.upto(n-1) do |i|
        #N-1=4
        (n-1).downto(0) do |j|
            if nums[j][:value] < nums[j-1][:value] && j != 0
                nums[j], nums[j-1] = nums[j-1], nums[j]
            end
        end
    end
    return nums
end

def selection_sort(a,b)
    b.each_with_index do |num,i|
        min_index = 0 
        min_num = -1
        (i).upto(a-1) do |j|
            if min_num >= 0
                num_index = (min_num > b[j][:value]) ? [b[j][:value], j] : [min_num, min_index]
                min_num, min_index = num_index[0],num_index[1]
            else
                min_num = b[j][:value]
                min_index = j
            end
        end
        if b[i][:value] != b[min_index][:value]
            b[i],b[min_index] = b[min_index],b[i]
        end
    end
    return b
end

N = gets.chomp.to_i
cards_list = gets.chomp.split(" ")
hashed_cards_list = []
cards_list.each do |card|
    hashed_card = {}
    hashed_card[:suit], hashed_card[:value] =  card.split("")[0], card.split("")[1].to_i
    hashed_cards_list << hashed_card
end
bubble_sorted_cards_list = bubble_sort(N,hashed_cards_list.clone)
selection_sorted_cards_list = selection_sort(N,hashed_cards_list.clone)

stable = true
bubble_sorted_cards_list.length.times do |i|
    if bubble_sorted_cards_list[i][:suit] != selection_sorted_cards_list[i][:suit]
        stable = false
    end
end
output_string1 = ""
bubble_sorted_cards_list.each_with_index do |card,i|
    if i != 0
        output_string1 = output_string1 + " #{card[:suit]}#{card[:value]}"
    else
        output_string1 = "#{card[:suit]}#{card[:value]}"
    end
end
output_string2 = ""
selection_sorted_cards_list.each_with_index do |card,i|
    if i != 0
        output_string2 = output_string2 + " #{card[:suit]}#{card[:value]}"
    else
        output_string2 = "#{card[:suit]}#{card[:value]}"
    end
end
puts output_string1
puts "Stable"
puts output_string2
if stable
    puts "Stable"
else
    puts "Not stable"
end
