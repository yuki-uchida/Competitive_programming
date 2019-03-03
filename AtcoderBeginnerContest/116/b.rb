s = gets.chomp.to_i
int_dic = {}
i = 1
while true do
  if int_dic[s.to_s.to_sym]
    int_dic[s.to_s.to_sym] += 1
    break
  else
    int_dic[s.to_s.to_sym] = 1
  end
  if s%2 == 0
    s = s/2
  else
    s = s*3 + 1
  end
  i += 1
end

puts i
