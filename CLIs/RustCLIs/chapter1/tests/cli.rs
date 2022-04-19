use std::process::Command;

#[test]

fn run() {
    let mut cmd = Command::new("hello");
    let res = cmd.output();
    assert!(res.is_ok());

}