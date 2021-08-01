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

mytake :: Int -> [a] -> [a]
mytake a [] = []
mytake n (x:xs) = if n <= 0 then [] else x:(mytake (n-1) xs)

mydrop :: Int -> [a] -> [a]
mydrop a [] = []
mydrop n (x:xs) = if n <= 0 then (x:xs) else mydrop (n-1) xs

rev :: [a] -> [a]
rev s = func s []
    where func [] acc = acc
          func (x:xs) acc = func xs (x:acc)

app :: [a] -> [a] -> [a]
app a [] = a
app [] b = b
app (x:xs) b = x: (app xs b)
