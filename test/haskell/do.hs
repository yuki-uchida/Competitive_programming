import Control.Applicative
main = do
    -- ss <- words <$> getLine
    -- putStrLn (head ss)
    -- ss <- (map read . words) <$> getLine
    -- putStrLn $ show $ foldl (+) 0 ss
    [a,b] <- words <$> getLine
    (c:cs) <- getLine
    print $ (c:cs)
    -- puts cs