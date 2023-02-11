use proconio::{input};
fn main() {
    input! {
        text: String,
    }
    // println!("{:?}", text);
    if let Some(i) = text.rfind("a") {
        println!("{}", i + 1);
    } else {
        println!("{}", -1);
    }
}
