function validatePIN (pin) {
    return /(^\d{4}$)/.test(pin) || /(^\d{6}$)/.test(pin)
}

console.log(validatePIN('1234'))
console.log(validatePIN('12d34'))
console.log(validatePIN('123994'))