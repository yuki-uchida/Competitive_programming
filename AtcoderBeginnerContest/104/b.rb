str = gets.chomp.split("").map(&:to_s)



if str[0] == "A"
  str_len = str.length
  has_c = false
  c_index = 0
  for i in 2..(str_len-2)
    if str[i] == "C"
      if has_c == true
        has_c = false
        break
      else
        has_c = true
        c_index = i
      end
    end
  end
  if str[str_len-1] == "C"
    has_c = false
  end
  if has_c
    str2 = str
    has_ac = false
    if str2[0] == str[0].tr('a','A')
      if str2[c_index] == str[c_index].tr('c','C')
        has_ac = true
      end
    end
    if has_ac
      str2.delete("A")
      str2.delete("C")
      has_upother = false
      str2.each do |char|
        if char == char.upcase
          has_upother = true
        else
        end
      end
      unless has_upother
        puts("AC")
      else
        puts("WA")
      end
    else
      puts("WA")
    end
  else
    puts("WA")
  end
else
  puts("WA")
end
