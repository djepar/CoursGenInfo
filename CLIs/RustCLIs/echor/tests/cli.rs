use assert_cmd::Command;
use predicates::prelude::*;
use std::fs;


type TestResult = Result<(), Box<dyn std::error::Error>>;



//test to be sure it's show the help documentation if the system crash  
#[test]
fn dies_no_args() {
    let mut cmd = Command::cargo_bin("echor").unwrap();
    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("USAGE"));
}

//running the arg hello should exit the program 
#[test]
fn runs() {
    let mut cmd = Command::cargo_bin("echor")?;
    cmd.arg("hello").assert().success();
    
}

#[test]
fn hello1(){
    let outfile = "tests/expected/hello1.txt";
    let expected = fs::read_to_string(outfile)?;
    let mut cmd = Command::cargo_bin("echor")?;
    cmd.arg("Hello there").assert().success().stdout(expected);
}