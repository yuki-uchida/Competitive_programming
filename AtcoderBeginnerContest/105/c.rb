n = gets.chomp.to_i
change = []
if n != 0
  while n != 1 do
    if n < 0 #正の時の計算
      if n % (-2) != 0
        d = 1
        n = n / (-2) + 1
      else
        d = n % (-2)
        n = n / (-2)
      end
    else #負の時の計算
      if n % (-2) != 0
        d = 1
        n = n / (-2) + 1
      else
        d = n % (-2)
        n = n / (-2)
      end
    end
    change.insert(0, d)
  end
  change.insert(0,n)

  answer = ""
  change.each do |char|
    answer =  answer + char.to_s
  end

  puts answer
else
  puts "0"
end
