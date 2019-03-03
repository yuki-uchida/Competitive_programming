N = gets.chomp.to_i
points = []
1.upto(N) do |i|
  points << gets.chomp.split(" ").map(&:to_i)
end
max = 0
points.each do |point1|
  points.each do |point2|
    x = (point1[0]-point2[0])**2
    y = (point1[1]-point2[1])**2
    if max < x+y
      max = x+y
    end
  end
end
puts Math.sqrt(max)
puts "\n"
