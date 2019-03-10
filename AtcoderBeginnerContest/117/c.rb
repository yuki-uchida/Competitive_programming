n,m=gets.split.map(&:to_i)
x=gets.split.map(&:to_i)
if n>=m
    puts 0
else
    x.sort!
    # diffs=x.each_cons(2).map{|a,b|b-a}.sort
    diffs = []
    x.each_cons(2) do |a,b|
        diffs << b-a
    end
    diffs.sort!
    p diffs[0...m-n].inject(:+)
end
