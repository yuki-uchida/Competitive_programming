N,M = gets.chomp.split(" ").map(&:to_i)
data = {}
M.times do 
    P,Y = gets.chomp.split(" ").map(&:to_i)
    if data[P]
        data[P] = data[P].push(Y).sort
    else
        data[P] = [Y]
    end
end

data.each do |num|
    a = num[0]
    b = new_hash[num[0]].index(num[1]) + 1
    puts ('%06d' % a)+('%06d' % b)
end
