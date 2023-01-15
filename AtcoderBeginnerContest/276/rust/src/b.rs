use proconio::input;
fn main() {
    input! {
        n: usize,
        m: usize,
        mut roads: [(usize, usize); m],
    }
    // println!("{:?}", roads);
    let mut connected_cities: Vec<Vec<i32>> = vec![vec![]; n+1];
    let mut connected_cities_count: Vec<i32> = vec![0; n+1];
    for i in 0..m {
        let a_city: i32 = (roads[i].0 as i32);
        let b_city: i32 = (roads[i].1 as i32);
        connected_cities[a_city as usize].push(b_city);
        connected_cities[b_city as usize].push(a_city);
        connected_cities_count[a_city as usize] += 1;
        connected_cities_count[b_city as usize] += 1;
    }
    // println!("{:?}", connected_cities);
    // println!("{:?}", connected_cities_count);
    for j in 1..(n+1) {
        connected_cities[j as usize].sort();
        let connected_cities: Vec<String> = connected_cities[j as usize].iter().map(|i: &i32| i.to_string()).collect();
        let connected_cities_str: String = connected_cities.join(" ");
        println!("{} {}", connected_cities_count[j], connected_cities_str);
    }
}
