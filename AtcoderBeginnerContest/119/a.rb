S = gets.chomp.split("/").map(&:to_i)
base = [2019,4,30]

if S[0] < base[0]
    puts "Heisei"
elsif S[0] > base[0]
    puts "TBD"
else
    if S[1] < base[1]
        puts "Heisei"
    elsif S[1] > base[1]
        puts "TBD"
    else
        if S[2] < base[2]
            puts "Heisei"
        elsif S[2] > base[2]
            puts "TBD"
        else
            puts "Heisei"
        end
    end
end
