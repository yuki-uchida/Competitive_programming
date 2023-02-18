use proconio::{input};

fn main() {
    input! {
        left: usize,
        right: usize,
    }
    let text: String = "atcoder".to_string();
    println!("{}", &text[left-1..right]);
}
