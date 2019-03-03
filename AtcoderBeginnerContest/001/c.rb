dir,w = gets.chomp.split

dir = (dir.to_f%3600) / 10
w = (w.to_f/60).round(1)
direction = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"] #0~15

if (dir < 11.25) || (dir >= 348.75)
  ans_dir = direction[0]
else
  num = (dir - 11.25).div(22.5) + 1
  ans_dir = direction[num]
end
speeds = [0,0.2,1.5,3.3,5.4,7.9,10.7,13.8,17.1,20.7,24.4,28.4,32.6]
ans_speed = 0
speeds.each_with_index do |speed, i|

  if w == 0
    ans_speed = 0
    break
  elsif w <= speeds[i]
    ans_speed = i - 1
    break
  end
  ans_speed = 12
end

if ans_speed == 0
  ans_dir = "C"
end

puts ans_dir + " " + ans_speed.to_s
