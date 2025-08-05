// ******************************* symbol and bigint in JavaScript ******************************

// ******************************* do while loop in JavaScript ******************************
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 5);

// ******************************* while loop in JavaScript ******************************
let j = 0;
while (j < 5) {
    console.log(j);
    j++;
}

// ******************************* for loop in JavaScript ******************************
for (let k = 0; k < 5; k++) {
    console.log(k);
}

// ******************************* break and continue in JavaScript ******************************
for (let k = 0; k < 5; k++) {
    if (k == 3) {
        break;
    }
    console.log(k);
}
    
for (let k = 0; k < 5; k++) {
    if (k == 3) {
        continue;
    }
    console.log(k);
}       

// ******************************* nested loop in JavaScript ******************************
for (let k = 0; k < 5; k++) {
    for (let l = 0; l < 5; l++) {
        console.log(k, l);
    }
}

// ******************************* switch case in JavaScript ******************************
let day = 3;
switch (day) {
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    case 4:
        console.log("Thursday");
        break;
    case 5:
        console.log("Friday");
        break;
    case 6:
        console.log("Saturday");
        break;
    case 7:
        console.log("Sunday");
        break;
    default:
        console.log("Invalid day");
}

