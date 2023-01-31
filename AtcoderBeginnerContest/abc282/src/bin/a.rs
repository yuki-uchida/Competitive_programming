use proconio::input;

fn main() {
    input! {
        k: usize
    }
    const abc: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    println!("{}", &abc[..k]);
}