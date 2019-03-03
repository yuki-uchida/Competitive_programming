require "matrix"

N,K = gets.chomp.split(" ").map(&:to_i)
foods = [[],[]]
N.times do
  food = gets.chomp.split(" ").map(&:to_i)
  foods[0] << food[0]
  foods[1] << food[1]
end

foods

food_nums = foods[0].uniq.length

:wq

