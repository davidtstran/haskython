incList :: [Integer] -> [Integer]
incList [] = []
incList (x:xs) = x+1 : incList xs

decList :: [Integer] -> [Integer]
decList [] = []
decList (x:xs) = x-1 : decList xs

sumList :: [Integer] -> Integer
sumList [] = 0
sumList (x:xs) = x + sumList xs

power :: Integer -> Integer -> Integer
power x 0 = 1
power x 1 = x
power x y = x * power x (y - 1)
