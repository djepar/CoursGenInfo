use assert_cmd::Command;
use predicates::prelude::*;
use std::fs;


type TestResult = Result<(), Box<dyn std::error::Error>>;



//testing the 4 files 
fn run(args: &[&str], expected_file: &str) -> TestResult {
    let expected = fs::read_to_string(expected_file)?;
    Command::cargo_bin("echor")?
        .args(args)
        .assert()
        .success()
        .stdout(expected);
    Ok(())
}


//test to be sure it's show the help documentation if the system crash  
#[test]
fn dies_no_args() {
    let mut cmd = Command::cargo_bin("echor").unwrap();
    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("USAGE"));
}



#[test]
fn hello1() -> TestResult {
    run(&["Hello there"], "tests/expected/hello1.txt")
}

#[test]
fn hello1n() -> TestResult {
    run(&["Hello there", "-n"], "tests/expected/hello1.n.txt")
}


#[test]
fn hello2() -> TestResult {
    run(&["Hello", "there"], "tests/expected/hello2.txt")
}

#[test]
fn hello2n() -> TestResult {
    run(&["Hello", "there", "-n"], "tests/expected/hello2.n.txt")
}