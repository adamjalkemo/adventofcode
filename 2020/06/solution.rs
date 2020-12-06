use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::string::String;
use std::collections::HashSet;

fn main() {
    // Create a path to the desired file
    let path = Path::new("input.txt");
    let input = read_file(path);
    part1(&input);
    part2(&input);
}

fn part1(input: &String) {
    println!("Part 1:");
    let mut sum = 0;
    for group_answers in input.split("\n\n") {
        let letters = group_answers.replace("\n", "");
        let unique_letters: HashSet<char> = letters.chars().collect();
        sum += unique_letters.len();
    }
    println!("Solution: The sum of counts is {}", sum);
    assert!(sum == 7120);
}

fn part2(input: &String) {
    println!("Part 2:");
    let mut sum = 0;
    for group_answers in input.split("\n\n") {
        let possible_answers: HashSet<char> = group_answers.replace("\n", "").chars().collect();
        let mut intersection_of_answers = possible_answers.clone();
        for person_answers in group_answers.split("\n") {
            let answers: HashSet<char> = person_answers.chars().collect();
            intersection_of_answers = intersection_of_answers.intersection(&answers).cloned().collect();
        }
        sum += intersection_of_answers.len();
    }
    println!("Solution: The sum of counts is {}", sum);
    assert!(sum == 3570);
}

fn read_file(path: &Path) -> String {
    let display = path.display();

    // Open the path in read-only mode, returns `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    // Read the file contents into a string, returns `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => (),
    }

    return s;
}