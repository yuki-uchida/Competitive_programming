use proconio::{input};
fn main() {
    input! {
        a: usize,
        b: usize,
    }
    // 1 => 01
    // 2 => 10
    // 3 => 11
    // 4 => 100
    // 5 => 101
    // 6 => 110
    // 7 => 111
    println!("{}", a | b);
}
