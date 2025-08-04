// let promise = new Promise(function(resolve, reject) {
//     let success = true;
  
//     if(success) {
//       resolve("Data loaded successfully!");
//     } else {
//       reject("Failed to load data!");
//     }
//   });
  
//   promise
//     .then(function(result) {
//       console.log(result); // success
//     })
//     .catch(function(error) {
//       console.log(error); // failed
//     });

paymentSuccess = true;
let marks = 80;

function enroll() {
    console.log("Enrolling...");
    const promise = new Promise(function(resolve, reject) {
        if (paymentSuccess) {
            resolve("Payment successful");
        } else {
            reject("Payment failed");
        }
    });
    return promise;
}   

function progress() {
    console.log("Processing...");
    const promise = new Promise(function(resolve, reject) {
        if (marks >= 80) {
            resolve("You are eligible for the certificate");
        } else {
            reject("You are not eligible for the certificate");
        }
    });
    return promise;
}

function getCertificate() {
    console.log("Getting certificate...");
    const promise = new Promise(function(resolve, reject) {
        if (marks >= 80) {
            resolve("You are eligible for the certificate");
        } else {
            reject("You are not eligible for the certificate");
        }
    });
    return promise;
}


enroll()
    .then(progress)
    .then(getCertificate)
    .catch(function(error) {
        console.log(error);
    });


