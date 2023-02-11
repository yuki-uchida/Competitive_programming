use proconio::{input};
use std::collections::HashSet;
use std::iter::FromIterator;
fn main() {
    input! {
        nums: [usize; 5],
    }
    // println!("{:?}", nums);
    let set: HashSet<usize> = HashSet::from_iter(nums.iter().cloned());
    println!("{:?}", set.len()); 
}
