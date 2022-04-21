fn main() {
    let temp_f : f64 = 25.5;
    let temp_c : f64 = fahrenheit_to_celcius(temp_f);
    println!("The temperature in f is : {} and the temperature in C is : {} ", temp_f, temp_c);
    let temp_f : f64 = temp_c;
    let temp_f : f64 = fahrenheit_to_celcius(temp_f);
    println!("The temperature in f is : {} and the temperature in C is : {} ", temp_f, temp_c);
}

fn fahrenheit_to_celcius(temperature_f: f64) -> f64 {
    return (temperature_f - 32.0)*(5.0/9.0);
}


fn celcius_to_fahrenheit(temperature_c: f64) -> f64 {
    return temperature_c * (9.0/5.0)+32.0;
}
