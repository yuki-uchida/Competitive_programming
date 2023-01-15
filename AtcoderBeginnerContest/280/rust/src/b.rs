use proconio::input;
fn main() {
    input! {
        string_length: usize,
        nums: [isize; string_length],
    };
    print!("{} ", nums[0]);
    for i in 1..string_length {
        print!("{} ", nums[i] - nums[i-1]);
    }
}
