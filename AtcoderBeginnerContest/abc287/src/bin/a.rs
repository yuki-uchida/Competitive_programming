use proconio::{input};
fn main() {
    input! {
        n: usize,
        mut answers: [String; n],
    }
    let count:usize = answers.iter().filter(|&ans| ans == "For").count();
    // println!("{}", count);
    let div: usize = ((n as f32 / 2.0)).ceil() as usize;
    // println!("{}", div);
    if count >= div {
        print!("Yes");
    } else {
        print!("No");
    }
}
