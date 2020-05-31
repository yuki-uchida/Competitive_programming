main = do
    n <- readLn
    if even n 
        then do
            putStrLn "Blue"
        else do
            putStrLn "Red"