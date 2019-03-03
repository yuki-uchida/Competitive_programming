N,K = gets.chomp.split(" ").map(&:to_i)

combis = (1..N).to_a.map{|num| num%K}
count = 0

count = Hash.new(0)
combis.each do |elem|
  count[elem] += 1
end
ans = {}
count.each{|key, value|
  if (key+key)%K == 0
    ans[key] = value
  end
}
ans_count = 0
ans.each{|key, value|
  ans_count += value**3
}

p ans_count
