use proconio::input;

fn main() {
    input! {
        t: usize,
    };
    for _ in 0..t {
        input! {
            n: usize,
            mut nums: [usize; n],
        };
        println!("{}", nums.iter().filter(|&x| x % 2 == 1).count())
    }
}
