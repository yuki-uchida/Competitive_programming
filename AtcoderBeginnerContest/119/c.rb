N,A,B,C = gets.chomp.split(" ").map(&:to_i)

chops = []
N.times do |i|
    chops << gets.chomp.to_i
end
chops.sort!{|a, b| b <=> a }
similar_chops = []
goal_length = [A,B,C].sort{|a, b| b <=> a }
p goal_length
goal_length.each do |length|
    div_length = []
    chops.each do |chop|
        div_length << (chop-length).abs
    end
    div_length_sorted = div_length.sort
    use_chop_index = div_length.index(div_length_sorted[0])
    similar_chops << chops[use_chop_index]
    chops.delete_at(use_chop_index)
end
p similar_chops



