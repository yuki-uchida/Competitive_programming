use proconio::{input};
fn main() {
    input! {
        a: usize,
        b: usize,
    }
    println!("{:.3}", (b as f32 / a as f32 * (10i32.pow(3) as f32)).round() / (10i32.pow(3) as f32));
}
