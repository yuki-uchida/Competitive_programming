N = gets.chomp.to_i
alice = 0
bob = 0
cards = gets.chomp.split(" ").map(&:to_i) 
cards.sort!{|a, b| b <=> a }
cards.each_with_index do |card,i|
  if i%2 == 0
    alice += card
  else
    bob += card
  end
end

puts alice-bob
