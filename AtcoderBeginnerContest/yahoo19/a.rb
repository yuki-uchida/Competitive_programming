N,K = gets.chomp.split(" ").map(&:to_i)
if N >= K*2-1
    puts("YES")
else
    puts("NO")
end
