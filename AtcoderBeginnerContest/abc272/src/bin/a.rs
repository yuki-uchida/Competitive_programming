use proconio::{input};
fn main() {
    input! {
        n: usize,
        nums: [usize; n],
    }
    println!("{}", nums.iter().sum::<usize>());
}
