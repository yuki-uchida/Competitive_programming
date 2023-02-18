use proconio::{input};

fn main() {
    input! {
        x: usize,
        y: usize,
        n: usize,
    }
    let mut min_payment: usize = y*n;
    for i in 0..=(n/3) {
        for j in (10-i)..=(n-(3*i)) {
            if (x*i)+(y*j) < min_payment {
                min_payment = (x*i)+(y*j);
            }
        }
    }
    println!("{}", min_payment);
}
