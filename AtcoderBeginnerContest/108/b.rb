x1,y1,x2,y2 = gets.chomp.split(" ").map(&:to_i)

#これは必ず右上に向かう直線になっているはず。
vec = [x2-x1,y2-y1]

vec90 = [-vec[1],vec[0]]

ans = "#{(x2+vec90[0]).to_s} #{(y2+vec90[1]).to_s} #{(x1+vec90[0]).to_s} #{(y1+vec90[1]).to_s}"
puts ans
