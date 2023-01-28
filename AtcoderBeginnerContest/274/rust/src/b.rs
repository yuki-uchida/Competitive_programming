use proconio::{input, marker::Bytes};
use std::fmt;
use itertools::Itertools;
fn main() {
    input! {
        h: usize,
        w: usize,
        c: [Bytes; h], //h*w
    }
    let ans = (0..w).map(|j| c.iter().filter(|cs| cs[j] == b'#').count()).join(" ");
    println!("{}", ans);
}
