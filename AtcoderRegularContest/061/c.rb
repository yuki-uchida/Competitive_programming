S = gets.chomp.split("").map(&:to_i)
list = []
['','+'].repeated_permutation(S.length-1) do |a|
  list << a
end
total = 0
list.each do |al|
  moji = []
  S.each_with_index do |sa, i|
    moji << sa
    moji << al[i] if i < al.length
  end
total += eval(moji.join)
end
puts total
