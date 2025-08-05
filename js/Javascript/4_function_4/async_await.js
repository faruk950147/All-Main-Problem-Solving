let paymentSuccess = true;
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

async function courseFlow() {
    try {
        await enroll();
        await progress();
        await getCertificate();
    } catch (err) {
        console.log(err);
    }
}
courseFlow();

