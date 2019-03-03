K,A,B = gets.chomp.split(" ").map(&:to_i)

#まず A-1ステップが必要
##そこからA=>B で何枚増えるか  == B-A (2ステップ)
n = (K-(A-1))/2
j = K - ((A-1)+(2*n))

if B-A >= 2
    p n*(B-A)+A+j
else
    p 1+K
end
