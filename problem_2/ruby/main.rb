last = 1
sum = current = 2

while current < 4_000_000
  tmp = last + current
  sum += tmp if tmp.even?
  last = current
  current = tmp
end

puts sum