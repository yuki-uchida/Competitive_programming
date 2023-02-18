use proconio::{input};
use std::collections::HashMap;
fn main() {
    input! {
        nums: [usize; 5],
    }
    let mut hash = HashMap::new();
    for x in nums {
        if hash.contains_key(&x) {
            hash.insert(x, hash.get(&x).unwrap() + 1);
        } else {
            hash.insert(x, 1);
        }
    }
    // println!("{:?}", hash);
    if hash.keys().len() != 2 {
        println!("No");
    } else {
        let mut ans = true;
        for key in hash.keys() {
            if *hash.get(&key).unwrap() == 2 as i32 || *hash.get(&key).unwrap() == 3 as i32 {
                ans = true;
            } else {
                ans = false;
            }
        }
        if ans == true {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
