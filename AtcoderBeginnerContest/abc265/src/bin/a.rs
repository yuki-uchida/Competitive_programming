use proconio::{input};

fn main() {
    input! {
        x: usize,
        y: usize,
        n: usize,
    }
    let mut min_payment: usize = y*n;
    for y_i in 0..=(n/3) {
        let x_i = n-(3*y_i);
        if (y*y_i) + (x*x_i) < min_payment {
            min_payment = (y*y_i) + (x*x_i);
        }
    }
    println!("{}", min_payment);
}
