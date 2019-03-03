N = gets.chomp.to_i
red_points = []
blue_points = []
N.times do |i|
  red_points << gets.chomp.split(" ").map(&:to_i)
end
N.times do |i|
  blue_points << gets.chomp.split(" ").map(&:to_i)
end


answers = []
blue_points.each_with_index do |blue_point,i|
  answer = []
  red_points.each_with_index do |red_point,s|
    if (red_point[0] < blue_point[0])&&(red_point[1] < blue_point[1])
      answer << red_point
    end
  end
  answers << answer
end

count = 0
answers.sort_by! {|answer| answer.length}
ngs = []
answers.each do |answer|
  ans = answer
  ngs.each do |ng|
    ans.delete(ng)
  end
  if ans.length > 0
    count += 1
  end
  ngs << answer[0]
end
puts count
