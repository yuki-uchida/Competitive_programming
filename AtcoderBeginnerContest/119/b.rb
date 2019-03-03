N = gets.chomp.to_i
otoshidamas = []
N.times do |i|
    otoshidamas << gets.chomp.split(" ")
end
sum = 0
otoshidamas.each_with_index do |otoshidama,i|
    if otoshidama[1] == "JPY"
        sum += otoshidama[0].to_f
    else
        sum += (otoshidama[0].to_f * 380000.0)
    end
end

puts sum
