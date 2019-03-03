h = gets.chomp.to_i
if h < 100
  vv = 0
  vv = "%02d" % vv
elsif (100 <= h)&&(h <= 1000)
  vv = (h.to_f/1000)*10
  vv = "%02d" % vv
elsif (1000 <=  h)&&(h <= 5000)
  vv = ((h.to_f/1000)*10)
  vv = vv.to_i
elsif (6000 <= h)&&(h <= 30000)
  vv = (h.to_f/1000) + 50
  vv = vv.to_i
elsif (35000 <= h)&&(h <= 70000)
  vv = (h/1000 - 30)/5 + 80
  vv = vv.to_i
elsif (70000 < h)
  vv = 89
end
puts vv
