//Convert strings to pig latin. The first consonant of each word
// is moved to the end of the word and “ay” is added, so “first” 
//becomes “irst-fay.” Words that start with a vowel have “hay”
// added to the end instead (“apple” becomes “apple-hay”). 
//Keep in mind the details about UTF-8 encoding!
fn main() {
    let mut stringy = String::from("Hello");
    let first_vowel = stringy[0];
    let mut newstring = &stringy[1..4]; 
    if start_with_vowel == true { 
        newstring += "-";
        newstring += "";
        newstring += "ay";
    }

}

fn _starting_vowel(s :Vec<char>) -> bool {
    let vowel = ['a', 'e','i', 'o', 'u', 'A','E','I','O','U'];
    for letter in vowel {
        if s[0] == letter {
            return false
        }
    }
    return true
}

/*
fn starting_vowel(s :String) -> bool {
    let first_letter = &s[0];
    let vowel = ['a', 'e','i', 'o', 'u'];
    for letter in &vowel {
        if first_letter == letter {
            return false
        }
    }
    return true
}

 */