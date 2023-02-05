use proconio::input;
fn main() {
    input! {
        n: usize,
        x: usize,
        nums: [usize; n],
    }
    for i in 0..n {
        if nums[i] == x {
            println!("{}", i+1);
        }
    }
}
