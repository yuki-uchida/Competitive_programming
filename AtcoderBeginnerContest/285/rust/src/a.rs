use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize
    }
    if b >= a*2 && b <= a*2 + 1 {
      println!("Yes");
    } else {
      println!("No");
    }
}
