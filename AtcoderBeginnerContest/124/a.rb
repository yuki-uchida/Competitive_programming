A,B = gets.chomp.split(" ").map(&:to_i)

if A > B + 1
    puts A+A-1
elsif A+1 < B
    puts B+B-1
else
    puts A+B
end
