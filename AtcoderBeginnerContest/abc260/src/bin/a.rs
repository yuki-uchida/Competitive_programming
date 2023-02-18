use proconio::{input};
use std::collections::HashMap;
fn main() {
    input! {
        text: String,
    }
    let mut hash = HashMap::new();
    for x in text.chars()  {
        if hash.contains_key(&x) {
            hash.insert(x, hash.get(&x).unwrap() + 1);
        } else {
            hash.insert(x, 1);
        }
    }
    for key in hash.keys() {
        if *hash.get(&key).unwrap() == 1 as i32 {
            println!("{}", key);
            return
        } 
    }
    println!("-1");
}
