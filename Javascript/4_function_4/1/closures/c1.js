// function bankAccount(initialBalance){
//     let balance = initialBalance;
//     return function(){
//         return balance;
//     }
// }

// const account = bankAccount(1000);

// console.dir(account);

// function bankAccount(initialBalance){
//     let balance = initialBalance;
//     function getBalance(){
//         return balance;
//     }
//     function deposit(amount){
//         balance += amount;
//     }
//     function withdraw(amount){
//         balance -= amount;
//     }
//     return {getBalance, deposit, withdraw};

// }
// const account = bankAccount(1000);
// console.dir(account);


let num1 = 80
let num2 = 20
//it is a closure because num1 and num2 are in the scope of add3
let add3 = function () {
    let num3 = 50;
    return function () {
        return num1 + num2 + num3;
    }
}
// this is most common use of closure
let sum3 = add3();
console.dir(sum3);
console.log(sum3());

