use assert_cmd::Command;

#[test]

fn runs() {
    let mut cmd = Command::cargo_bin("ls").unwrap();
    let res = cmd.output();
    assert!(res.is_ok());
}

fn true_ok() {
    let mut cmd = Command::cargo_bin("true").unwrap();
    cmd.assert().success();
}

fn false_not_ok() {
    let mut cmd = Command::cargo_bin("false").unwrap();
    cmd.assert().failure();
}