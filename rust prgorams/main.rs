use std::io;

fn main() {
    let mut thing = String::new();
    println!("...what are you doing?");
    io::stdin()
        .read_line(&mut thing)
        .expect("Did not get that");
    println!("AY THIS MAN {}", thing);
}
