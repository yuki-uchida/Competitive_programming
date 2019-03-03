nums = []
nums << gets.chomp.split(" ").map(&:to_i)
nums << gets.chomp.split(" ").map(&:to_i)
nums << gets.chomp.split(" ").map(&:to_i)
nums.flatten!
hash = {}
nums.each do |num|
    if hash[num]
        hash[num] += 1
    else
        hash[num] = 1
    end
end

if hash.find {|k,v| v >= 3 }
    puts "NO"
else
    puts "YES"
end
