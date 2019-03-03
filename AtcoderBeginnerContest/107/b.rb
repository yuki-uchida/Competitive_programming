H,W = gets.chomp.split(" ").map(&:to_i)
math = []
H.times do |i|
  gyou = gets.chomp.split("")
  math << gyou
end

new_math = []
math.each_with_index do |gyou, i|
  if gyou.count(".") != W
    new_math << gyou
  end
end

delete_math = []
new_math[0].length.times do |i|
  delete = true
  new_math.each_with_index do |gyou, j|
    if gyou[i] == "#"
      delete = false
    end
  end
  delete_math << delete
end


answer = []
new_math.each_with_index do |gyou,i|
  new_array = []
  delete_math.each_with_index do |n,j|
    if n == false
      new_array << gyou[j]
    end
  end
  answer << new_array
end


answer.each_with_index do |gyou, i|
  output = ""
  gyou.each do |char|
    output = output+char
  end
  print(output+"\n")
end
