use proconio::input;
use std::collections::VecDeque;
fn main() {
    input! {
        n: usize,
        k: usize,
        nums: [usize; n],
    }
    let mut nums_vec = VecDeque::new();
    for num in nums {
        nums_vec.push_back(num);
    }
    for _ in 0..k {
        nums_vec.pop_front();
        nums_vec.push_back(0);
    }
    println!("{:?}", nums_vec.join(" å"));
}
