check num
    -- elem num list(or str): True or Falseが返る 
    | num `elem` "24579" = "hon"
    | num `elem` "0168" = "pon"
    | num `elem` "3" = "bon"

main = do
    nums <- getLine
    putStrLn . check . last $ nums