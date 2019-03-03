num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
array = gets.chomp.split(";")
# array = ["three","seve"]

ans = ""
array.each do |i|
    ans = num.index(i).to_s
end
p array
#puts ans    
