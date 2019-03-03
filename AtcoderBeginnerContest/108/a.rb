K = gets.chomp.to_i

if K % 2 == 0
  puts (K/2)**2
else
  puts (K/2)*(K/2+1)
end
