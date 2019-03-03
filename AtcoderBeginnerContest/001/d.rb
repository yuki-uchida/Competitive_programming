N = gets.chomp.to_i
times = []
N.times do |i|
  from,to = gets.chomp.split("-").map(&to_i)
  time = [from,to]
  times << time
end

ans_times = []
#N =6
N.times do |i|
  times[i][0]
end
