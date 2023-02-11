use proconio::{input};
use std::collections::HashMap;

fn main() {
    input! {
        day: String,
    }
    let mut weekday: HashMap<String, usize> = HashMap::new();
    weekday.insert("Monday".to_string(), 5);
    weekday.insert("Tuesday".to_string(), 4);
    weekday.insert("Wednesday".to_string(), 3);
    weekday.insert("Thursday".to_string(), 2);
    weekday.insert("Friday".to_string(), 1);
    println!("{}", weekday.get(&day).unwrap());
}
