N = gets.chomp.split("").map(&:to_i)
p "999999999".split("").length
all_data = []
[3,5,7].repeated_combination(N.length-1) do |x|
    p x 
    if x.uniq.length == 3 
        all_data << x
    end
end
p all_data
