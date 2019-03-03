rows,column = gets.chomp.split(" ").map(&:to_i)
boxes = []
rows.times do |row|
  columns = gets.chomp.split("").map(&:to_s)
  boxes << columns
end
boxes.each_with_index do |row,y|
  row.each_with_index do |point,x|
    if point != "#"
      count = 0
      check_list = [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
      check_list.each do |check|
        if (check[1] >= 0 && check[1] < rows)&&(check[0] >= 0 && check[0] < column)
          if boxes[check[1]][check[0]] == "#"
            count += 1
          end
        end
      end
      boxes[y][x] = count
    end
  end
end

boxes.each do |row|
  ans = ""
  row.each do |point|
    ans += point.to_s
  end
  puts ans
end

