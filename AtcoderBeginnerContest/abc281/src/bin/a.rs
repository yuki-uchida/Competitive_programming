use proconio::input;
fn main() {
    input! {
        n: i32,
    }
    for i in (0..=n).rev() {
        println!("{}",i);
    }
}
