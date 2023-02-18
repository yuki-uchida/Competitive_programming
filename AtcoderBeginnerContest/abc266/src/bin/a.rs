use proconio::{input};

fn main() {
    input! {
        mut text: String,
    }
    let text_length: usize = text.chars().count();

    println!("{}", text.chars().nth(text_length / 2).unwrap());
}
