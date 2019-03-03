N = gets.chomp.to_i
start = [0,0]
points = []
N.times do |i|
  points << gets.chomp.split(" ").map(&:to_i)
end
ans = ""
#元の位置に戻る方法 x+1 x-1, y+1 y-1,x+1 y+1 x-1 y-1,
points.each_with_index do |point,i|
  # point = [3,1,2]
  if i == 0

    if point[0] == point[1] + point[2]
      ans = "Yes"
    else
      ans = "No"
      break
  end
  else
    number = point[0] - points[i-1][0]
    x_move = points[i-1][1] - point[1]
    y_move = points[i-1][2] - point[2]
    if number == x_move + y_move
      ans = "Yes"
    elsif number > x_move + y_move
      if (number - x_move - y_move) % 2 == 0
        ans = "Yes"
      else
        ans = "No"
        break
      end
    else
      ans = "No"
      break
    end
  end
end

puts ans
