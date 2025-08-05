// যখন অনেক asynchronous কাজ একটার পরে আরেকটা করতে হয়, এবং প্রতিটা কাজের জন্য আমরা একটা করে callback function ব্যবহার করি — তখন একসময় আমাদের কোড অনেকগুলো nested callback-এ ভরে যায়।
// এটাকেই বলে callback hell।


// callback hell is a situation where multiple nested callbacks are used to handle asynchronous operations, making the code difficult to read and maintain.
// doTask1(function(result1) {
//     doTask2(result1, function(result2) {
//       doTask3(result2, function(result3) {
//         doTask4(result3, function(result4) {
//           console.log("All tasks completed!");
//         });
//       });
//     });
//   });



let paymentSuccess = true;
let marks = 80;

function enroll(callback) {
    console.log("Enrolling...");
    setTimeout(() => {
        if (paymentSuccess) {
            console.log("Payment successful");
            callback();
        } else {
            console.log("Payment failed");
        }
    }, 2000);
}

function progress(callback) {
    console.log("Processing...");
    setTimeout(() => {
        if (marks >= 80) {
            console.log("You are eligible for the certificate");
            callback();
        } else {
            console.log("You are not eligible for the certificate");
        }
    }, 2000);
}

function getCertificate(callback) {
    console.log("Getting certificate...");
    setTimeout(() => {
        console.log("Certificate downloaded successfully!");
        callback();
    }, 2000);
}

// Callback Hell (Pyramid of Doom)
enroll(function() {
    progress(function() {
        getCertificate(function() {
            console.log("Course completed!");
        });
    });
});
  