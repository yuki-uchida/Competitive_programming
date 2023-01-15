use proconio::input;
fn main() {
    input! {
        n: usize,
        mut texts: [String; n],
    };
    let mut ans = true;
    let first_string_vector = vec!["H","D","C","S"];
    let second_string_vector = vec!["A","2","3","4","5","6","7","8","9","T","J","Q","K"];
    for i in 0..n{
        let a_text = &texts[i];
        if !first_string_vector.iter().any(|e| e.chars().nth(0).unwrap() == a_text.chars().nth(0).unwrap()) {
            // println!("{:?} => first", a_text);
            ans = false;
        }
        if !second_string_vector.iter().any(|e| e.chars().nth(0).unwrap() == a_text.chars().nth(1).unwrap()) {
            // println!("{:?} => second", a_text);
            ans = false;
        }
        for j in (i+1)..n {
            let b_text = &texts[j];
            if !first_string_vector.iter().any(|e| e.chars().nth(0).unwrap() == b_text.chars().nth(0).unwrap()) {
                // println!("{:?} => first", b_text);
                ans = false;
            }
            if !second_string_vector.iter().any(|e| e.chars().nth(0).unwrap() == b_text.chars().nth(1).unwrap()) {
                // println!("{:?} => second", b_text);
                ans = false;
            }
            if a_text == b_text {
                // println!("{:?}, {:?} => same", a_text,b_text);
                ans = false;
            }

        }
    }
    if ans {
        println!("Yes");
    }else{
        println!("No");
    }
}
