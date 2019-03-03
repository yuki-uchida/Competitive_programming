string = gets.chomp.to_s


string.gsub!("eraser","")
string.gsub!("erase","")
string.gsub!("dreamer","")
string.gsub!("dream","")



if string.empty?
  puts "YES"
else
  puts "NO"
end
