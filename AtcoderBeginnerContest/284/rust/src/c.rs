use proconio::input;
use std::collections::HashSet;
fn main() {
    input! {
        n: usize,
        m: usize,
        uv: [(usize, usize);m],
    };
    let mut point_to_points = vec![Vec::new(); n];
    for (u,v) in uv {
        point_to_points[u-1].push(v-1);
        point_to_points[v-1].push(u-1);
    }
    let mut checked_root_points = HashSet::new();
    let mut ans = 0;
    for start in 0..n {
        if checked_root_points.contains(&start) {
            continue;
        }
        checked_root_points.insert(start);
        ans += 1;
        let mut q = vec![start];
        while q.len() > 0 {
            let c = q.pop().unwrap();
            for next in &point_to_points[c] {
                if checked_root_points.contains(next) {
                    continue;
                }
                checked_root_points.insert(*next);
                q.push(*next);
            }
        }
    }
    println!("{}", ans);
}
