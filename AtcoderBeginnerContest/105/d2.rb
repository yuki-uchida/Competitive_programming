N,M = gets.chomp.split(" ").map(&:to_i)
A = gets.chomp.split(" ").map(&:to_i)


cum = [0]
##合計を配列の中に入れていく
(0..N-1).each do |i|
    cum << cum[i] + A[i]
end

##配列の中身を全てあまりにする
cum.map!{ |c| c % M }

#余りによって何個あるかをハッシュに入れる
  ##ここで重要なのは、cum[i]-cum[r]のi,rの組み合わせを探すこと。
  ##cum[i]-cum[r]をMで割った余りが0の時を探したい
  ##=>cum[i]とcum[r]の余りが等しい時にはcum[i]-cum[r]をMで割った余りが0の時
  ##hashにまとめる
hash = {}
cum.each do |c|
    if hash.has_key?(c)
        hash[c] += 1
    else
        hash[c] = 1
    end
end

count = 0
hash.values.each do |v|
  ##後は余りが同じ同士の組み合わせを計算すれば良い
  next if v == 1
  ##二つの組み合わせを選ぶためnP2
  count += v * (v - 1) / 2
end
p count

