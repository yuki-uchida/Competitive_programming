N,M = gets.chomp.split(" ").map(&:to_i)
A = gets.chomp.split(" ").map(&:to_i)

# A.map! {|box| box%M}

choise = 0
len = A.length
A.each_with_index do |num,i|
  count = num
  choise = choise + 1 if count % M == 0
  if i != len - 1
    i.upto(len-1) do |j|
      if j != len-1
        count = count + A[j+1]
        if count % M == 0
          choise = choise + 1
        end
      end
    end
  end
end

puts choise
