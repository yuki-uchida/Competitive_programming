use proconio::{input};
fn main() {
    input! {
        k: usize, 
    }
    let left = 21;
    let right = 00;
    println!("{}:{:02}", left + (k/60), right + (k%60));
}
