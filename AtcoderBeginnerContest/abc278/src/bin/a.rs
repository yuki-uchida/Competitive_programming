use proconio::input;
use std::collections::VecDeque;
fn main() {
    input! {
        n: usize,
        mut k: usize,
        nums: [usize; n],
    }
    k = k.min(n);
    for i in k..n {
        print!("{} ", nums[i]);
    }
    for _ in (n-k)..n {
        print!("0 ",);
    }
}
