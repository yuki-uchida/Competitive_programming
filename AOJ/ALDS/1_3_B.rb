n,q = gets.chomp.split(" ").map(&:to_i)
tasks = []
n.times do |i|
    task = gets.chomp.split(" ")
    hash = {}
    hash[task[0].to_sym] = task[1].to_i
    tasks << hash
end

p tasks
time_count = 0
tasks.each_with_index do |task_hash,i|
    hash_key
    task_hash[]
    tasks << task_hash
end
